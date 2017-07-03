# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class InvoiceManager(models.Manager):
    def seed_invoices(self, data):
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

class Invoice(models.Model):
    simplelegal_id = models.CharField(max_length=200)
    invoice_number = models.IntegerField()
    invoice_date = models.DateField()
    status = models.CharField(max_length=200)
    received_date = models.DateField()
    billing_start_date = models.DateField()
    billing_end_date = models.DateField()
    total = models.DecimalField(max_digits=12, decimal_places=4)
    net = models.DecimalField(max_digits=12, decimal_places=4, null=True)
    tax = models.DecimalField(max_digits=12, decimal_places=4, null=True)
    currency = models.CharField(max_length=3)  # ISO 4217 codes are 3 letters
    exchange_rate = models.DecimalField(max_digits=12, decimal_places=4, null=True)
    native_currency = models.CharField(max_length=3, null=True)
    native_total = models.DecimalField(max_digits=12, decimal_places=4, null=True)
    native_net = models.DecimalField(max_digits=12, decimal_places=4, null=True)
    native_tax = models.DecimalField(max_digits=12, decimal_places=4, null=True)
    approvers = models.CharField(max_length=200)
    vendor = models.CharField(max_length=200)
    vendor_id = models.CharField(max_length=200)
    api_url = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    objects = InvoiceManager()

class LineItemManager(models.Manager):
    def seed_line_items(self, invoice_number, lines):
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




class LineItem(models.Model):
    line_item_number = models.IntegerField()
    invoice_number = models.IntegerField()
    description = models.CharField(max_length=200)
    law_firm_matter_id = models.CharField(max_length=200)
    client_id = models.IntegerField()
    line_item_type = models.CharField(max_length=200)
    units = models.DecimalField(max_digits=12, decimal_places=4)
    rate = models.DecimalField(max_digits=12, decimal_places=4)
    adjustment = models.DecimalField(max_digits=12, decimal_places=4)
    total = models.DecimalField(max_digits=12, decimal_places=4)
    date = models.DateTimeField()
    task_code = models.CharField(max_length=200, null=True)
    expense_code = models.CharField(max_length=200, null=True)
    activity_code = models.CharField(max_length=200, null=True)
    timekeeper_id = models.CharField(max_length=200, null=True)
    timekeeper = models.CharField(max_length=200, null=True)
    timekeeper_level = models.CharField(max_length=200, null=True)
    native_tax = models.DecimalField(max_digits=12, decimal_places=4)
    native_rate = models.DecimalField(max_digits=12, decimal_places=4)
    native_adjustment = models.DecimalField(max_digits=12, decimal_places=4)
    native_total = models.DecimalField(max_digits=12, decimal_places=4)
    objects = LineItemManager()
