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
  

  def draw_patient_graph_interval(patient_data: list, start_time: object, end_time: object) -> None:
    """Draws a graph of the given patient's CGM readings over a specified time interval"""
    patient_data = [float(datum) for datum in patient_data]
    current_time = datetime.strptime('12:00 AM', '%I:%M %p')
    times_list = []
    counter = 0

    # STORES THE NUMBER OF INCREMENTS BETWEEN current_time AND start_time
    while current_time <= start_time:
      current_time += timedelta(minutes=5)
      counter += 1

    current_time = start_time

    # CREATES A LIST OF DISCRETE TIMES IN BETWEEN THE TIME INTERVAL
    while current_time <= end_time:
      times_list.append(current_time.strftime('%I:%M %p'))
      current_time += timedelta(minutes=5)

    patient_interval_data = []

    for i in range(len(times_list)):
      patient_interval_data.append(patient_data[counter+i])

    # GRAPH SETUP
    plt.figure(figsize=(12, 4))
    plt.plot(times_list, patient_interval_data)
    plt.title('Patient Data Over Time')
    plt.xlabel('Time')
    plt.ylabel('Patient Data')

    # MAKE X-TICKS VISILE AT EVERY HOUR
    plt.xticks([time for x,time in enumerate(times_list) if x%12==0])

    # REMOVES MARGINS ON X-AXIS
    plt.xlim(times_list[0], times_list[-1])

    plt.show()

  def draw_patient_graph_day(patient_data: list) -> None:
    """Draws a graph of the given patient's CGM readings over an entire day"""
    start_time = datetime.strptime('12:00 AM', '%I:%M %p')
    end_time = datetime.strptime('11:55 AM', '%I:%M %p')
    DataProcessor.draw_patient_graph_interval(patient_data, start_time, end_time)

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

  # GRAPH PATIENT DATA OVER AN ENTIRE DAY
  DataProcessor.draw_patient_graph_day(patient_data)

  # GRAPH PATIENT DATA OVER THE TIME INTERVAL FROM 3:00 PM to 5:00 PM
  start_time = datetime.strptime('3:00 PM', '%I:%M %p')
  end_time = datetime.strptime('5:00 PM', '%I:%M %p')
  DataProcessor.draw_patient_graph_interval(patient_data, start_time, end_time)
  
