class DataProcessor:

  def __init__(self):
    pass

  def get_interval_avg(self, data, interval):
    """Returns the avg blood-glucose level in a given time interval"""

if __name__ == '__main__':
  # IMPORT MODULE
  from data_handler import DataHandler

  filename = 'test_db.csv'
  dh = DataHandler(filename)

  # GET DATA FROM PROFILE 1
  data = dh.get_data_by_profile(1)

  dp = DataProcessor()

  interval_avg = dp.get_interval_avg(data)
  print(interval_avg)
