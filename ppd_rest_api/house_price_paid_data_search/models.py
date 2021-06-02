

# Create your models here.
from datetime import datetime


class PricePaidData():
    transactionUniqueIdentifier: str
    price: float
    dateOfTransfer: datetime
    postCode: str
    propertyType: str
    oldOrNew: bool
    duration: str
    paon: str
    saon: str
    street: str
    locality: str
    city: str
    district: str
    county: str
    category: str
    status: str


class PagingDetails:
    pageNumber: int
    startRecord: int
    endRecord: int
    hasNextPage: bool
    hasPrevPage: bool

