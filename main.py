"""
Author: Tyler J. Burgee
Date: 11 July 2023
"""

# IMPORT MODULES
from data_handler import DataHandler
from patient import Patient
from datetime import datetime, timedelta, time
from gpt_api import GPT_API

class Main:

    def __init__(self, api_key: str, org_id: str) -> None:
        """Defines the constructor for a Main object"""
        self.api_key = api_key
        self.org_id = org_id
        self.gpt = GPT_API(self.api_key, self.org_id)

    def blood_glucose_increment_test(self):
        """
        Slowly increments blood-glucose level to determine ChatGPT's thresholds
        for what it considers healthly/unhealthy/severe blood-glucose.
        """
        log = []

        for x in range(21):
            if x % 10 == 0:
                prompt = "My fasting blood-glucose level is {} mg/dL.".format(x)
                response = self.gpt.send_prompt(prompt)
                log.append(("Prompt:", prompt, "Response:", response))

        return log

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

        return response

    def average_blood_glucose_prompt(self, patient: object) -> str:
        """Sends an average of CGM readings since last meal to ChatGPT and requests meal suggestions."""
        pass

if __name__ == '__main__':
    # PATIENT CGM DATA FILE
    filename = 'test_db.csv'

    # INSTANTIATE DataHandler OBJECT
    dh = DataHandler(filename)

    # GPT API ACCOUNT INFORMATION
    api_key = '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'
    org_id = 'org-cMRrZweyGUcQPXCwXcub7hc9'

    # INSTANTIATE Main OBJECT
    main = Main(api_key, org_id)

    # INSTANTIATE Patient OBJECT
    last_meal_time = datetime.strptime('3:00 PM', '%I:%M %p')
    diabetic_patient = Patient(dh.get_data_by_patient(patient=0, profile=4), last_meal_time=last_meal_time, dietary_restrictions='vegan', budget='20')

    # GET DINNER MEAL RECOMMENDATIONS FOR diabetic_patient
    #response = main.instantaneous_blood_glucose_prompt(diabetic_patient, 'dinner')
    #print(response)

    # SEE HOW CHATGPT INTERPRETS BLOOD-GLUCOSE LEVELS
    #log = main.blood_glucose_increment_test()
    #print(log)
