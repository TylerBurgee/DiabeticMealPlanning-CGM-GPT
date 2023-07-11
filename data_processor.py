class DataProcessor:

  def __init__(self):
    pass

  def get_interval_avg(self, data: list, interval: tuple) -> float:
    """Returns the avg blood-glucose level in a given time interval"""
    pass

if __name__ == '__main__':
  # IMPORT MODULE
  from data_handler import DataHandler

  filename = 'test_db.csv'
  dh = DataHandler(filename)

  # GET DATA FROM A SINGLE DAY
  data = dh.get_data_by_day(0, 1)

  dp = DataProcessor()

  interval_avg = dp.get_interval_avg(data, (0, 60))
  print(interval_avg)
