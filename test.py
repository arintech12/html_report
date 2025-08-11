import unittest
from io import StringIO
from unittest.mock import patch
from say_my_name import say_my_name

class TestHandlerCase(unittest.TestCase):
    def test_valid_name(self):
        name = 'testmycode'
        expected_output = f'{name}??? You are right !!!\n'
        with patch('sys.stdout', new=StringIO()) as fake_out:
            say_my_name(name)
            self.assertEqual(fake_out.getvalue(), expected_output)
    
    def test_empty_string(self):
        name = ""
        expected_output = "Heisenberg??? You are right !!!\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            say_my_name(name)
            self.assertEqual(fake_out.getvalue(), expected_output)
    
    def test_none_input(self):
        expected_output = "Heisenberg??? You are right !!!\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            say_my_name(None)
            self.assertEqual(fake_out.getvalue(), expected_output)
    
    def test_whitespace_name(self):
        name = "   "
        expected_output = f'{name}??? You are right !!!\n'
        with patch('sys.stdout', new=StringIO()) as fake_out:
            say_my_name(name)
            self.assertEqual(fake_out.getvalue(), expected_output)

if __name__ == "__main__":
    unittest.main()
