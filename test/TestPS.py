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
