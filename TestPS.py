import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../package')))

import unittest
from io import StringIO
from tabulate import tabulate
from package.subpckg1.PersonalSummary import PersonalSummary
from unittest.mock import patch

class TestPersonalSummary(unittest.TestCase):

    @patch('builtins.input', side_effect=['John', '170', '70', '25', 'M'])
    def test_collect_info(self, mock_input):
        
        ps = PersonalSummary()

        ps.collect_info()

        self.assertEqual(ps.name, 'John')
        self.assertEqual(ps.height, 170.0)
        self.assertEqual(ps.weight, 70.0)
        self.assertEqual(ps.age, 25)
        self.assertEqual(ps.gender, 'M')

    @patch('builtins.input', side_effect=['John', '170', '70', '25', 'M'])
    def test_calculate_BMI(self, mock_input):
        
        ps = PersonalSummary()

        ps.collect_info()

        ps.calculate_BMI()

        self.assertEqual(ps.BMI, 24)  # BMI = 70 / (1.7 ** 2) -> 24

    
