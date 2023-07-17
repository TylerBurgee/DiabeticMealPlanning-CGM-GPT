"""
Authors: Tyler J. Burgee, Vaageesha Das
"""

import matplotlib.pyplot as plt
from datetime import datetime, timedelta

class DataProcessor:
  """Class to process synthetic CGM data"""

  @staticmethod
  def _get_start_count_(start_time: object) -> int:
    """Returns the number of increments between current_time and start_time"""
    current_time = datetime.strptime('12:00 PM', '%I:%M %p')
    counter = 0

    while current_time < start_time:
      current_time += timedelta(minutes=5)
      counter += 1

    return counter

  @staticmethod
  def _get_times_list_(start_time: object, end_time: object) -> list:
    """Returns a list of discrete times in between the given time interval"""
    current_time = start_time
    times_list = []

    while current_time.time() != end_time.time():
      times_list.append(current_time.strftime('%I:%M\n%p'))
      current_time += timedelta(minutes=5)

    return times_list

  @staticmethod
  def get_interval_avg(patient_data: list, start_time: object, end_time: object) -> float:
    """Returns the average blood-glucose level over a given time interval"""
    patient_data = [float(datum) for datum in patient_data]
    counter = DataProcessor._get_start_count_(start_time)
    times_list = DataProcessor._get_times_list_(start_time, end_time)
    num_of_readings = len(times_list)
    sum_of_readings = 0

    for i in range(len(times_list)):
      sum_of_readings += patient_data[counter+i]

    avg = sum_of_readings / num_of_readings

    return avg

  @staticmethod
  def get_day_avg(patient_data: list) -> float:
    """Returns the average blood-glucose level in a given day"""
    start_time = datetime.strptime('12:00 PM', '%I:%M %p')
    end_time = datetime.strptime('11:55 AM', '%I:%M %p')

    avg = DataProcessor.get_interval_avg(patient_data, start_time, end_time)

    return avg

  def _get_patient_interval_data_(patient_data: list, start_time: object, end_time: object) -> list:
    patient_data = [float(datum) for datum in patient_data]
    times_list = DataProcessor._get_times_list_(start_time, end_time)
    counter = DataProcessor._get_start_count_(start_time)
    patient_interval_data = []

    for i in range(len(times_list)):
      patient_interval_data.append(patient_data[counter+i])

    return patient_interval_data

  @staticmethod
  def draw_patient_graph_interval(patients_data: list, start_time: object, end_time: object, tick_factor=12) -> None:
    """Draws a graph of the given patient's CGM readings over a specified time interval"""
    times_list = DataProcessor._get_times_list_(start_time, end_time)
    patients_interval_data = []

    for patient_data in patients_data:
      patients_interval_data.append(DataProcessor._get_patient_interval_data_(patient_data, start_time, end_time))

    # GRAPH SETUP
    plt.figure(figsize=(12, 4))
    for patient_interval_data in patients_interval_data:
      plt.plot(times_list, patient_interval_data)
    plt.title('Patient Data Over Time')
    plt.xlabel('Time')
    plt.ylabel('Patient Data')

    # MAKE X-TICKS VISILE AT EVERY HOUR
    plt.xticks([time for x,time in enumerate(times_list) if x%tick_factor==0])

    # REMOVES MARGINS ON X-AXIS
    plt.xlim(times_list[0], times_list[-1])

    plt.show()

  @staticmethod
  def draw_patient_graph_day(patient_data: list) -> None:
    """Draws a graph of the given patient's CGM readings over an entire day"""
    start_time = datetime.strptime('12:00 PM', '%I:%M %p')
    end_time = datetime.strptime('11:55 AM', '%I:%M %p')
    DataProcessor.draw_patient_graph_interval(patient_data, start_time, end_time)

if __name__ == '__main__':
  # IMPORT MODULES
  from data_handler import DataHandler

  filename = 'test_db.csv'
  dh = DataHandler(filename)

  # GET DATA FROM A SINGLE PATIENT (ONE DAY)
  patient_data1 = dh.get_data_by_patient(patient=0, profile=1)
  patient_data2 = dh.get_data_by_patient(patient=0, profile=2)
  patient_data3 = dh.get_data_by_patient(patient=0, profile=3)
  patient_data4 = dh.get_data_by_patient(patient=0, profile=4)

  patients_data = [patient_data1, patient_data2, patient_data3, patient_data4]

  # CREATE START AND END TIME OBJECTS
  start_time = datetime.strptime('3:00 PM', '%I:%M %p')
  end_time = datetime.strptime('5:00 PM', '%I:%M %p')

  # GET THE AVERAGE BLOOD-GLUCOSE LEVEL FROM 3:00 PM to 5:00 PM
  interval_avg = DataProcessor.get_interval_avg(patient_data1, start_time, end_time)
  print("Average blood-glucose from 3:00 PM to 5:00 PM:", interval_avg)

  # GET THE AVERAGE BLOOD-GLUCOSE LEVEL OVER AN ENTIRE DAY
  day_avg = DataProcessor.get_day_avg(patient_data1)
  print("Average blood-glucose for the day:", day_avg)

  # GRAPH PATIENT DATA OVER AN ENTIRE DAY
  DataProcessor.draw_patient_graph_day(patients_data)

  # GRAPH PATIENT DATA OVER THE TIME INTERVAL FROM 3:00 PM to 5:00 PM
  DataProcessor.draw_patient_graph_interval(patients_data, start_time, end_time)
