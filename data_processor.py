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
  

  def draw_patient_graph_interval(patient_id, patient_profile, start_time, end_time) -> None:
      """Draws a graph of the given patient's CGM readings over the day"""
      patient_data = dh.get_data_by_patient(patient_id, patient_profile)
      patient_data = [float(datum) for datum in patient_data]

      times_list = []
      current_time = datetime.strptime('12:00 AM', '%I:%M %p')
      counter = 0

      while current_time <= start_time:
        current_time += timedelta(minutes=5)
        counter += 1

      current_time = start_time

      while current_time <= end_time:
          times_list.append(current_time.strftime('%I:%M %p'))
          current_time += timedelta(minutes=5)

      patient_interval_data = []

      for i in range(len(times_list)):
          patient_interval_data.append(patient_data[counter+i])

      plt.figure(figsize=(12, 4))
      plt.plot(times_list, patient_interval_data)
      plt.title('Patient Data Over Time')
      plt.xlabel('Time')
      plt.ylabel('Patient Data')
      
      #this is to make sure that the x ticks are visible just at every hour
      x_ticks = plt.gca().xaxis.get_major_ticks()
      for i, tick in enumerate(x_ticks):
          if i % 12 != 0:
              tick.set_visible(False)

      #this is to make sure that right where the graph starts and ends is where the x ticks start and end
      plt.xlim(times_list[0], times_list[-1])

      plt.show()

  def draw_patient_graph_day(patient_id, patient_profile):
     start_time = datetime.strptime('12:00 AM', '%I:%M %p')
     end_time = datetime.strptime('11:55 AM', '%I:%M %p')
     DataProcessor.draw_patient_graph_interval(patient_id, patient_profile, start_time, end_time)

  # def draw_patient_graph_interval(data: list, interval: tuple, time_increment=5, tick_factor=6) -> None:
  #   """
  #   Draws a graph of the given patient's CGM readings
  #   over a given time interval.
  #   """
  #   data = [float(datum) for datum in data]

  #   start_time = datetime.strptime('12:00pm', '%I:%M%p')
  #   times_list = []
  #   current_time = start_time

  #   for i in range(len(data)):
  #       times_list.append(current_time.strftime('%I:%M\n%p'))
  #       current_time += timedelta(minutes=time_increment)

  #   start_time = int(interval[0] / time_increment)
  #   end_time = int(interval[1] / time_increment)

  #   data = data[start_time:end_time]
  #   times_list = times_list[start_time:end_time]

  #   # GRAPH SETUP
  #   plt.plot(times_list, data)
  #   plt.title('Patient Data Over Time')
  #   plt.xlabel('Time')
  #   plt.ylabel('Patient Data')
  #   plt.xticks([time for x,time in enumerate(times_list) if x%tick_factor==0])
  #   plt.margins(x=0)
  #   plt.show()

  # def draw_patient_graph_day(data: list) -> None:
  #   """Draws a graph of the given patient's CGM readings over the day"""
  #   interval = (0, 1440)
  #   DataProcessor.draw_patient_graph_interval(data, interval, tick_factor=12)


if __name__ == '__main__':
  # IMPORT MODULES
  from data_handler import DataHandler

  filename = 'test_db.csv'
  dh = DataHandler(filename)

  # GET DATA FROM A SINGLE PATIENT (ONE DAY)
  patient_data = dh.get_data_by_patient(patient=0, profile=2)

  interval_avg = DataProcessor.get_interval_avg(patient_data, (10, 20))
  print("Average blood-glucose from minutes 10-20:", interval_avg)

  day_avg = DataProcessor.get_day_avg(patient_data)
  print("Average blood-glucose for the day:", day_avg)

  # GRAPH PATIENT DATA
  DataProcessor.draw_patient_graph_day(0, 1)
  DataProcessor.draw_patient_graph_interval(0, 1, datetime.strptime('3:00 PM', '%I:%M %p'), datetime.strptime('5:00 PM', '%I:%M %p'))
