

# Create your models here.
from django.db import models


class PricePaidData(models.Model):
    transactionUniqueIdentifier = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=100)
    dateOfTransfer = models.DateField()
    postCode = models.CharField(max_length=100)
    propertyType = models.CharField(max_length=1)
    oldOrNew = models.BooleanField()
    duration = models.CharField(max_length=1)
    paon = models.CharField(max_length=100)
    saon = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    locality = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    county = models.CharField(max_length=100)
    category = models.CharField(max_length=1)
    status = models.CharField(max_length=1)


class PagingDetails:
    pageNumber: int
    startRecord: int
    endRecord: int
    hasNextPage: bool
    hasPrevPage: bool

