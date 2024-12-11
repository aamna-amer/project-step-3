import unittest
from io import StringIO
from tabulate import tabulate
from package.subpckg1.PersonalSummary import PersonalSummary
from unittest.mock import patch

class TestPersonalSummary(unittest.TestCase):

    @patch('builtins.input', side_effect=['John', '170', '70', '25', 'M'])
    def test_collect_info(self, mock_input):
        # Create an instance of the class
        ps = PersonalSummary()

        # Call collect_info to "fake" the user input
        ps.collect_info()

        # Check that the information has been correctly assigned
        self.assertEqual(ps.name, 'John')
        self.assertEqual(ps.height, 170.0)
        self.assertEqual(ps.weight, 70.0)
        self.assertEqual(ps.age, 25)
        self.assertEqual(ps.gender, 'M')

    @patch('builtins.input', side_effect=['John', '170', '70', '25', 'M'])
    def test_calculate_BMI(self, mock_input):
        # Create an instance of the class
        ps = PersonalSummary()

        # Call collect_info to assign values
        ps.collect_info()

        # Call calculate_BMI
        ps.calculate_BMI()

        # Check that the BMI is calculated correctly
        self.assertEqual(ps.BMI, 24)  # BMI = 70 / (1.7 ** 2) -> 24

    
