"""
Author: Tyler J. Burgee
Date: 11 July 2023
"""

# IMPORT MODULES
from data_handler import DataHandler
from data_processor import DataProcessor
from patient import Patient
from datetime import datetime, timedelta, time

class Main:

    def _create_prompt_(patient: object) -> str:
        blood_glucose = 'Blood-glucose: {} mg/dL.\n'.format(patient.get_current_blood_glucose())
        last_meal = 'Last meal: {} hr ago.\n'.format(patient.get_hours_since_last_meal())
        query = 'Query: Is this safe? If so, recommend meals for breakfast (If blood-glucose is severely low or high, prioritize quickly raising or lowering blood-sugar levels,respectively, before eating a meal); if not, what should I do(prioritize seeking medical attention over remedies)?\n'

        prompt = blood_glucose + last_meal + query

        if patient.get_dietary_restrictions() is not None:
            prompt += 'Dietary restrictions: {}.\n'.format(patient.get_dietary_restrictions())
        if patient.get_budget() is not None:
            prompt += 'Budget: ${}.\n'.format(str(patient.get_budget()))
        if patient.get_exercise() is not None:
            prompt += 'Exercise: {}.\n'.format(patient.get_exercise())
        if patient.get_medication() is not None:
            prompt += 'Medication: {}.\n'.format(patient.get_medication())

        return prompt

    def blood_glucose_increment_test(increment=5):
        """
        Slowly increments blood-glucose level to determine ChatGPT's thresholds
        for what it considers healthly/unhealthy/severe blood-glucose.
        """
        pass

    def instantaneous_blood_glucose_test(patient: object):
        """Sends an instantaneous CGM reading to ChatGPT and requests meal suggestions."""
        patient_data = patient.get_data()
        last_meal_time = patient.get_last_meal_time()

        prompt = Main._create_prompt_(patient)

    def average_blood_glucose_test(patient: object):
        """Sends an average of CGM readings since last meal to ChatGPT and requests meal suggestions."""
        pass

if __name__ == '__main__':
    filename = 'test_db.csv'
    dh = DataHandler(filename)

    last_meal_time = datetime.strptime('3:00 PM', '%I:%M %p')
    diabetic_patient = Patient(dh.get_data_by_patient(patient=0, profile=4), last_meal_time=last_meal_time, dietary_restrictions='vegan', budget='20')

    prompt = Main._create_prompt_(diabetic_patient)
    print(prompt)

    api_key = ''
    org_id = ''
    gpt = GPT_API(api_key, org_id)
    response = gpt.send_prompt(prompt)
    print(response)
