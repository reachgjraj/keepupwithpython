#!/usr/bin/env python
# local restaranturant contact details

import json
import urllib2

api_key ='9fb8cd70cb34cab8e83690473133f51943b5c93f'
locu_api ='9fb8cd70cb34cab8e83690473133f51943b5c93f'
#
# urls='https://api.locu.com/v1_0/venue/search/?&category=restaurant&api_key=9fb8cd70cb34cab8e83690473133f51943b5c93f'
#
# openurl = urllib2.urlopen(urls)
# loadjson = json.load(openurl)
#
# print loadjson

# for item in loadjson['objects']:
#     # print item
#     print item['name']
#     print item['website_url']
#     print item['locality']
#     print '****'


def locu_search(query):
    api_key = locu_api
    url_locu = 'https://api.locu.com/v1_0/venue/search/?api_key=' + api_key
    cat = query
    final_url = url_locu + "&category=" + cat
    print final_url
    json_obj = urllib2.urlopen(final_url)
    datajs = json.load(json_obj)

    print datajs

    for item in datajs['objects']:
        print item['name'],'*',item['locality'],'*', item['phone']

locu_search('restaurant')