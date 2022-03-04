import unittest

from translator import englishToFrench, frenchToEnglish

class Tests(unittest.TestCase):
    def test_frenchToEnglish(self):
        self.assertEqual(frenchToEnglish("Bonjour"), "Hello")

    def test_englishToFrench(self):
        self.assertEqual(englishToFrench("Hello"), "Bonjour")
        


if __name__ == '__main__':
    unittest.main()
