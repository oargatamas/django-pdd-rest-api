

# Create your models here.
from datetime import datetime

class PricePaidData():
    def __init__(self, transaction_unique_identifier, price, date_of_transfer, post_code, property_type, old_or_new, duration, paon, saon, street, locality, city, district, county, category, status):
        self.transaction_unique_identifier = transaction_unique_identifier,
        self.price = price,
        self.date_of_transfer = date_of_transfer,
        self.post_code = post_code,
        self.property_type = property_type,
        self.old_or_new = old_or_new,
        self.duration = duration,
        self.paon = paon,
        self.saon = saon,
        self.street = street,
        self.locality = locality,
        self.city = city,
        self.district = district,
        self.county = county,
        self.category = category,
        self.status = status,


class PagingDetails:
    def __init__(self, page_number, start_record, end_record, has_next_page, has_prev_page):
        self.page_number = page_number
        self.start_record = start_record
        self.end_record = end_record
        self.has_next_page = has_next_page
        self.has_prev_page = has_prev_page

