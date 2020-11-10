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

    
    Methods
    ----------------
    take_survey()
        Validates the survey data filled in by the person and stores it.
    get_stats()
        Gives a summary of the person's standing against the existing data.
    """

    def __init__(self, name, age, country, is_smoker):
        """Constructor for the class"""
        self.name = name
        self.age = age
        self.country = country
        self.is_smoker = is_smoker

    def take_survey(self):
        """Method for recording the answers to survey questions [stub]"""
        pass

    def get_stats(self):
        """Method for getting the summary of a person's standing the population"""
