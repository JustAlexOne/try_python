#! /usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import json
import re
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE

import itertools
import requests
import smtplib

import time

import sys

url_search_tickets = 'http://booking.uz.gov.ua/purchase/search/'
url_station_id = 'http://booking.uz.gov.ua/purchase/station/?term='

form_data = {
    'station_id_from': '2210690',
    'station_id_till': '2204001',
    'station_from': 'Бердянськ',
    'station_till': 'Харків',
    'date_dep': '13.08.2017',
    'time_dep': '00:00',
    'time_dep_till': '',
    'another_ec': 0,
    'search': '',
}

global temp_text1
global temp_text2
global recipients
global creds
global gmail_server
gmail_server = None

mins_wait = 10
trains = 1
old_places = {}


def parse_len(list):
    if len(list) > 1: return True


def parse_places(list):
    types_list = list[0]['types']

    luxe_places = [type for type in types_list if type['id'] == 'Л']
    cupe_places = [type for type in types_list if type['id'] == 'К']
    platz_places = [type for type in types_list if type['id'] == 'П']

    luxe_places = check_places_present(luxe_places)
    cupe_places = check_places_present(cupe_places)
    platz_places = check_places_present(platz_places)

    places_dict = {'luxe_places': luxe_places, 'cupe_places': cupe_places, 'platz_places': platz_places}
    print("Current state: " + str(places_dict))
    return places_dict


def check_places_present(luxe_places):
    if (len(luxe_places) > 0):
        luxe_places = luxe_places[0]['places']
    else:
        luxe_places = 0
    return luxe_places


def send_data_request():
    print('sending request to PZ')
    resp = requests.post(url_search_tickets, data=form_data)
    # temp_text = '{"value":[{"num":"262П","model":0,"category":0,"travel_time":"10:09","from":{"station":"Бердянськ","date":1502431500,"src_date":"2017-08-11 09:05:00"},"till":{"station":"Харків-Пас","date":1502468040,"src_date":"2017-08-11 19:14:00"},"types":[{"id":"Л","title":"Люкс","letter":"Л","places":15},{"id":"К","title":"Купе","letter":"К","places":62},{"id":"П","title":"Плацкарт","letter":"П","places":1}],"allow_stud":1,"allow_transportation":1,"allow_booking":1,"allow_roundtrip":1}],"error":null,"data":null,"captcha":null}'
    # temp_text2 = '{"value":[{"num":"262П","model":0,"category":0,"travel_time":"10:09","from":{"station":"Бердянськ","date":1502604300,"src_date":"2017-08-13 09:05:00"},"till":{"station":"Харків-Пас","date":1502640840,"src_date":"2017-08-13 19:14:00"},"types":[{"id":"Л","title":"Люкс","letter":"Л","places":10},{"id":"К","title":"Купе","letter":"К","places":1}],"allow_stud":1,"allow_transportation":1,"allow_booking":1,"allow_roundtrip":1}],"error":null,"data":null,"captcha":null}'
    json_response = json.loads(resp.text)
    value = json_response['value']
    # print('Response from PZ', json.dumps(value, sort_keys=True, indent=4, ensure_ascii=False))
    assert resp.status_code == 200
    print('response recieved')
    return value


def send_email(places_map, body):
    print('sending email')
    global gmail_server
    gmail_server = gmail_server

    if not gmail_server:
        login_to_gmail()

    # Send the mail
    msg = create_msg(body, places_map)
    gmail_server.sendmail(creds[0], recipients, msg.as_string())
    print('email sent!')


def create_msg(body, places_map):
    msg = MIMEMultipart()
    msg['From'] = creds[0]
    msg['To'] = str(recipients)
    msg['Subject'] = "New changes to tickets detected"
    if body:
        msg.attach(MIMEText(create_msg_text(None, body)))
    else:
        msg.attach(MIMEText(create_msg_text(places_map, None)))
    return msg


def login_to_gmail():
    global gmail_server
    gmail_server = smtplib.SMTP('smtp.gmail.com', 587)
    # Next, log in to the server
    gmail_server.starttls()
    gmail_server.login(creds[0], creds[1])

def create_msg_text(new, body):
    res = ''
    if body:
        res = body
    else:
        res = f'New:\n{new}\nOld:\n{old_places}\n'
    res = res + '\nCheck it out: http://booking.uz.gov.ua/'
    return res


def wait(seconds):
    time_out = int(seconds / 60)
    print(f'Waiting for {time_out} minutes')
    time.sleep(seconds)

def wait_minutes(minutes):
    wait(minutes * 60)

def parse_available_trains(trains_list):
    global trains
    if (len(trains_list) == 0):
        text_new_train = 'No trains found :('
        print(text_new_train)
        trains = 0
        send_email(None, text_new_train)
        pass
    if (len(trains_list) > trains):
        text_new_train = 'New train is available :)'
        print(text_new_train)
        send_email(None, text_new_train)
        trains = len(trains_list)


def print_iteration_data():
    print('#', attempt)
    print('Time', time.strftime('%H:%M (%d.%m.%Y)'))  # 'Mon Oct 18 13:35:29 2010'

def read_cmd_arguments():
    parser = argparse.ArgumentParser(prog='pz_script')
    parser.add_argument('--date', '-d', help='please set a date using rather "-d" or "--date"', required=True)
    parser.add_argument('--fromC', '-f', help='please set a city "FROM" using rather "-f" or "--from"', required=True)
    parser.add_argument('--to', '-t', help='please set a city "TO" using rather "-t" or "--to"', required=True)
    return parser.parse_args()


def validate_arguments(arguments):
    city_from = arguments.fromC

    city_to = arguments.to

    date_dep = arguments.date
    date_regex = '^\d{1,2}\.\d{1,2}\.\d{4}$'

    if not re.match(date_regex, date_dep):
        raise ValueError('Incorrect date [{0}]. Should be in format "DD.MM.YYYY", e.g. "13.08.2017"'.format(date_dep))
    return (city_from, city_to, date_dep)

def exception_handler(exception_type, exception, traceback):
    # All your trace are belong to us!
    # your format
    print("%s: %s" % (exception_type.__name__, exception))

def get_station_id(station):
    response = requests.get(url_station_id + station)
    assert response.status_code == 200
    json_response = json.loads(response.text)
    if not json_response:
        raise ValueError('Unknown station "{}"'.format(station))

    titles = []
    for destination in json_response:
        titles.append(destination['title'])
    if station not in titles:
        raise ValueError('Unknown station "{}". Please specify the one from list: {}'.format(station, titles))
    station_id = json_response[0]['value']
    return station_id

def set_form_data(city_from, city_to, date_dep):
    form_data = {
        'station_id_from': get_station_id(city_from),
        'station_id_till': get_station_id(city_to),
        # 'station_from': 'Бердянськ',
        # 'station_till': 'Харків',
        'date_dep': date_dep,
        'time_dep': '00:00',
        'time_dep_till': '',
        'another_ec': 0,
        'search': '',
    }
    pass


if __name__ == '__main__':
    # ----- pre config --------
    sys.excepthook = exception_handler
    # -------------------------

    arguments = read_cmd_arguments()
    (city_from, city_to, date_dep) = validate_arguments(arguments)
    set_form_data(city_from, city_to, date_dep)

    creds = ('ukrnat19@gmail.com', 'ukrnat1991')
    recipients = [
        creds[0],
        'alex.cherevatiy@gmail.com',
        'annkorn13@gmail.com'
    ]

    for attempt in itertools.count(1):
        print_iteration_data()
        try:
            print(f'Searching tickets for {date_dep} from "{city_from}" to "{city_to}"')

            response = send_data_request()
            if 'Сервіс тимчасово недоступний.' in response:
                print('Service unavailable')
                wait_minutes(1)
                continue

            parse_available_trains(response)
            new_places = parse_places(response)

            if not old_places:
                old_places = new_places
                continue
            if old_places != new_places:
                print("Hooray! Updates found! :)")
                print(create_msg_text(new_places, None))
                send_email(new_places, None)
                old_places = new_places
            else:
                print('No updates found')
        except Exception as e:
            print('Caught exception', e.message)
        wait_minutes(mins_wait)
