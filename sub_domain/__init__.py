import json
import urllib.request

newConditions = {"con1": 40, "con2": 20, "con3": 99, "con4": 40, "password": "1234"}
params = json.dumps(newConditions).encode('utf8')
req = urllib.request.Request("http://www.baidu.com", data=params,
                             headers={'content-type': 'application/json'})
response = urllib.request.urlopen(req)
response.re
