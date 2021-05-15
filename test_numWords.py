#unittest

import unittest
import numWords

class TestCase (unittest.TestCase):
    def test_1(self):
        self.assertEqual(numWords.printNumWords("How are you"),'3')

    def test_2(self):
        self.assertEqual(numWords.printNumWords("d d d d d"),'5')

    def test_3(self):
        self.assertEqual(numWords.printNumWords(12),-1)

if __name__ == '__main__': 
    unittest.main(verbosity=2) 


#pytest

#def test_1():
#    assert numWords.printNumWords("how are you") == '3'

#def test_2():
#    assert numWords.printNumWords("d d d d d") == '5'

#def test_3():
#    assert numWords.printNumWords(12) == -1