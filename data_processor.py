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

  def draw_patient_graph_day(patient_data) -> None:
        """Draws a graph of the given patient's CGM readings over the day"""
        patient_data = [float(datum) for datum in patient_data]

        start_time = datetime.strptime('12:00 AM', '%I:%M %p')
        times_list = []
        current_time = start_time

        for i in range(len(patient_data)):
            times_list.append(current_time.strftime('%I:%M %p'))
            current_time += timedelta(minutes=5)

        plt.bar(times_list, patient_data)
        plt.title('Patient Data Over Time')
        plt.xlabel('Time')
        plt.ylabel('Patient Data')
        plt.show()

        # plt.xticks(time_list)
        # plt.yticks(patient_data)
        # git commit -m "updated draw_patient_graph_day, x is to be the time and y is to be the glucose level"
        # plt.grid()

        # plt.gca().margins(x=0)
        # plt.gcf().canvas.draw()
        # tl = plt.gca().get_xticklabels()
        # maxsize = max([t.get_window_extent().width for t in tl])
        # m = 0.2  # Inch margin
        # s = maxsize / plt.gcf().dpi * N + 2 * m
        # margin = m / plt.gcf().get_size_inches()[0]

        # plt.gcf().subplots_adjust(left=margin, right=1. - margin)
        # plt.gcf().set_size_inches(s, plt.gcf().get_size_inches()[1])

        # plt.xlabel('Time')
        # plt.ylabel('CGM Reading')
        # plt.title('CGM Readings over the Day')

        # plt.yticks(fontsize=8)

        # plt.tight_layout()
        # plt.show()



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
  DataProcessor.draw_patient_graph_day(patient_data)
