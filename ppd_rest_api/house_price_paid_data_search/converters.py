from ppd_rest_api.house_price_paid_data_search.models import PricePaidData


class PpdCsvRowConverter:
    def covertCsvRow(self, row):
        return PricePaidData(

        )