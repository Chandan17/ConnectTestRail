
from testrail import *

import json
import ConfigParser

config = ConfigParser.ConfigParser()
config.read('.\TestData\loginData.config')

URL=config.get('detail', 'testrailURL')
userEmail=config.get('detail', 'testrailEmailID')
userPassword=config.get('detail', 'testrailPassword')
projID = config.get('detail', 'projectID')
suiID= config.get('detail', 'suiteID')
print(userEmail)
print(userPassword)

client = APIClient(URL)
client.user = userEmail
client.password = userPassword


##print(client.send_get)
uri= 'get_cases/%s&suite_id=%s'% (projID ,suiID)
print (uri)
testcase = client.send_get(uri)
print(testcase)

with open('testcases.json', 'w') as fp:
    json.dump(testcase, fp)

jsonFile = open('testcases.json', 'r')
values = json.load(jsonFile)
for v in values:
    print v['id'],v ['title']


