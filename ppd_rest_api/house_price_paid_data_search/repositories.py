import os
from abc import abstractmethod, ABC
from datetime import datetime
from typing import IO

import requests

from . import converters
from ppd_rest_api import settings


def get_repository():
    return RealTimeLatestCsvPpdRepository()

class CsvPpdRepository(ABC):

    def find_record_by_id(self, transaction_id):
        filter = lambda row: row[0] == '{' + transaction_id + '}'

        return self.__get_records(filter, 0, 1)

    def find_all_records(self, offset, limit):
        filter = lambda row: True
        return self.__get_records(filter, offset, limit)

    def find_all_records_between(self, from_period, until_period, offset, limit):
        filter = lambda row: datetime.strptime(row[2],settings.DATE_FORMAT) >= from_period and datetime.strptime(row[2],settings.DATE_FORMAT)  <= until_period
        return self.__get_records(filter, offset, limit)

    def __get_records(self, filter, offset, limit):
        records = []
        converter = converters.PpdCsvRowConverter()

        with self.get_csv_data() as file :
            i = 0
            matches = 0
            while matches < limit :
                line = file.readline()
                if not line:
                    break

                if i >= offset and filter(line.replace('"','').split(sep=',')):
                    records.append(converter.covertCsvRow(line))
                    matches += 1
                i += 1

        self.cleanup()

        return records

    @abstractmethod
    def get_csv_data(self) -> IO:
        pass

    def cleanup(self):
        pass


class FileSystemCachedCsvPpdRepository(CsvPpdRepository):

    def get_csv_data(self) -> IO:
        return open(settings.LOCAL_CSV_FILE_URI,"r")


class RealTimeLatestCsvPpdRepository(CsvPpdRepository):
    def get_csv_data(self) -> IO:
        response = requests.get(settings.LATEST_CSV_URL)
        self.temp_file_path = "latest_ppd_cache.csv"
        file = open(self.temp_file_path, 'w+')
        file.write(response.text)
        file.seek(0)
        return file

    def cleanup(self):
        pass
