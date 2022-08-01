import unittest

from translator import english_to_french, french_to_english

class TestTranslate(unittest.TestCase):
    def test_null_fr_en(self):
        self.assertEqual(french_to_english(None), "")

    def test_null_en_fr(self):
        self.assertEqual(english_to_french(None), "")
        
    def test_bonjour_fr_en(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")

    def test_hello_en_fr(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour")

if __name__ == '__main__':
    unittest.main()