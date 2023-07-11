"""
Author: Tyler J. Burgee
Date: 27 June 2023
"""

# IMPORT MODULES
import csv

class DataHandler:
    """Class for loading and retreiving data from a DB containing CGM readings"""

    def __init__(self, filename: str) -> None:
        """Defines the constructor for a DataHandler object"""
        self.filename = filename
        self.file = self._read_file_(self.filename)
        self.data = self._format_file_data_(self.file)

    def _read_file_(self, filename: str) -> list:
        """Loads data from database"""
        file = None

        try:
            with open(filename, 'r') as file:
                file = csv.reader(file)
                file = list(file)
        except FileNotFoundError:
            print("File: \'{}\' could not be located.")

        return file

    def _format_file_data_(self, file: list) -> dict:
        """Formats data from database into profile groups"""
        data = dict()
        keys = []

        for line in file:
            if line[0] not in keys:
                keys.append(line[0])
                day_data = [datum for x,datum in enumerate(line) if x > 0]
                data[line[0]] = [day_data]
            else:
                data[line[0]].append(day_data)

        return data

    def get_data_by_profile(self, profile: int) -> list:
        """
        Returns all data from a given profile, separated by day.
        Available profiles based on HbA1c levels:
            - 1 (below 6.5%)
            - 2 (between 6.5% to <7%)
            - 3 (between 7% to <8%)
            - 4 (above 8%)
        """
        data = self.data[str(profile)]
        return data

    def get_data_by_patient(self, patient: int, profile: int) -> list:
        """
        Returns data from a given profile for a specified patient.
        Note: the first patient is 0.
        """
        all_data = self.get_data_by_profile(profile)
        day_data = all_data[patient]
        return day_data

if __name__ == '__main__':
    # INSTANTIATE DataHandler OBJECT
    dh = DataHandler('test_db.csv')

    # GET DATA FROM PROFILE 1
    profile1 = dh.get_data_by_profile(1)

    for x,patient in enumerate(profile1):
        print('Profile 1, Patient #{}:'.format(x), patient)
