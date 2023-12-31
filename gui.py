# IMPORT MODULES
from tkinter import *
from datetime import datetime, timedelta

class LoginWindow:
    """Class to represent a login/signup window"""

    def __init__(self, size: tuple, title: str) -> None:
        """Defines the constructor for a LoginWindow object"""
        self.window = Tk()
        self.window.title(title)
        self.window.minsize(size[0], size[1])

        self.values_list = []
        self.patient = None

    def add_widgets(self) -> None:
        """Adds widgets to window"""
        # LOGIN
        login_heading = Label(self.window, text = "Login", font=("Arial", 25), pady=20).grid(row=0, column=0)

        self.username1 = Entry(self.window, width=25)
        self.username1.grid(row=1, column=1)
        username_label1 = Label(self.window, text = "Username:", padx=15).grid(row=1, column=0)

        self.password1 = Entry(self.window, width=25)
        self.password1.grid(row=2, column=1)
        password_label1 = Label(self.window, text = "Password:").grid(row=2, column=0)

        self.login = Button(self.window, text ="Login", command = self.user_login).grid(row=5, column=1)

        # SIGNUP
        signup_heading = Label(self.window, text = "Signup", font=("Arial", 25), pady=20).grid(row=6, column=0)

        self.username2 = Entry(self.window, width=25)
        self.username2.grid(row=7, column=1)
        username_label2 = Label(self.window, text = "Username:", padx=15).grid(row=7, column=0)

        self.password2 = Entry(self.window, width=25)
        self.password2.grid(row=8, column=1)
        password_label2 = Label(self.window, text = "Password:", padx=15).grid(row=8, column=0)

        dietary_restrictions = Entry(self.window, width=25)
        dietary_restrictions.grid(row=9, column=1)
        dietary_restrictions_label = Label(self.window, text='Dietary Restrictions:', padx=15).grid(row=9, column=0)

        medication = Entry(self.window, width=25)
        medication.grid(row=10, column=1)
        medication_label = Label(self.window, text='Medications:', padx=15).grid(row=10, column=0)

        self.signup = Button(self.window, text ="Signup", command = self.user_signup).grid(row=11, column=1)

    def launch(self) -> None:
        """Execute main event loop"""
        self.window.mainloop()

    def user_login(self) -> None:
        """Logs a user into the server using inputted information"""
        # GET INPUTTED DATA
        username = self.username1.get(1.0, "end-1c")
        password = self.password1.get(1.0, "end-1c")

        # IF CREDENTIALS ARE VERIFIED, INSTANTIATE AND RETURN PATIENT OBJECT
        patient = None
        return patient

    def user_signup(self) -> None:
        """Creates new user account with inputted information"""
        # GET INPUTTED DATA
        username = self.username2.get(1.0, "end-1c")
        password = self.password2.get(1.0, "end-1c")

class MainWindow:

    def __init__(self, patient: object, dimensions=(600, 400), title="") -> None:
        self.width = dimensions[0]
        self.height = dimensions[1]
        self.window = Tk()
        self.window.geometry("{}x{}".format(self.width, self.height))
        self.title = title
        self.patient = patient

    def add_widgets(self) -> None:
        self.log_meal = Button(self.window, text ="Log Meal Time", command = self.log_meal_time).grid(row=0, column=0)
        self.get_meal_suggestions = Button(self.window, text ="Request Meal Suggestions", command = self.request_meal_suggestions).grid(row=0, column=1)

    def log_meal_time(self):
        log_time = datetime.now()

    def request_meal_suggestions(self):
        meal_planning_window = MealPlanningWindow(self.patient)
        meal_planning_window.add_widgets()
        meal_planning_window.launch()

        meal_suggestions = meal_planning_window.meal_suggestions

        messagebox.showinfo(title="Meal Suggestions", message=meal_suggestions, **options)

    def launch(self) -> None:
        self.window.mainloop()


class MealPlanningWindow:

    def __init__(self, patient: object, dimensions=(600, 400), title="") -> None:
        self.width = dimensions[0]
        self.height = dimensions[1]
        self.window = Tk()
        self.window.geometry("{}x{}".format(self.width, self.height))
        self.title = title

        self.meal_suggestions = ""

    def add_widgets(self) -> None:
        meal_inquiry_label = Label(self.window, text='Meal Inquiry:')
        meal_inquiry = Entry(self.window, width=25)
        meal_inquiry_label.grid(row=0, column=0)
        meal_inquiry.grid(row=0, column=1)

        last_meal_time_label = Label(self.window, text='Time of Last Meal:')
        last_meal_time = Entry(self.window, width=25)
        last_meal_time_label.grid(row=1, column=0)
        last_meal_time.grid(row=1, column=1)

        budget_label = Label(self.window, text='Meal Budget $:')
        budget = Entry(self.window, width=25)
        budget_label.grid(row=2, column=0)
        budget.grid(row=2, column=1)

        exercise_label = Label(self.window, text='Upcoming Exercise:')
        exercise = Entry(self.window, width=25)
        exercise_label.grid(row=3, column=0)
        exercise.grid(row=3, column=1)

        self.get_meal_suggestions = Button(self.window, text ="Request Meal Suggestions", command = self.get_meal_suggestions).grid(row=0, column=0)

    def get_meal_suggestions(self):
        self.meal_suggestions = ""

    def launch(self) -> None:
        self.window.mainloop()

if __name__ == '__main__':
    login_window = LoginWindow((300, 400), "")
    login_window.add_widgets()
    login_window.launch()

    patient = login_window.patient

    main_window = MainWindow(patient)
    main_window.add_widgets()
    main_window.launch()
