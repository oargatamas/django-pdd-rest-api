import io
from datetime import datetime

from django.conf import settings
from django.test import SimpleTestCase
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.test import RequestsClient

# Create your tests here.
from .converters import PpdCsvRowConverter
from .models import PricePaidData


class PpdApiTest(SimpleTestCase):
    def setUp(self):
        self.client = RequestsClient()

    def test_ppd_all_view_expect_all_record_with_paging(self, *args, **kwargs):
        response = self.client.get("http://testserver/ppd")
        response_body = response.json()

        print(settings.CSV_DATA_LOCATION)

        fixtures = open(settings.FIXTURE_DATA_LOCATION, "r").read()
        expectations = JSONParser().parse(io.BytesIO(bytes(fixtures, 'utf-8')))

        self.assertEqual(len(response_body["price_paid_data"]), len(expectations["price_paid_data"]))
        self.assertEqual(response_body, expectations)

    def test_ppd_valid_period_view_expect_all_record_within_period_with_paging(self, *args, **kwargs):
        response = self.client.get("http://testserver/ppd/from/2006-07-01T00:00:00/until/2006-07-30T23:59:00")
        response_body = response.json()

        print(settings.CSV_DATA_LOCATION)

        fixtures = open(settings.FIXTURE_FILTERED_DATA_LOCATION, "r").read()
        expectations = JSONParser().parse(io.BytesIO(bytes(fixtures, 'utf-8')))

        self.assertEqual(len(response_body["price_paid_data"]), len(expectations["price_paid_data"]))
        self.assertEqual(response_body, expectations)

    def test_ppd_not_existing_period_view_expect_empty_list(self, *args, **kwargs):
        response = self.client.get("http://testserver/ppd/from/2021-07-01T00:00:00/until/2021-07-30T23:59:00")
        response_body = response.json()

        self.assertEqual(len(response_body["price_paid_data"]), 0)

    def test_ppd_invalid_period_view_expect_bad_request(self, *args, **kwargs):
        response = self.client.get("http://testserver/ppd/from/2006-07-30T00:00:00/until/2006-07-01T23:59:00")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class PpdCsvConverterTest(SimpleTestCase):

    def setUp(self):
        self.csv_valid_row = '"{BEF7EBBE-9F40-7A76-E053-6B04A8C092F7}","201000","2006-07-28 00:00","WA16 6DQ","T","N","F","3","","CHURCH VIEW","","KNUTSFORD","CHESHIRE EAST","CHESHIRE EAST","A","A"'
        self.csv_invalid_date_row = '"{BEF7EBBE-9F40-7A76-E053-6B04A8C092F7}","201000","200607-28 0000","WA16 6DQ","T","N","F","3","","CHURCH VIEW","","KNUTSFORD","CHESHIRE EAST","CHESHIRE EAST","A","A"'
        self.csv_invalid_price_row = '"{BEF7EBBE-9F40-7A76-E053-6B04A8C092F7}","201sdfs000","2006-07-28 00:00","WA16 6DQ","T","N","F","3","","CHURCH VIEW","","KNUTSFORD","CHESHIRE EAST","CHESHIRE EAST","A","A"'
        self.csv_invalid_column_count_row = '"{BEF7EBBE-9F40-7A76-E053-6B04A8C092F7}","201sdfs000","2006-07-28 00:00"'
        self.valid_parsed_record = PricePaidData(
            id="BEF7EBBE-9F40-7A76-E053-6B04A8C092F7",
            price=201000,
            date_of_transfer=datetime.strptime("2006-07-28 00:00", settings.DATE_FORMAT),
            post_code="WA16 6DQ",
            property_type="T",
            old_or_new="N",
            duration="F",
            paon="3",
            saon="",
            street="CHURCH VIEW",
            locality="",
            city="KNUTSFORD",
            district="CHESHIRE EAST",
            county="CHESHIRE EAST",
            category="A",
            status="A",
        )

    def test_converter_with_valid_value_expect_valid_record(self):
        converter = PpdCsvRowConverter()

        result = converter.covertCsvRow(self.csv_valid_row)

        self.assertEqual(result, self.valid_parsed_record)

    def test_converter_with_invalid_date_value_expect_error(self):
        converter = PpdCsvRowConverter()
        with self.assertRaises(ValueError):
            converter.covertCsvRow(self.csv_invalid_date_row)

    def test_converter_with_invalid_price_value_expect_error(self):
        converter = PpdCsvRowConverter()
        with self.assertRaises(ValueError):
            converter.covertCsvRow(self.csv_invalid_price_row)

    def test_converter_with_short_record_value_expect_error(self):
        converter = PpdCsvRowConverter()
        with self.assertRaises(ValueError):
            converter.covertCsvRow(self.csv_invalid_column_count_row)
