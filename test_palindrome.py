import unittest
import palindrome

#unittest

class TestCase (unittest.TestCase):
    def test_1(self):
        self.assertEqual(palindrome.isPalindrome("dad dad"),"is a palindrome")

    def test_2(self):
        self.assertEqual(palindrome.isPalindrome("my name is katie"),"is not a palindrome")

    def test_3(self):
        self.assertEqual(palindrome.isPalindrome(1001),1)

    def test_4(self):
        self.assertEqual(palindrome.isPalindrome(12),1)

if __name__ == '__main__':
    unittest.main(verbosity=2)

#pytest

def test_1():
    assert palindrome.isPalindrome("dad dad") == "is a palindrome"

def test_2():
    assert palindrome.isPalindrome("my name is katie") == "is not a palindrome"

def test_3():
    assert palindrome.isPalindrome(1001) == 1

def test_4():
    assert palindrome.isPalindrome(12) == 1