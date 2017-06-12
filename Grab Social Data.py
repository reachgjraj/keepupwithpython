#Grab that Social Data from www.Fullcontact.com using via their API using Python/Json
#Fullcontact has been signed up with raj.eden@gmail.com

#curl -H "X-FullContact-APIKey: 4510205cc605cc83" https://api.fullcontact.com/v2/person.json?email=raj.eden%40gmail.com


import urllib2
import json
# import pprint

# url = 'https://api.fullcontact.com/v2/person.json?apiKey=4510205cc605cc83&email=raj.eden%40gmail.com'
# urlData = urllib2.urlopen(url)
# loadedJson = json.load(urlData)
# # print loadedJson['organizations{startDate}']
# print loadedJson

def collectallcontact (email):
    api_key = '4510205cc605cc83'
    email = email
    fullurl = 'https://api.fullcontact.com/v2/person.json?apiKey='+ api_key +'&email=' + email
    loadUrl = urllib2.urlopen(fullurl)
    jsonData = json.load(loadUrl)

    print jsonData

    # org1 = jsonData['organizations']
    # print org1
    # #
    # pprint.pprint(jsonData,width=1)

    organizations = jsonData['organizations']

    # for item in organizations:
    #     print item['title']
    #
    # for key in jsonData:
    #     print key
    #
    # for value in jsonData:
    #     print value

    for item in jsonData['organizations']:
        print item


collectallcontact('raj.eden@gmail.com')

