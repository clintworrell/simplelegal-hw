# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json, os, urllib2

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render

from simplelegal.models import Invoice, LineItem

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

def invoices(request):
    invoices = Invoice.objects.all()
    context = {'invoices': invoices}

    return render(request, 'simplelegal/invoices.html', context)

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

def seed_lineitem_model(request):
    auth_token_file = os.path.join(settings.PROJECT_ROOT, 'auth_token.txt')
    with open(auth_token_file) as f:
        AUTH_TOKEN = f.read().strip()

    invoice_urls = Invoice.objects.values_list('api_url', flat=True)
    for url in invoice_urls:
        request = urllib2.Request(url)
        request.add_header('Authorization', 'Token ' + AUTH_TOKEN)
        response = urllib2.urlopen(request)
        data = json.load(response)

        invoice_number = data['invoice_number']
        lines = data['lines']
        for line in lines:
            current_line = LineItem()
            current_line.line_item_number = line['line_item_number']
            current_line.invoice_number = invoice_number
            current_line.description = line['description']
            current_line.law_firm_matter_id = line['law_firm_matter_id']
            current_line.client_id = line['client_id']
            current_line.line_item_type = line['line_item_type']
            current_line.units = line['units']
            current_line.rate = line['rate']
            current_line.adjustment = line['adjustment']
            current_line.total = line['total']
            current_line.date = line['date']
            current_line.task_code = line['task_code']
            current_line.expense_code = line['expense_code']
            current_line.activity_code = line['activity_code']
            current_line.timekeeper_id = line['timekeeper_id']
            current_line.timekeeper = line['timekeeper']
            current_line.timekeeper_level = line['timekeeper_level']
            current_line.native_tax = line['native_tax']
            current_line.native_rate = line['native_rate']
            current_line.native_adjustment = line['native_adjustment']
            current_line.native_total = line['native_total']
            current_line.save()

    return HttpResponse("LineItem model seed complete...")
