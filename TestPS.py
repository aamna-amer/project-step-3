import sys
import os

# Add the 'package' directory to sys.path so Python can find it
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../package')))

import unittest
from io import StringIO
from tabulate import tabulate
from package.subpckg1.PersonalSummary import PersonalSummary

class TestPersonalSummary(unittest.TestCase):

    def test_calculate_BMI(self):
        ps = PersonalSummary()

        #dummy variables
        ps.height = 170.0  # cm
        ps.weight = 70.0   # kg

        ps.calculate_BMI()

        #assertions
        expected_bmi = round(70 / (170 / 100) ** 2)
        self.assertEqual(ps.BMI, expected_bmi)
        self.assertIsNotNone(ps.BMI)
