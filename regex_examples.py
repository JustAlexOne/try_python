import re

some_date = '13.05.2017'
d_ = '^\d{1,2}\.\d{1,2}\.\d{4}$'
pattern = re.compile(d_)
res = re.match(d_, some_date)
if res:
    print(True)
print('res', res)