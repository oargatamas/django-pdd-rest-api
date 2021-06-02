from time import strptime

from ppd_rest_api.house_price_paid_data_search.models import PricePaidData


class PpdCsvRowConverter:
    def covertCsvRow(self, row):
        return PricePaidData(
            transaction_unique_identifier=row[0],
            price=float(row[1]),
            date_of_transfer=strptime(row[2],"%y-%m-%d %H:%M"),
            post_code=row[3],
            property_type=row[4],
            old_or_new=row[5],
            duration=row[6],
            paon=row[7],
            saon=row[9],
            street=row[10],
            locality=row[11],
            city=row[12],
            district=row[13],
            county=row[14],
            category=row[15],
            status=row[16],
        )