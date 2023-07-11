"""
Author: Tyler J. Burgee
Date: 11 July 2023
"""

class DataProcessor:
  """Class to process synthetic CGM data"""

  @staticmethod
  def get_interval_avg(data: list, interval: tuple) -> float:
    """
    Returns the average blood-glucose level in a given time interval.
    Lower bound on the interval is inclusive, upper bound is exclusive. 
    Interval values should be multiples of the time_increment variable.
    """
    time_increment = 5 # TIME BETWEEN EACH CGM READING
    sum_of_readings = 0
    num_of_readings = (interval[1] - interval[0]) / time_increment

    for x in range(int(interval[0] / time_increment), int(interval[1] / time_increment)):
      sum_of_readings += float(data[x])

    avg = sum_of_readings / num_of_readings

    return avg

if __name__ == '__main__':
  # IMPORT MODULES
  from data_handler import DataHandler

  filename = 'test_db.csv'
  dh = DataHandler(filename)

  # GET DATA FROM A SINGLE DAY
  data = dh.get_data_by_day(0, 1)

  interval_avg = DataProcessor.get_interval_avg(data, (10, 20))
  print(interval_avg)
