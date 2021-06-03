from datetime import datetime

from . import models
from django.conf import settings


class PpdCsvRowConverter:
    def covertCsvRow(self, row):
        row_array = row.replace('"','').replace('\n','').split(sep=',')
        return models.PricePaidData(
            id=row_array[0].replace("{",'').replace("}",''),
            price=float(row_array[1]),
            date_of_transfer=datetime.strptime(row_array[2],settings.DATE_FORMAT),
            post_code=row_array[3],
            property_type=row_array[4],
            old_or_new=row_array[5],
            duration=row_array[6],
            paon=row_array[7],
            saon=row_array[8],
            street=row_array[9],
            locality=row_array[10],
            city=row_array[11],
            district=row_array[12],
            county=row_array[13],
            category=row_array[14],
            status=row_array[15],
        )