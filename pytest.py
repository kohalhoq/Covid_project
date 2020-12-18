import pytest
from person import travelling_overseas

def test_questions():
    with mock.patch("builtins.input", 
                side_effect= ["2,4,6,7", 
                "15", "Indoor"])
        assert questions(list_of_symptoms, symptoms_span, in_or_out) == 
        "You have 4 symptoms, Please consider getting tested for Covid-19"
    with mock.patch ("builtins.input",
                    side_effect = ["5,9","10"])
        assert questions(list_of_symptoms, symptoms_span, in_or_out) == 
        "Please wait at least 14 days in quarantine before getting tested"
    with mock.patch ("builtins.input", 
                    side_effects =  ["4,5,3,7,8", "20", "Outdoor", "Yes"])
        assert questions(list_of_symptoms, symptoms_span, in_or_out)==
        "You have 5 symptoms, Please consider getting tested for Covid-19"
        assert questions()== 
        "You need to be in quarantine" 
        ctd = capsys.readouterr()
        assert ctd.out == ("")
        
  
def test_use_gender():
  person1 = Person('Nadia', 20, 'USA', True, 'F')
  person2 = Person('James', 20, 'USA', False' 'M')
  assert person1.use_gender() = 'Women are less likely to die from COVID-19. Still be careful though!'
  assert person2.use_gender() = 'Men have a 20% higher chance of dying from COVID-19. Stay safe!'
