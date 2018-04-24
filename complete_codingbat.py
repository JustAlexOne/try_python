import argparse
import json
import re

import requests

USER_NAME = 'tester1@gmail.com'
PW = 'tester'

home_url = 'http://codingbat.com'
run_url = home_url + '/run'
login_url = home_url + '/login'


def startIt():
    form_data = {
        'id':'p187868',
        'code':'public boolean sleepIn(boolean weekday, boolean vacation) { return vacation || !weekday;}',
        'cuname': USER_NAME,
        # 'owner':'',
        # 'date':'290652149',
        # 'adate':'20170811-064002z',
    }
    # response = requests.post(run_url, data=form_data)
    session = login_to_codingbat()
    post_response = session.post(run_url, data=form_data)
    print(post_response.status_code)
    print('text', post_response.text)


def login_to_codingbat():
    print('Logging to {0}'.format(home_url))
    login_data = {
        'uname': USER_NAME,
        'fromurl': '/java',
        'pw': PW,
        'dologin': 'submit',
    }
    session = requests.session()
    response = session.post(login_url, login_data)

    assert response.status_code == 200
    assert 'Failed to login' not in response.text

    print('Logged in successfully'.format(home_url))
    return session

if __name__ == '__main__':
    startIt()