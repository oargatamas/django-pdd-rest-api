from adaptor.fields import CharField, DecimalField, DateField, BooleanField
from adaptor.model import CsvModel


# Create your models here.
class PricePaidData(CsvModel):
    transactionUniqueIdentifier = CharField()
    price = DecimalField()
    dateOfTransfer = DateField()
    postCode = CharField()
    propertyType = CharField(max_length=1)
    oldOrNew = BooleanField()
    duration = CharField(max_length=1)
    paon = CharField()
    saon = CharField()
    street = CharField()
    locality = CharField()
    city = CharField()
    district = CharField()
    county = CharField()
    category = CharField(max_length=1)
    status = CharField(max_length=1)

    class Meta:
        delimiter = ","


class PagingDetails:
    pageNumber: int
    startRecord: int
    endRecord: int
    hasNextPage: bool
    hasPrevPage: bool

