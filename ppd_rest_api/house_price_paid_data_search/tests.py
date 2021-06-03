import io

from django.conf import settings
from django.test import SimpleTestCase
import mock
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.test import RequestsClient

# Create your tests here.
from .models import PagingPricePaidData
from .repositories import FileSystemCachedCsvPpdRepository, get_repository

from .serializers import PagingPricePaidDataSerializer


class PpdApiTest(SimpleTestCase):
    def setUp(self):
        self.client = RequestsClient()

    def test_ppd_all_view_expect_all_record_with_paging(self, *args, **kwargs):
        response = self.client.get("http://testserver/ppd")
        response_body = response.json()

        print(settings.CSV_DATA_LOCATION)

        fixtures = open(settings.FIXTURE_DATA_LOCATION,"r").read()
        expectations = JSONParser().parse(io.BytesIO(bytes(fixtures,'utf-8')))

        self.assertEqual(len(response_body["price_paid_data"]),len(expectations["price_paid_data"]) )
        self.assertEqual(response_body,expectations)

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

        self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST)


