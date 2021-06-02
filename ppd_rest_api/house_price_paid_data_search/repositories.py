from abc import abstractmethod, ABC
from typing import IO
from ppd_rest_api.house_price_paid_data_search.converters import PpdCsvRowConverter
from ppd_rest_api.ppd_rest_api import settings


class CsvPpdRepository(ABC):

    def find_record_by_id(self, transaction_id):
        filter = lambda row: row[0] == transaction_id
        return self.__get_records(filter, 0, 1)

    def find_all_records(self, offset, limit):
        filter = lambda row: True
        return self.__get_records(filter, offset, limit)

    def find_all_records_between(self, from_period, until_period, offset, limit):
        filter = lambda row: row[2] >= from_period and row[2] <= until_period
        return self.__get_records(filter, offset, limit)

    def __get_records(self, filter, offset, limit):
        records = []
        converter = PpdCsvRowConverter()

        with self.__get_csv_data() as file :
            i = 0
            matches = 0
            while matches < limit:
                line = file.readline()

                if not line:
                    break

                if i >= offset and filter(line):
                    records.append(converter.covertCsvRow(line))
                i += 1

            file.close()

        return records

    @abstractmethod
    def __get_csv_data(self) -> IO:
        pass


class FileSystemCachedCsvPpdRepository(CsvPpdRepository):

    def __get_csv_data(self) -> IO:
        return open(settings.LOCAL_CSV_FILE_URI,"r")