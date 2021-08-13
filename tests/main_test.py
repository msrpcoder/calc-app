import unittest
import main

class MainTest(unittest.TestCase):
  def test_constructor():
    obj = main.Calc('add', 1, 2)
    assert obj.operator  == 'add',
    assert obj.param1 == 1
    assert obj.param2 == 2
