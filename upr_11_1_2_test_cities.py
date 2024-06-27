import unittest
from upr_11_1_2_city_functions import get_city_name

class NamesTestCase(unittest.TestCase):
    def test_city_country(self):
        formatted_name = get_city_name('santiago', 'chile')
        self.assertEqual(formatted_name, 'Santiago, Chile')

    def test_city_country_population(self):
        formatted_name = get_city_name('santiago', 'chile', '5000000')
        self.assertEqual(formatted_name, 'Santiago, Chile Population= 5000000')

unittest.main()