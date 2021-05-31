import unittest
import leapTDD

class TestCase(unittest.TestCase):

    #test one
    def test_leap(self):
        self.assertEqual(leapTDD.leap(4), "leap year")
        

        
   
if __name__ == '__main__':
    unittest.main()