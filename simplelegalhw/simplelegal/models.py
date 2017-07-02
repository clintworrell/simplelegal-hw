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
