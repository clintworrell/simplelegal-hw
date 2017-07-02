# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

import json, os, urllib2

# Create your views here.
def get_invoice_api_data():
    with open('./auth_token.txt') as f:
        AUTH_TOKEN = f.read().strip()

    url = 'https://falcon.simplelegal.com/api/v1/invoices/'
    request = urllib2.Request(url)
    request.add_header('Authorization', 'Token ' + AUTH_TOKEN)
    response = urllib2.urlopen(request)
    data = json.load(response)

    print data

get_invoice_api_data()
