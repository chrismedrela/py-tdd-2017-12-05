# encoding: utf-8

'''Testowany kod - funkcja factorial'''

def factorial(num):
    if not isinstance(num, int):
        raise TypeError('Argument must be int')

    if num == 0:
        return 1
    else:
        return factorial(num-1) * num

'''Najprostsze testy'''

import unittest

class FactorialTests(unittest.TestCase):
    def test_factorial_of_one(self):
        got = factorial(1)
        expected = 1
        self.assertEqual(got, expected)

    def test_factorial_of_two(self):
        got = factorial(2)
        expected = 2
        self.assertEqual(got, expected)

    def test_factorial_of_three(self):
        got = factorial(3)
        expected = 6
        self.assertEqual(got, expected)

    def test_failing(self):
        raise ValueError()

    def test_raises_typeerror_for_invalid_argument(self):
        with self.assertRaises(TypeError):
            factorial(2.5)

'''setUp'''

class SetUp(unittest.TestCase):
    def setUp(self):
        print('Setup')

    def test_pass(self):
        print('Passing test')

    def test_error(self):
        print('Test resulting in an error')
        raise ValueError()

    def test_fail(self):
        print('Failing test')
        self.fail()

'''Asercje'''

class Assertions(unittest.TestCase):
    def test(self):
        self.assertTrue(['not-empty'])
        self.assertFalse([])
        
        self.assertNotEqual(2, 3)
        
        first_dict = {}
        second_dict = {}
        self.assertIsNot(first_dict, second_dict)
        self.assertEqual(first_dict, second_dict)

        self.assertIsNone(None)
        self.assertIsNotNone({})
        
        self.assertIn('bar', ['foo', 'bar', 'spam'])
        self.assertIsInstance([], list)
        self.assertIsInstance(2, (int, float))
        self.assertIsInstance(2.5, (int, float))

    def test_fail_immediatelly(self):
        self.fail('reason')

'''Uruchomienie skryptu powoduje automatyczne wystartowanie testów'''

if __name__ == "__main__":
    unittest.main()

'''
Dodatkowe argumenty, które można przekazać w CLI:

    -v for higher verbosity
    -q for quiet
    -f for fail-fast (Python 3.2+)
    --locals for displaying values of local variables in tracebacks (Python 3.5+)

Uruchomienie testów:

    python3 -m unittest 
    python3 -m unittest FactorialTests.test_factorial_of_one
'''