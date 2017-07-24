import pytoml as toml
import argparse
import re

with open('test.toml', 'rb') as fin:
    res = toml.load(fin)

print(res)

name = res['block'][0]['name']
print(name)