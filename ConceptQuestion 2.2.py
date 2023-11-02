"""2.2   Make a new test file and write comprehensive unit tests for the
             function you wrote in 2.1"""
from unittest import TestCase
from ConceptQuestion import is_isogram

def is_isogram(input_string):

    class TestIsIsogram(unittest.TestCase):

        def test_empty_string(self):
            self.assertTrue(is_isogram(""))

        def test_single_character(self):
            self.assertTrue(is_isogram("a"))
            self.assertTrue(is_isogram("A"))
            self.assertTrue(is_isogram("z"))
            self.assertTrue(is_isogram("Z"))

        def test_lowercase_isogram(self):
            self.assertTrue(is_isogram("isogram"))
            self.assertTrue(is_isogram("uncopyrightable"))

        def test_uppercase_isogram(self):
            self.assertTrue(is_isogram("ISoGRaM"))
            self.assertTrue(is_isogram("UNCOpyrIGHtABlE"))

        def test_mixed_case_isogram(self):
            self.assertTrue(is_isogram("IsOgRaM"))
            self.assertTrue(is_isogram("uNcOPYriGHtAbLE"))

        def test_non_isogram(self):
            self.assertFalse(is_isogram("ambidextrously"))
            self.assertFalse(is_isogram("hello"))
            self.assertFalse(is_isogram("aabbcdef"))

if __name__ == '__main__':
    unittest.main()
