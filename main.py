"""
Author: Tyler J. Burgee
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

        for x in range(400):
            if x % 10 == 0:
                prompt = "My fasting blood-glucose level is {} mg/dL.".format(x)
                response = self.gpt.send_prompt(prompt)
                log.append(("Prompt:", prompt, "Response:", response))

        return log

    def get_meal_suggestions(self, patient: object, meal_inquiry: str) -> str:
        """Sends Patient CGM information to ChatGPT and requests meal suggestions"""
        current_blood_glucose = 'Current blood-glucose: {} mg/dL.\n'.format(patient.get_current_blood_glucose())
        start_blood_glucose = 'Blood-glucose at {}: {}.\n'.format(patient.get_last_meal_time_str(), patient.get_blood_glucose_at_time(patient.get_last_meal_time()))
        avg_blood_glucose = 'Average blood-glucose since last meal: {} mg/dL.\n'.format(patient.get_avg_blood_glucose_last_meal())
        min_blood_glucose = 'Minimum blood-glucose since last meal: {} mg/dL.\n'.format(patient.get_min_blood_glucose_last_meal())
        max_blood_glucose = 'Maximum blood-glucose since last meal: {} mg/dL.\n'.format(patient.get_max_blood_glucose_last_meal())
        last_meal = 'Last meal: {} hr ago.\n'.format(patient.get_hours_since_last_meal())
        query = 'Query: Is this safe? If so, recommend meals for {} (If blood-glucose is severely low or high, prioritize quickly raising or lowering blood-sugar levels, respectively, before eating a meal); if not, what should I do (prioritize seeking medical attention over remedies)?\n'.format(meal_inquiry)

        prompt = current_blood_glucose + start_blood_glucose + avg_blood_glucose + min_blood_glucose + max_blood_glucose + last_meal + query

        if patient.get_dietary_restrictions() != "":
            prompt += 'Dietary restrictions: {}.\n'.format(patient.get_dietary_restrictions())
        if patient.get_budget() != "":
            prompt += 'Budget: ${}.\n'.format(str(patient.get_budget()))
        if patient.get_exercise() != "":
            prompt += 'Exercise: {}.\n'.format(patient.get_exercise())
        if patient.get_medication() != "":
            prompt += 'Medication: {}.\n'.format(patient.get_medication())

        response = self.gpt.send_prompt(prompt)

        return response

if __name__ == '__main__':
    # PATIENT CGM DATA FILE
    filename = 'test_db.csv'

    # INSTANTIATE DataHandler OBJECT
    dh = DataHandler(filename)

    # GPT API ACCOUNT INFORMATION
    api_key = ''
    org_id = ''

    # INSTANTIATE Main OBJECT
    main = Main(api_key, org_id)

    print("Welcome to the Diabetic Meal Planning Portal!\n")
    print("Fields with \"*\" are required.\nAll other fields are optional and may be left blank.\n")
    print("#", "-"*35, "#")
    profile_number = input("Enter Profile Number* (1-4): ")
    patient_number = input("Enter Patient Number* (0-9): ")
    last_meal_time = input("Enter Time of Last Meal* (formatted hh:mm AM/PM): ")
    meal_inquiry = input("Enter Meal about to be Eaten* (i.e., breakfast, lunch, or dinner): ")
    dietary_restrictions = input("Enter Dietary Restrictions (separated by commas): ")
    budget = input("Enter Meal Budget $: ")
    exercise = input("Enter any upcoming exercise or notable physical activity: ")
    medication = input("Enter any medications (with amounts) being taken: ")
    print("#", "-"*35, "#")

    # INSTANTIATE Patient OBJECT
    last_meal_time = datetime.strptime(last_meal_time, '%I:%M %p')
    patient_data = dh.get_data_by_patient(patient=int(patient_number), profile=int(profile_number))
    diabetic_patient = Patient(patient_data, last_meal_time, budget, exercise, dietary_restrictions, medication)

    # GET DINNER MEAL RECOMMENDATIONS FOR diabetic_patient
    response = main.get_meal_suggestions(diabetic_patient, meal_inquiry)
    print(response)
    print("#", "-"*35, "#")

    # SEE HOW CHATGPT INTERPRETS BLOOD-GLUCOSE LEVELS
    #log = main.blood_glucose_increment_test()
    #print(log)
