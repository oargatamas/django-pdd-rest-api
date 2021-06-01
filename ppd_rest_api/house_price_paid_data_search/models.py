from django.db import models


# Create your models here.
class PricePaidData(models.Model):
    transactionUniqueIdentifier = models.CharField()
    price = models.DecimalField()
    dateOfTransfer = models.DateTimeField()
    postCode = models.CharField()
    propertyType = models.CharField()
    oldOrNew = models.BooleanField()
    duration = models.CharField()
    paon = models.CharField()
    saon = models.CharField()
    street = models.CharField()
    locality = models.CharField()
    city = models.CharField()
    district = models.CharField()
    county = models.CharField()
    category = models.CharField()
    status = models.CharField()


class PagingDetails:
    pageNumber = 0
    startRecord = 0
    endRecord = 0
    hasNextPage = False
    hasPrevPage = False

