import pytest
from person import travelling_overseas

def test_person(time, location):
  assert person_travelling_overseas(16, Kenya, 1) = Level 3 risk area
  assert person_travelling_overseas( 25, Vatican city,1) = Level 1 risk area
  assert person_travelling_overseas (10, Brazil,1) = Level 4 risk area

def test_person_edge(time,location):
  assert person_travelling_overseas(27, Tunisia,1) = Level 2 risk area
  assert person_travelling_overseas( 45, Venezuela,1) = Level 3 risk area
  assert person_travelling_overseas (32, Poland,1) = Level 4 risk area
  with pytest.raises(Exception):
      pass
  
def test_use_gender():
  person1 = Person('Nadia', 20, 'USA', True, 'F')
  person2 = Person('James', 20, 'USA', False' 'M')
  assert person1.use_gender() = 'Women are less likely to die from COVID-19. Still be careful though!'
  assert person2.use_gender() = 'Men have a 20% higher chance of dying from COVID-19. Stay safe!'
