"""
Author: Tyler J. Burgee
Date: 11 July 2023
"""

# IMPORT MODULES
from data_handler import DataHandler
from data_processor import DataProcessor
from patient import Patient

class Main:

    def _create_prompt_(patient: object) -> str:
        prompt = '''
            Blood-glucose: {} mg/dL. 
            Last meal: {} hr ago. 
            Query: Is this safe? 
            If so, recommend meals for breakfast (If blood-glucose is severely low or high,
                prioritize quickly raising or lowering blood-sugar levels, respectively, before eating a meal);
            if not, what should I do (prioritize seeking medical attention over remedies)?
        '''.format(patient.get_instantaneous_blood_glucose(0), patient.get_last_meal())

        if patient.get_dietary_restrictions() is not None:
            prompt += ' Dietary restrictions: {}.'.format(patient.get_dietary_restrictions())
        if patient.get_budget() is not None:
            prompt += ' Budget: ${}.'.format(str(patient.get_budget()))
        if patient.get_exercise() is not None:
            prompt += ' Exercise: {}.'.format(patient.get_exercise())
        if patient.get_medication() is not None:
            prompt += 'Medication: {}.'.format(patient.get_medication())

        return prompt

    def blood_glucose_increment_test(increment=5):
        """
        Slowly increments blood-glucose level to determine ChatGPT's thresholds
        for what it considers healthly/unhealthy/severe blood-glucose.
        """
        pass

    def instantaneous_blood_glucose_test(patient: object):
        """Sends an instantaneous CGM reading to ChatGPT and requests meal suggestions."""
        pass

    def average_blood_glucose_test(patient: object):
        """Sends an average of CGM readings since last meal to ChatGPT and requests meal suggestions."""
        pass

if __name__ == '__main__':
    filename = 'test_db.csv'
    dh = DataHandler(filename)

    healthy_patient = Patient(dh.get_data_by_patient(patient=0, profile=1), last_meal=10)

    prompt = Main._create_prompt_(healthy_patient)
    print(prompt)

    api_key = ''
    org_id = ''
    #gpt = GPT_API(api_key, org_id)
