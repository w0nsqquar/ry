import  test_reverse_string
import unittest

def reverse_string(s):
    return s[::-1]

class TestReverseString(test_reverse_string.TestCase):

    def test_empty_string(self):
        self.assertEqual(reverse_string(""), "")

    def test_single_character(self):
        self.assertEqual(reverse_string("a"), "a")


    def test_normal_string(self):
        self.assertEqual(reverse_string("hello"), "olleh")

    def test_string_with_spaces(self):
        self.assertEqual(reverse_string("hello world"), "dlrow olleh")

    def test_string_with_special_characters(self):
        self.assertEqual(reverse_string("hello, world!"), "!dlrow ,olleh")

if __name__ == '__main__':
    test_reverse_string.main()
