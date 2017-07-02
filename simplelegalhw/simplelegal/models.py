# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
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
