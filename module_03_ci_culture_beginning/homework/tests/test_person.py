import unittest
import datetime
from homework.hw4.person import Person

class TestPerson(unittest.TestCase):
    def setUp(self):
        self.person = Person('Zamir', 2000)

    def test_init(self):
        self.assertEqual(self.person.name, 'Zamir')
        self.assertEqual(self.person.yob, 2000)
        self.assertEqual(self.person.address, '')

    def test_get_age(self):
        now = datetime.datetime.now()
        expected_age = now.year - self.person.yob
        self.assertEqual(self.person.get_age(), expected_age)

    def test_get_name(self):
        self.assertEqual(self.person.get_name(), 'Zamir')

    def test_set_name(self):
        new_name = 'Vampir'
        self.person.set_name(new_name)
        self.assertEqual(self.person.get_name(), new_name)

    def test_set_adress(self):
        new_address = '123 PP'
        self.person.set_address(new_address)
        self.assertEqual(self.person.get_address(), new_address)

    def test_get_address(self):
        self.assertEqual(self.person.get_address(), '')

    def test_is_homeless(self):
        self.person.set_address('')
        self.assertTrue(self.person.is_homeless())
        self.person.set_address('123 PP')
        self.assertFalse(self.person.is_homeless())