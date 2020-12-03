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

    def questions(symptoms,symptoms_span, indoor_or_outdoor ):
    """ This function will ask the questions about symptoms for covid
    Attributes : 
    symptoms: will consist of questions about symptoms the users are encountering 
    Returns:
    list_of_symptoms: List of symptoms users chose from the provided list of symptoms
    """
    print ("Mention the symptoms that you are facing from the following list")
    list_of_symptoms = ["1. Fever or chills", "2. Cough", "3.Shortness of breathe", 
    "4.Difficulty breathing", "5. Fatigue", "6. Body/muscle ache",
     "7.Headache","8.New loss of tase or smell", "9. Sore throat", 
     "10. Congestion or runny nose", "11. Nausea or vomiting", "12. Diarrhea"]
    print (list_of_symptoms)
    user_ans = str(input("Symptoms:"))
    print (user_ans)
    x= input("How many days have you been facing the symptoms: ")
    print(x)
    if x>14:
        if list_of_symtomps > 3:
          return (list_of_symptoms)
    if x<14:
       return list_of_symtoms
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
    t = input("Amount of time spent on the location in days")
    print(t)
    self.location = location
    location = input("Enter the location you have travelled to: ")
    print(location)
    list = df['A'].tolist(loc)
    loc= []
    if location in list:
        print loc
    else:
        print ("Not Applicable")
    df = pd.read_excel (r'Covid data.xlsx')
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
