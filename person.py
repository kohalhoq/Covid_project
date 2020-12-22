import sys
import pandas as pd


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
     """

    

    def __init__(self, name, age, country, is_smoker, gender):
        """Constructor for the class"""
        self.name = name
        self.age = age
        self.country = country
        self.is_smoker = is_smoker
        self.gender = gender


    @classmethod
    def withnoargs(cls) -> 'Person':
        return cls(None, None, None, None, None)

        
    def answer_questions(self):
        """Asks questions to get some personal information about the person and creates an instance of the Person class.
        
        Side effect
        ---
        Writes to stdout

        """

        name = input("Please enter your full name : ")
        print(f"Hi {name}! Hope you're doing well. Kindly take some time out to answer this questionnaire.")
        self.name = name

        while True:
            try:
                age = int(input("What's your age? (Only enter a positive integer value) : "))
            except ValueError:
                print("Please enter a valid value for age. Postive integers only.")
                continue
            if age <= 0:
                print("Please enter a valid value for age. Postive integers only.")
                continue
            self.age = age
            break


        country = input("What is your country of residence? : ")
        self.country = country

        while True:
            is_smoker = input("Are you a smoker? (Y/N) : ")
            if is_smoker.lower().strip() not in ('y', 'n'):
                print("Please enter a valid response (Y/N)")
                continue
            else:
                if is_smoker.lower().strip() == 'y':
                    self.is_smoker = True
                else:
                    self.is_smoker = False
                break
        
        while True:
            gender = input("What is your gender? (M/F) : ")
            if gender.lower().strip() not in ('m', 'f'):
                print("Please enter a valid response (M/F).")
                continue
            else:
                if gender.lower().strip() == 'm':
                    self.gender = 'M'
                else:
                    self.gender = 'F'
                break
        print("People of older age, with habit of smoking or males have higher chances of getting affected by Covid-19.")

    
    def questions(self):
    """ This function will ask the questions about symptoms, symptom span and indoor or outdoor 
    Attributes : 
    list_of_symptoms: questions about list_of_symptoms the users are encountering 
    symptoms_span : time frame for the existing symtomps
    in_or_out: Indoor and outdoor staying tendencies 
    Returns:
    list_of_symptoms(str): list_of_symptoms users chose from the provided list 
    get_tested: whether or not the user should consider getting tested
    quarintine : whether or not user should stay in quarantine
    """
      
        print ("Mention the list_of_symptoms that you are facing from the following list")
    
        symp= ["1. Fever or chills", "2. Cough", "3.Shortness of breathe", 
        "4.Difficulty breathing", "5. Fatigue", "6. Body/muscle ache",
        "7.Headache","8.New loss of tase or smell", "9. Sore throat", 
        "10. Congestion or runny nose", "11. Nausea or vomiting", "12. Diarrhea"]

        print (symp)
        user_ans = str(input("list_of_symptoms:"))
        print (user_ans)
        x= int(input("How many days have you been facing the list_of_symptoms: "))
        if x > 14:
            if len(symp) > 3:
                return f" Your have {user_ans} symptoms. Please consider getting a test for Covid-19"
        if x <14:
            return symp
            print("Please wait at least 14 days in quarantine before getting tested")
        ans = input(" Have you been staying indoor or outdoor more commonly in the last few days: ")
      
        if ans == "Indoor":
            return None
        if ans == "Outdoor":
            contact = input("Have you been in contact with any other covid patient recently: ")
            print(contact)
            if contact is yes:
                return f("You need to be in quarantine")
            else:
                return None
        
   
    
    def use_gender(self):
        output = '' 
        if self.gender == 'M': 
            output = 'Men have a 20% higher chance of dying from COVID-19. Stay safe!'
        else:
            output = 'Women are less likely to die from COVID-19. Still be careful though!
        return output
    use_gender()
                    
    
   def testing_centers(self):
        """Method to request a users location and return nearby covid testing centers"""
        userstate = input("What state are you located in (Abbreviation): ").upper()
        usercity = input("What city are you located in? (No Abbreviation): ").upper()

        df = pd.read_csv("HHS_Provider_Relief_Fund.csv")
        df3 = df[df["State"] == userstate]
        df5 = df3[df3["City"] == usercity]
        listvals = df5.values
        for item in listvals:
            print(f"\n----------\nName: {item[0]}\nState: {item[1]}\nCity: {item[2]}")

        with open("states.json", "r", encoding="utf-8") as file:states = json.load(file)
        userstate = states[userstate.upper()]

        with open("covid_data.csv", "r", encoding="utf-8") as file:
            csv = file.readlines()[3:]
        columns = csv[0].split(",")
        csv = csv[1:]
        for row in csv:
            if row.split(",")[0].lower() == userstate.lower():
                for item in range(len(row.split(","))):
                    print(columns[item].replace("\n", "") + ": " + row.split(",")[item])
      
      
   def travelling_overseas(self):
    """ This function will ask the question about overseas travelling 
    Attributes:
        time: time spend in any foreign location
        location: location of the area of visting
        frequency: number of times the location was visited by users
     Returns:
        travel_stat: identify the level of risk for specific country
    """
    print ("If you have taken any overseas trip please answer the following questions")
    frequency = int(input("What is the frequency of your travel:"))
    if frequency > 1:
        print(" Please retake the quiz if you have travelled more than once using different location ")
    
    time = int(input("Amount of time spent on the location in days:"))
    location = input("Enter the location you have travelled to: ")
    df = pd.read_csv('Covid_data1.csv')
    list1 = df['Location'].tolist()
    df.head()
    if location in list1:
        print(location)
    else:
        print("Not Applicable")
    if location in list1[0:13]:
        return f" {location} is Level 4 risk Area"
    elif location in list1[14:66]:
        return f"{location} is Level 3 risk area"
    elif location in list1[67:172]:
        return f"{location} is Level 2 risk area"
    else:
        return f"{location} is Level 1 risk area"




 def nursing home(self):
    answer = input('Have you been to a nursing home recently are more likely to get COVID-19. Please seek medical attention' (Y/N)?')
    if answer = 'Y': 
        return 'People who have been to a nursing home recenly are more likely to get COVID-19;
    else:
        return 'You are less likely to have COVID-19 since you have not visited a nursing home'
                                     
                                  

if __name__ == "__main__":
    c = Person.withnoargs()
    c.answer_questions()
    c.questions()
    c.use_gender()
    c.testing_centers()
    c.travelling_overseas()
