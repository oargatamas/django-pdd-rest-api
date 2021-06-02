from abc import abstractmethod


class CsvPpdRepository:

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

        return records

    @abstractmethod
    def __get_csv_data(self):
        pass

    def __cleanup(self):
        pass
