# Create your models here.
from datetime import datetime

from django.db import models


class PricePaidData(models.Model):
    id = models.CharField(),
    price = models.DecimalField(),
    date_of_transfer = models.DateTimeField(),
    post_code = models.CharField(),
    property_type = models.CharField(),
    old_or_new = models.CharField(),
    duration = models.CharField(),
    paon = models.CharField(),
    saon = models.CharField(),
    street = models.CharField(),
    locality = models.CharField(),
    city = models.CharField(),
    district = models.CharField(),
    county = models.CharField(),
    category = models.CharField(),
    status = models.CharField(),


class PagingDetails(models.Model):
    page_number = models.IntegerField()
    start_record = models.IntegerField()
    end_record = models.IntegerField()
    has_next_page = models.BooleanField()
    has_prev_page = models.BooleanField()
