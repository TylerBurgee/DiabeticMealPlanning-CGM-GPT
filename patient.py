"""
Author: Tyler J. Burgee
"""

# IMPORT MODULES
from data_processor import DataProcessor as dp
from datetime import datetime, timedelta, time

class Patient:
    """Class to represent a Type I Diabetic patient using a CGM monitor"""

    def __init__(self, cgm_data: list, last_meal_time: object, budget="", exercise="", dietary_restrictions="", medication="") -> None:
        """Defines the constructor for a Patient object"""
        self.cgm_data = cgm_data

        self.dietary_restrictions = dietary_restrictions
        self.medication = medication

        self.last_meal_time = last_meal_time
        self.budget = budget
        self.exercise = exercise

    def set_last_meal_time(self, last_meal: float) -> None:
        """Sets the time a Patient object ate their last meal"""
        self.last_meal_time = last_meal_time

    def set_exercise(self, exercise: str) -> None:
        """Sets the exercise a Patient object is about to perform"""
        self.exercise = exercise

    def set_budget(self, budget: float) -> None:
        """Sets the budget for a Patient object's next meal"""
        self.budget = budget

    def get_current_blood_glucose(self) -> float:
        """Returns a Patient object's blood-glucose at the current time"""
        current_time=datetime.now()
        # ROUND CURRENT TIME TO NEAREST 5 MINUTES
        rounded_current_time = (current_time + (datetime.min - current_time) % timedelta(minutes=5))
        # GET PREVIOUS CGM READING TIME
        last_reading_time = rounded_current_time - timedelta(minutes=5)

        # CONVERT TIME OBJECTS TO FORMATTED STRINGS
        rounded_current_time = datetime.strftime(rounded_current_time, "%I:%M %p")
        last_reading_time = datetime.strftime(last_reading_time, "%I:%M %p")

        # CREATE NEW TIME OBJECTS
        rounded_current_time = datetime.strptime(rounded_current_time, '%I:%M %p')
        last_reading_time = datetime.strptime(last_reading_time, "%I:%M %p")

        last_cgm_reading = dp.get_patient_interval_data(self.cgm_data, last_reading_time, rounded_current_time)[0]

        return last_cgm_reading

    def get_blood_glucose_at_time(self, time: object) -> float:
        """Returns a Patient object's blood-glucose at the specified time"""
        # ROUND CURRENT TIME TO NEAREST 5 MINUTES
        rounded_time = (time + (datetime.min - time) % timedelta(minutes=5))
        # GET PREVIOUS CGM READING TIME
        last_reading_time = rounded_time - timedelta(minutes=5)

        # CONVERT TIME OBJECTS TO FORMATTED STRINGS
        rounded_time = datetime.strftime(rounded_time, "%I:%M %p")
        last_reading_time = datetime.strftime(last_reading_time, "%I:%M %p")

        # CREATE NEW TIME OBJECTS
        rounded_time = datetime.strptime(rounded_time, '%I:%M %p')
        last_reading_time = datetime.strptime(last_reading_time, "%I:%M %p")

        cgm_reading = dp.get_patient_interval_data(self.cgm_data, last_reading_time, rounded_time)[0]

        return cgm_reading

    def get_avg_blood_glucose_last_meal(self):
        """
        Returns the average blood-glucose level from the time a Patient object
        ate their last meal, until now.
        """
        current_time=datetime.now()

        # ROUND CURRENT TIME TO NEAREST 5 MINUTES
        rounded_current_time = (current_time + (datetime.min - current_time) % timedelta(minutes=5))
        # GET LAST CGM READING TIME
        last_reading_time = rounded_current_time + timedelta(minutes=5)

        # CONVERT TIME OBJECT TO FORMATTED STRING
        last_reading_time = datetime.strftime(last_reading_time, "%I:%M %p")

        # CREATE NEW TIME OBJECT
        last_reading_time = datetime.strptime(last_reading_time, "%I:%M %p")

        avg = dp.get_interval_avg(self.cgm_data, self.get_last_meal_time(), last_reading_time)

        return avg

    def get_max_blood_glucose_last_meal(self):
        """
        Returns the maximum blood-glucose level from the time a Patient object
        ate their last meal, until now.
        """
        current_time=datetime.now()

        # ROUND CURRENT TIME TO NEAREST 5 MINUTES
        rounded_current_time = (current_time + (datetime.min - current_time) % timedelta(minutes=5))
        # GET LAST CGM READING TIME
        last_reading_time = rounded_current_time + timedelta(minutes=5)

        # CONVERT TIME OBJECT TO FORMATTED STRING
        last_reading_time = datetime.strftime(last_reading_time, "%I:%M %p")

        # CREATE NEW TIME OBJECT
        last_reading_time = datetime.strptime(last_reading_time, "%I:%M %p")

        max_reading = dp.get_patient_interval_data_max(self.cgm_data, self.get_last_meal_time(), last_reading_time)

        return max_reading

    def get_min_blood_glucose_last_meal(self):
        """
        Returns the minimum blood-glucose level from the time a Patient object
        ate their last meal, until now.
        """
        current_time=datetime.now()

        # ROUND CURRENT TIME TO NEAREST 5 MINUTES
        rounded_current_time = (current_time + (datetime.min - current_time) % timedelta(minutes=5))
        # GET LAST CGM READING TIME
        last_reading_time = rounded_current_time + timedelta(minutes=5)

        # CONVERT TIME OBJECT TO FORMATTED STRING
        last_reading_time = datetime.strftime(last_reading_time, "%I:%M %p")

        # CREATE NEW TIME OBJECT
        last_reading_time = datetime.strptime(last_reading_time, "%I:%M %p")

        min_reading = dp.get_patient_interval_data_min(self.cgm_data, self.get_last_meal_time(), last_reading_time)

        return min_reading

    def get_hours_since_last_meal(self, current_time=datetime.now()) -> float:
        """
        Returns number of hours between now and the time a Patient object
        ate their last meal.
        """
        # CONVERT TIME OBJECTS TO FORMATTED STRINGS
        current_time = datetime.strftime(current_time, "%I:%M %p")

        # CREATE NEW TIME OBJECTS
        current_time = datetime.strptime(current_time, '%I:%M %p')

        time_difference = current_time - self.get_last_meal_time()
        days, seconds = time_difference.days, time_difference.seconds
        minutes_since_last_meal = ((seconds % 3600) // 60) / 60
        hours_since_last_meal = (days * 24 + seconds // 3600) + minutes_since_last_meal

        return hours_since_last_meal

    def get_last_meal_time(self) -> object:
        """Returns the time a Patient object ate their last meal"""
        return self.last_meal_time

    def get_last_meal_time_str(self) -> str:
        """Returns the time a Patient object ate their last meal, in string format"""
        last_meal_time = datetime.strftime(self.last_meal_time, "%I:%M %p")

        return last_meal_time

    def get_exercise(self) -> str:
        """Returns the exercise a Patient object is performing"""
        return self.exercise

    def get_budget(self) -> float:
        """Returns the budget a Patient object has set for their next meal"""
        return self.budget

    def get_dietary_restrictions(self) -> str:
        """Returns the dietary restrictions of a Patient object"""
        return self.dietary_restrictions

    def get_bmi(self) -> float:
        """Returns the Body Mass Index (BMI) of a Patient object"""
        return self.bmi

    def get_medication(self) -> str:
        """Returns the medications being used by a Patient object"""
        return self.medication

    def get_cgm_data(self) -> list:
        """Returns the CGM data from a Patient object"""
        return self.cgm_data

if __name__ == '__main__':
    from data_handler import DataHandler
    filename = 'test_db.csv'
    dh = DataHandler(filename)

    patient_data = dh.get_data_by_patient(patient=0, profile=1)
    last_meal_time = datetime.strptime('10:00 AM', '%I:%M %p')

    patient = Patient(patient_data, last_meal_time)
    blood_glucose = patient.get_current_blood_glucose()
    print("Current blood-glucose:", blood_glucose)
    hours_since_last_meal = patient.get_hours_since_last_meal()
    print("Hours since last meal:", hours_since_last_meal)
