class Calc(object):
  def __init__(self, operator, param1, param2):
    self.operator = operator
    self.param1 = param1
    self.param2 = param2

  def calculate(self):
    method = getattr(self, self.operator, None)
    if not method:
      raise Exception(f'Invalid operator: {operator}')
      
    return method()
  
  def add(self):
    return self.param1 + self.param2
  
  def minus(self):
    return self.param1 - self.param2

def start_app():
  return {
    'add': Calc('add', 21, 38).calculate(),
    'minus': Calc('minus', 4, 2).calculate()
  }
    
if __name__ == '__main__':
  print (start_app())
