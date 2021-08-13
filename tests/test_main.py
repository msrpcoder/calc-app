import unittest
import main

class MainTest(unittest.TestCase):
  def test_constructor(self):
    obj = main.Calc('add', 1, 2)
    self.assertEqual(obj.operator, 'add')
    self.assertEqual(obj.param1, 1)
    self.assertEqual(obj.param2, 2)

