import copy
import random
# Consider using the modules imported above.

class Hat:
  contents = []
  def __init__(self,**kwargs):
    self.contents = []
    for key, value in kwargs.items():
      for i in range(value):
        self.contents.append(key)
    
  def draw(self, nballs):  
    aux = []
    if (nballs >= len(self.contents)):
      aux = self.contents
      self.contents = []
      return aux
    for i in range(nballs):
      aux.append(self.contents.pop(random.randint(0,len(self.contents)-1)))
    return aux

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  n = 0
  for i in range(num_experiments):
    drawn = []
    #string2 = copy.copy(string)
    hatexp = copy.deepcopy(hat)
    drawn = hatexp.draw(num_balls_drawn)
    check = True
    for key,value in expected_balls.items():
      if (value > drawn.count(key)):
        check = False
        break
    if(check):
      n += 1
  return n/num_experiments
