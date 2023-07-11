"""
Author: Tyler J. Burgee
Date: 11 July 2023
"""

# IMPORT MODULES
from data_processor import DataProcessor as dp

class Patient:
    """Class to represent a Type I Diabetic patient using a CGM monitor"""

    def __init__(self, cgm_data: list, last_meal=0, budget=None, exercise=None, dietary_restrictions=None, medication=None) -> None:
        """Defines the constructor for a Patient object"""
        self.cgm_data = cgm_data

        self.dietary_restrictions = dietary_restrictions
        self.medication = medication

        self.last_meal = last_meal
        self.budget = budget
        self.exercise = exercise

    def set_last_meal(self, last_meal: float) -> None:
        """Sets how long ago a Patient object ate their last meal"""
        self.last_meal = last_meal

    def set_exercise(self, exercise: str) -> None:
        """Sets the exercise a Patient object is about to perform"""
        self.exercise = exercise

    def set_budget(self, budget: float) -> None:
        """Sets the budget for a Patient object's next meal"""
        self.budget = budget

    def get_instantaneous_blood_glucose(self, time: int) -> float:
        """Returns a Patient object's blood-glucose at a specified time"""
        time_increment = 5

        blood_glucose = dp.get_interval_avg(self.cgm_data, (time, time+time_increment), time_increment)

        return blood_glucose

    def get_last_meal(self) -> float:
        """Returns how long ago a Patient object ate their last meal"""
        return self.last_meal

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
