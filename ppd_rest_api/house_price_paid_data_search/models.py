# Create your models here.
from datetime import datetime

from django.db import models


class PricePaidData(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    price = models.DecimalField(max_digits=1000, decimal_places=2)
    date_of_transfer = models.DateTimeField()
    post_code = models.CharField(max_length=100)
    property_type = models.CharField(max_length=100)
    old_or_new = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)
    paon = models.CharField(max_length=100)
    saon = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    locality = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    county = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    status = models.CharField(max_length=100)


class PagingDetails(models.Model):
    page_number = models.IntegerField()
    start_record = models.IntegerField()
    end_record = models.IntegerField()
    next_page = models.CharField(max_length=250)
    prev_page = models.CharField(max_length=250)
