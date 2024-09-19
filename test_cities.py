import unittest
from city_functions import city_country

class CityCountryTestCase(unittest.TestCase):
    def test_city_country(self):
        result = city_country('aalen', 'germany')
        self.assertEqual(result, 'Aalen, Germany')

if __name__ == '__main__':
    unittest.main()

