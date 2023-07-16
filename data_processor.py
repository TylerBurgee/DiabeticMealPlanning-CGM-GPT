"""
Author: Tyler J. Burgee, Vaageesha Das
Date: 11 July 2023
"""
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

class DataProcessor:
  """Class to process synthetic CGM data"""

  @staticmethod
  def get_interval_avg(data: list, interval: tuple, time_increment=5) -> float:
    """
    Returns the average blood-glucose level in a given time interval.
    Lower bound on the interval is inclusive, upper bound is exclusive. 
    Interval values should be multiples of the time_increment variable.

    data: a single day of CGM data in list format.
    interval: time interval over which the average is to be calculated.
    time_increment: time in between each CGM reading.
    """
    sum_of_readings = 0
    num_of_readings = (interval[1] - interval[0]) / time_increment

    for x in range(int(interval[0] / time_increment), int(interval[1] / time_increment)):
      sum_of_readings += float(data[x])

    avg = sum_of_readings / num_of_readings

    return avg

  def get_day_avg(data: list, time_increment=5) -> float:
    """Returns the average blood-glucose level in a given day"""
    interval = (0, 1440)

    avg = DataProcessor.get_interval_avg(data, interval, time_increment)

    return avg

  def draw_patient_graph_interval(patient_data, patient_profile, patient_id, start_time, end_time) -> None:
        """Draws a graph of the given patient's CGM readings over the day"""
        patient_data = [float(datum) for datum in patient_data]

        times_list = []
        current_time = start_time

        while current_time <= end_time:
            times_list.append(current_time.strftime('%I:%M %p'))
            current_time += timedelta(minutes=5)

        starting_index = int(start_time.hour * 12 + start_time.minute / 5)

        plt.bar(times_list, patient_data)
        plt.title('Patient Data Over Time')
        plt.xlabel('Time')
        plt.ylabel('Patient Data')
        plt.show()

  def draw_patient_graph_day(patient_data, patient_profile, patient_id):
     start_time = datetime.strptime('12:00 AM', '%I:%M %p')
     end_time = datetime.strptime('11:55 AM', '%I:%M %p')
     DataProcessor.draw_patient_graph_interval(patient_data, patient_profile, patient_id, start_time, end_time)

if __name__ == '__main__':
  # IMPORT MODULES
  from data_handler import DataHandler

  filename = 'test_db.csv'
  dh = DataHandler(filename)

  # GET DATA FROM A SINGLE PATIENT (ONE DAY)
  patient_data = dh.get_data_by_patient(patient=0, profile=1)

  interval_avg = DataProcessor.get_interval_avg(patient_data, (10, 20))
  print("Average blood-glucose from minutes 10-20:", interval_avg)

  day_avg = DataProcessor.get_day_avg(patient_data)
  print("Average blood-glucose for the day:", day_avg)

  # GRAPH PATIENT DATA
  DataProcessor.draw_patient_graph_day(patient_data, 0, 0)
