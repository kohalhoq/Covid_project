import pytest
from person import travelling_overseas
from person import Person
from unittest import mock
import hashlib


def test_answer_questions(capsys):
    p1 = Person.withnoargs()
    with mock.patch("builtins.input", side_effect=["Paulo Matos", "19", "Brazil", "J", "N", "M"]):
        p1.answer_questions()
        captured = capsys.readouterr()
        print(captured)
        assert captured.out == (
            "Hi Paulo Matos! Hope you're doing well. Kindly take some time out to answer this questionnaire.\n"
            "People of older age, with habit of smoking or males have higher chances of getting affected by Covid-19.\n"
        )
        assert p1.name == "Paulo Matos"
        assert p1.age == 19
        assert p1.country == "Brazil"
        assert p1.is_smoker == False
        assert p1.gender == "M"
    

    p2 = Person.withnoargs()
    with mock.patch("builtins.input", side_effect=["Paulo Matos", "twenty three", "23", "Brazil", "N", "M"]):
        p2.answer_questions()
        assert p2.name == "Paulo Matos"
        assert p2.age == 23
        assert p2.country == "Brazil"
        assert p2.is_smoker == False
        assert p2.gender == "M"


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
                   
                   

def test():
    p = Person()
    assert str(hashlib.sha1(p.testing_centers("PA", "LANCASTER").encode()).hexdigest()) == "18f511a2f62cd66cb0927c7f16bbe4c7d7aeb5a6"
    assert str(hashlib.sha1(p.testing_centers("WY", "WORLAND").encode()).hexdigest()) == "95dad92de06cb4cef6a5ba8cbd71a617c2ce423c"
    assert str(hashlib.sha1(p.testing_centers("AK", "ANCHOR POINT").encode()).hexdigest()) == "db6729e9d51812cbea8dce730ce7073d6a2e980b"
    assert str(hashlib.sha1(p.testing_centers("CA", "SAN DIEGO").encode()).hexdigest()) == "42d4c25c6417f82b406505fbbb49b82c79ad369a"
test()
