import json


host = '6463'
engine_port = "4546"
payload = json.dumps({
    'name': host,
    'command-channel': [{'port': engine_port, 'secret': 'secret'}]
})

print("payload", payload) # payload {"name": "6463", "command-channel": [{"port": "4546", "secret": "secret"}]}