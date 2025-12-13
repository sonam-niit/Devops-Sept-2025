import unittest
from calculator import add,sub

class CalculatorTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1,2),3) # positive
        self.assertEqual(add(-1,1),0) # negative
        self.assertEqual(add(0,0),0) # zeros
    def test_sub(self):
        self.assertEqual(sub(-1,1),-2)
        
        
if __name__ == "__main__":
    unittest.main()
# python test_unittest.py (run with main)
# python -m unittest test_unittest.py (direct execution without main will work)