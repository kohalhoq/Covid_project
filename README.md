# Covid_project-
Final Project about Covid_19 Pandemic 

class Questions:
  """This class will consist of the questions that would be asked to the users to verify their symptoms, travelling frequencies, contacts with other covid patients that will help the code identify if the user is in need for medical assistance
  """
  
    def ___init___(self):
      """This function will initialise the class in roder to start the quiz
      """
    
    def symptoms_questions(self, symptoms,symptoms_span):
      """ This function will ask the questions about symptoms for covid
      Attributes : 
        symptoms: will consist of questions about symptoms the users are encountering 
       Returns:
       list_of_symptoms: List of symptoms users chose from checking boxes from the provided list of symptoms and other symtoms users chose to manually provide
       """
       print ("Mention the symptoms that you are facing from the following list")
       list_of_symptoms = ["1. Fever or chills", "2. Cough", "3.Shortness of breathe", "4.Difficulty breathing", "5. Fatigue", "6. Body/muscle ache", "7.Headache",        "8.New loss of tase or smell", "9. Sore throat", "10. Congestion or runny nose", "11. Nausea or vomiting", "12. Diarrhea"
       print (list_of_symptoms)
       user_ans = str(input("Symptoms:"))
       print (user_ans)
       
       x= print(str(input("How many days have you been facing the symptoms: ")
       if x>14
        
       if x<14
         print("Please wait at least 14 days in quarantine before getting tested")
         
      
      
     def travelling_question(self, time, location, frequency)
     """ This function will ask the question about travelling informations of the users 
     Attributes: 
      time: time spend in any foreign location
      location: location of the area of visting 
      frquency: number of times the location was visited by users 
     Returns: 
      travelling_statistics: take the provided statistics about different nations and use this function to identify the risk of being exposed to covid
      """
      self.time= time
      print(" Mention the travelling you have done within the last month ")
      time = str(input("Amount of time spent on the location in days")
      print(time)
      self.location = location
      l4_location = 
      
      
   
      
      def physical_contact(self, contact)
      """ This functions will consist of questions for the contact with other covid patients or possible covid affected individuals
      Attributes:
        contact: connection or contact the user has faced recently with other covid/possible covid patients 
       Returns: 
        quarantine_requirement: provide if the user needs to quarantined from other individuals
        social_distancing_requirement : provide the social distancing norms to the users
        """
        contact = print(input("Have you been in contact with any other covid patient recently: "))
        if contact is yes 
          return f("You need to be in quarantine")
         else
          Return None
         proximity = print (input(" is anyone in you family, friend or nearby surrounding affected by covid: "))
         if proximity == "Yes" or "yes"
         return f(" please consider getting tested and be in quarantine")
         
      def location_questions(self, indoors, outdoors)
        "" This function will ask the question about whether the user is currently indoors or outdoors""
        Attributes:
         
        Returns: 
        quarantine_requirement: provide if the user needs to quarantined from other individuals
        social_distancing_requirement : provide the social distancing norms to the users
        """
        
        
        def seek_attention(self, symptoms, contact, location, time, frequency)
       """This function will show the calculation of an individual risk evaluation for each response to the question"""
       
       Attributes: 
        Symptoms: A risk score for the potential of having COVID-19 will be given based on user responses
        Contact: A risk score of contactraction will be calculated from close contact, whether indoors or outdoors, or whether the user was in a place of high exporsure
        Location: A risk score calculated from visiting an area that has high COVID-19 infection rate-- whether state or recent exposure to high-infection areas
        Time: Risk score based on how long they were exposed to someone in contact
        Frequency: A risk score associated with the frequency in which they have been experiencing symptoms
        
       Returns: 
        Overall risk score (int.) of having contracted COVID, and advice as to whether the user has to get tested, along with other advice. 
     
 
 
 
 
