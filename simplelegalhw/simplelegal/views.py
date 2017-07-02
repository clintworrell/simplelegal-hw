# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json, os, urllib2

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render

from simplelegal.models import Invoice

# Create your views here.
def get_invoice_api_data():
    auth_token_file = os.path.join(settings.PROJECT_ROOT, 'auth_token.txt')
    with open(auth_token_file) as f:
        AUTH_TOKEN = f.read().strip()

    url = 'https://falcon.simplelegal.com/api/v1/invoices/'
    request = urllib2.Request(url)
    request.add_header('Authorization', 'Token ' + AUTH_TOKEN)
    response = urllib2.urlopen(request)
    data = json.load(response)

    return data

def seed_invoice_model(request):
    data = get_invoice_api_data()
    invoices = data.get('results')

    for invoice in invoices:
        curr_invoice = Invoice()
        curr_invoice.simplelegal_id = invoice['id']
        curr_invoice.invoice_number = invoice['invoice_number']
        curr_invoice.invoice_date = invoice['invoice_date']
        curr_invoice.status = invoice['status']
        curr_invoice.received_date = invoice['received_date']
        curr_invoice.billing_start_date = invoice['billing_start_date']
        curr_invoice.billing_end_date = invoice['billing_end_date']
        curr_invoice.total = invoice['total']
        curr_invoice.net = invoice['net']
        curr_invoice.tax = invoice['tax']
        curr_invoice.currency = invoice['currency']
        curr_invoice.exchange_rate = invoice['exchange_rate']
        curr_invoice.native_currency = invoice['native_currency']
        curr_invoice.native_total = invoice['native_total']
        curr_invoice.native_net = invoice['native_net']
        curr_invoice.native_tax = invoice['native_tax']
        curr_invoice.approvers = invoice['approvers']
        curr_invoice.vendor = invoice['vendor']
        curr_invoice.vendor_id = invoice['vendor_id']
        curr_invoice.api_url = invoice['api_url']
        curr_invoice.url = invoice['url']
        curr_invoice.save()

    return HttpResponse("Invoice model seed complete...")
