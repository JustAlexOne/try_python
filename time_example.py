import time
import pytz
from datetime import datetime
from pytz import timezone

date_time = '08/29/2011 11:05:02'
pattern = '%m/%d/%Y %H:%M:%S'

parsed_date1 = datetime.strptime(date_time, pattern).astimezone(timezone('UTC'))
parsed_date2 = datetime.strptime(date_time, pattern).timestamp()
print('parsed_date1', parsed_date1)
print('parsed_date2', parsed_date2)
timestamp1 = parsed_date1.timestamp()
timestamp2 = parsed_date2.timestamp()
print('result1', timestamp1)
print('result2', timestamp2)
