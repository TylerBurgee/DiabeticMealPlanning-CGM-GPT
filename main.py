"""
Author: Tyler J. Burgee
Date: 11 July 2023
"""

# IMPORT MODULES
from data_handler import DataHandler
from data_processor import DataProcessor
from patient import Patient
from datetime import datetime, timedelta, time
from gpt_api import GPT_API

class Main:

    def __init__(self, api_key, org_id):
        self.api_key = api_key
        self.org_id = org_id
        self.gpt = GPT_API(api_key, org_id)

    def blood_glucose_increment_test(self, increment=5):
        """
        Slowly increments blood-glucose level to determine ChatGPT's thresholds
        for what it considers healthly/unhealthy/severe blood-glucose.
        """
        pass

    def instantaneous_blood_glucose_prompt(self, patient: object, meal_inquiry: str) -> str:
        """Sends an instantaneous CGM reading to ChatGPT and requests meal suggestions."""
        blood_glucose = 'Blood-glucose: {} mg/dL.\n'.format(patient.get_current_blood_glucose())
        last_meal = 'Last meal: {} hr ago.\n'.format(patient.get_hours_since_last_meal())
        query = 'Query: Is this safe? If so, recommend meals for {} (If blood-glucose is severely low or high, prioritize quickly raising or lowering blood-sugar levels,respectively, before eating a meal); if not, what should I do(prioritize seeking medical attention over remedies)?\n'.format(meal_inquiry)

        prompt = blood_glucose + last_meal + query

        if patient.get_dietary_restrictions() is not None:
            prompt += 'Dietary restrictions: {}.\n'.format(patient.get_dietary_restrictions())
        if patient.get_budget() is not None:
            prompt += 'Budget: ${}.\n'.format(str(patient.get_budget()))
        if patient.get_exercise() is not None:
            prompt += 'Exercise: {}.\n'.format(patient.get_exercise())
        if patient.get_medication() is not None:
            prompt += 'Medication: {}.\n'.format(patient.get_medication())

        response = self.gpt.send_prompt(prompt)

        return prompt

    def average_blood_glucose_test(self, patient: object):
        """Sends an average of CGM readings since last meal to ChatGPT and requests meal suggestions."""
        pass

if __name__ == '__main__':
    filename = 'test_db.csv'
    dh = DataHandler(filename)

    api_key = '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'
    org_id = 'org-cMRrZweyGUcQPXCwXcub7hc9'

    main = Main(api_key, org_id)

    last_meal_time = datetime.strptime('3:00 PM', '%I:%M %p')
    diabetic_patient = Patient(dh.get_data_by_patient(patient=0, profile=4), last_meal_time=last_meal_time, dietary_restrictions='vegan', budget='20')

    response = main.instantaneous_blood_glucose_prompt(diabetic_patient, 'dinner')
    print(response)
