from django.db import models


# Create your models here.
class PricePaidData(models.Model):
    transactionUniqueIdentifier = models.CharField()
    price = models.DecimalField()
    dateOfTransfer = models.DateTimeField()
    postCode = models.CharField()
    propertyType = models.CharField(max_length=1)
    oldOrNew = models.BooleanField()
    duration = models.CharField(max_length=1)
    paon = models.CharField()
    saon = models.CharField()
    street = models.CharField()
    locality = models.CharField()
    city = models.CharField()
    district = models.CharField()
    county = models.CharField()
    category = models.CharField(max_length=1)
    status = models.CharField(max_length=1)


class PagingDetails:
    pageNumber: int
    startRecord: int
    endRecord: int
    hasNextPage: bool
    hasPrevPage: bool

