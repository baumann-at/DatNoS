'''
DatNoS: "Data Notarization Service"
(c) 2019 - baumann.at

Example Code for DatNoS Client ("Sender")

Viewer-GUI: https://blockchains.web-lab.at/datnos

'''
import sys
import datetime
import hashlib
import json
import requests # install with "pip3 install requests" if necessary

print('DatNoS Sender ...')

url = 'https://test.baumann.at/dev9/datnos-api/'
apiToken = 'xxx' # contact Chris Baumann for a valid apiToken

# Build API request

# example for calculating a sha256 hash from a timestamp
timeStamp = datetime.datetime.now().isoformat()
tsHash = hashlib.sha256(timeStamp.encode('utf-8')).hexdigest()

# using keys allows faster access when searching data on the blockchain
keys = ['PY-key-321', 'ABC-keyz']

# data can hold any fields 
data = {
  'CardId': 123,
  'PubKey': '0x32952623945872634876234985769872345',
  'TimeStamp': timeStamp,
  'TimeStampHash': tsHash
}

# the request has to have "keys" and "data" elements
request = {'keys': keys, 'data': data}

postData = json.dumps(request)
#print(postData)
length = str(len(postData))

httpHeaders = {
  'Content-type':'application/json',
	'Accept':'application/json',
	'Content-Length': length,
	'X-ApiToken': apiToken}
#print(httpHeaders)

response = requests.post(url, data = postData, headers = httpHeaders)
print(str(response))
print('RESULT: ' + response.text) 
