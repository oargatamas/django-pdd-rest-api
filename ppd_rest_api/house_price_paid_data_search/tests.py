from django.test import TestCase
import mock
from rest_framework.test import RequestsClient

# Create your tests here.
from .repositories import FileSystemCachedCsvPpdRepository
from . import test_settings


def repositoryMock():
    return FileSystemCachedCsvPpdRepository(fileUrl=test_settings.LOCAL_CSV_FILE_URI)


class PpdApiTest(TestCase):
    def setUp(self):
        pass

    @mock.patch("house_price_paid_data_search.repositories.get_repository", side_effect=repositoryMock)
    def test_ppd_all_view_expect_all_record_with_paging(self):
        print(self.repository.fileUrl)

        self.assertTrue(True)
