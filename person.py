import sys
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

class Person:
    """A class that represents a person taking the COVID-19 survey.
    
    Attributes
    ---------------
    name : str
        Name of the person
    age : int
        Age of the person
    country : str
        Current country of residence for the person
    is_smoker : boolean
        A boolean representing whether the person smokes or not.

    

    def __init__(self, name, age, country, is_smoker):
        """Constructor for the class"""
        self.name = name
        self.age = age
        self.country = country
        self.is_smoker = is_smoker
        
        
def answer_questions():
    """Asks questions to get some personal information about the person and creates an instance of the Person class."""
    name = input("Please enter your full name : ")
    print(f"Hi {name}! Hope you're doing well. Kindly take some time out to answer this questionnaire.")
    print("")
    age = input("What's your age? (Only enter a positive integer value)")
    try:
        age = int(age)
    except Exception as e:
        print("Please enter a valid value for age (positive integer)")
        age = input("What's your age? (Only enter a positive integer value)")
        age = int(age)
    country = input("What is your country of residence?")
    is_smoker = input("Are you a smoker? (Y/N)")
    if 'y' in is_smoker.lower():
        is_smoker = True
    else:
        is_smoker = False
    
    return Person(name, age, country, is_smoker)


def questions(self, list_of_symptoms,list_of_symptoms_span, in_or_out ):
    """ This function will ask the questions about list_of_symptoms for covid
    Attributes : 
    list_of_symptoms: will consist of questions about list_of_symptoms the users are encountering 
    Returns:
    list_of_list_of_symptoms: List of list_of_symptoms users chose from the provided list of list_of_symptoms
    """
    self.list_of_symptoms = list_of_symptoms
    self.symptoms_span = x
    self.in_or_out = ans

    print ("Mention the list_of_symptoms that you are facing from the following list")
    list_of_symptoms = ["1. Fever or chills", "2. Cough", "3.Shortness of breathe", 
    "4.Difficulty breathing", "5. Fatigue", "6. Body/muscle ache",
     "7.Headache","8.New loss of tase or smell", "9. Sore throat", 
     "10. Congestion or runny nose", "11. Nausea or vomiting", "12. Diarrhea"]

    print (list_of_symptoms)
    user_ans = str(input("list_of_symptoms:"))
    print (user_ans)
    x= input("How many days have you been facing the list_of_symptoms: ")
    print(x)
    if x>14:
        if list_of_symtomps > 3:
          return (list_of_symptoms)
    if x<14:
       return list_of_symptoms
       print("Please wait at least 14 days in quarantine before getting tested")
    ans = input(" Have you been staying indoor or outdoor more commonly in the last few days: ")
    print(ans)
    if ans == "Indoor":
        return None
    if ans == "Outdoor":
        contact = input("Have you been in contact with any other covid patient recently: ")
        print(contact)
        if contact is yes:
            return f("You need to be in quarantine")
        else:
            return None
    else:
        print ("Not valid")
        
def state_statistics(self):
        """Method to request a users state and supply the current covid statistics for the given state

        Returns:
            Covid statistics in a uses given state"""

        userstate = input("What state are you located in (No abbreviation): ").lower()


        with open("covid_data.csv", "r", encoding="utf-8") as file:
            csv = file.readlines()[3:]
        columns = csv[0].split(",")
        csv = csv[1:]
        for row in csv:
            if row.split(",")[0].lower() == userstate:
                for item in range(len(row.split(","))):
                    print(columns[item].replace("\n","")+": "+row.split(",")[item])
                    
def testing_centers(self):
        """Method to request a users location and return nearby covid testing centers

        Returns:
            Covid testing centers in the users given state
        """
        userstate = input("What state are you located in (Abbreviation): ").upper()

        with open("HHS_Provider_Relief_Fund.csv", "r", encoding="utf-8") as file:
            csv = file.readlines()[1:]
        for line in csv:
            if line.split(",")[1] == userstate:
                print(f"\n----------\nName: {line.split(',')[0]}\nState: {line.split(',')[1]}\nCity: {line.split(',')[2]}")
      
      
def travelling_overseas(self, time, location, frequency):
    """ This function will ask the question about travelling informations of the users 
    Attributes: 
    time: time spend in any foreign location
    location: location of the area of visting 
    frquency: number of times the location was visited by users 
    Returns: 
    travelling_statistics: take the provided statistics and identify the risk of being exposed to covid
    """
    self.time= time
    time = input("Amount of time spent on the location in days")
    print(time)
    self.location = location
    location = input("Enter the location you have travelled to: ")
    print(location)
    list = df['A'].tolist(loc)
    loc= []
    if location in list:
        print loc
    else:
        print ("Not Applicable")
    df = pd.read_csv('covid data')
    if df.iloc[2:15]:
        return f(" Level 4 risk Area")
    elif df.iloc[16:68]:
        return f("Level 3 risk area")
    elif df.iloc[69:174]:
        return f("Level 2 risk area")
    else:
        return f("Level 1 risk area")
        
        
    self.frequency = frequency 
    frequency = input("What is the frequency of your travel:")
    if frequency > 1:
        print (" Please retake the quiz if you have travelled more than once using different location " )
    else:
        return frequency 


def main1(symptoms,symptoms_span,in_or_out):
    for symptoms, symptoms_span, in_or_out in questions(symptoms, symptoms_span, in_or_out):
        print(symptoms, symptoms_span, in_or_out)

def main2(time, location, frequency):
    for time, location, frequency in travelling_overseas(time, location, frequency):
        print(time, location, frequency)
