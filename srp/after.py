import re
import unittest


EMAIL_PATTERN = re.compile(r'^([\w-]+(?:\.[\w-]+)*)@((?:[\w-]+\.)*\w[\w-]{0,66})\.([a-z]{2,6}(?:\.[a-z]{2})?)$')


class Email:
    def __init__(self, email):
        if EMAIL_PATTERN.match(email) is None:
            raise ValueError('Invalid email')

        self.email = email

class Person:
    def __init__(self, first_name, last_name, email):
        assert isinstance(first_name, str)
        assert isinstance(last_name, str)
        assert isinstance(email, str)
        
        self.first_name = first_name 
        self.last_name = last_name
        self.email = Email(email)


class PersonTests(unittest.TestCase):
    def test_valid_email(self):
        Person('Jan', 'Kowalski', 'jan@kowalski.pl')

    def test_invalid_email(self):
        with self.assertRaises(ValueError):
            Person('Jan', 'Kowalski', 'invalid email')


if __name__ == "__main__":
    unittest.main()
