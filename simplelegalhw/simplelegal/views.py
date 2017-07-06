# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json, os, urllib2

from django.db.models import Q, Sum
from django.http import HttpResponse
from django.shortcuts import render

from simplelegal.models import Invoice, LineItem
from utils import get_invoice_api_data

def filter_invoices(request, search_term):
    invoices = Invoice.objects.filter(Q(vendor__icontains=search_term)
                                    | Q(invoice_number__icontains=search_term)
                                    | Q(invoice_date__icontains=search_term)
                                    | Q(status__icontains=search_term)
                                    | Q(total__icontains=search_term))
    filtered_sum = invoices.aggregate(Sum('total'))
    filtered_sum = filtered_sum['total__sum']
    context = {'invoices': invoices, 'total_sum': filtered_sum}

    return render(request, 'simplelegal/invoice_table.html', context)

def invoices(request):
    invoices = Invoice.objects.all()
    total_sum = invoices.aggregate(Sum('total'))
    total_sum = total_sum['total__sum']
    context = {'invoices': invoices, 'total_sum': total_sum}

    return render(request, 'simplelegal/invoices.html', context)

def line_items(request, invoice_number):
    line_items = LineItem.objects.filter(invoice_number=invoice_number)
    context = {'line_items': line_items}

    return render(request, 'simplelegal/line_items.html', context)

def seed_invoice_model(request):
    data = get_invoice_api_data()
    Invoice.objects.seed_invoices(data)

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
        LineItem.objects.seed_line_items(invoice_number, lines)

    return HttpResponse("LineItem model seed complete...")
