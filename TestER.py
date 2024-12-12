
import unittest
from package.subpckg1.EnergyRequirements import EnergyRequirements

from unittest.mock import patch


class TestEnergyRequirements(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Setting up the test class for EnergyRequirements.")
        cls.test_client = EnergyRequirements()

    @classmethod
    def tearDownClass(cls):
        print("Tearing down the test class for EnergyRequirements.")
        del cls.test_client

    def setUp(self):
        self.energy_requirements = EnergyRequirements()

    def tearDown(self):
        pass

    #mock input
    @patch('builtins.input', side_effect=["John", "170", "70", "25", "M", "Moderately Active"])
    def test_calculate_TDEE_moderate_activity(self, mock_input):
        
        self.energy_requirements.collect_info()

        self.energy_requirements.calculate_TDEE()

        expected_RMR = (9.99 * self.energy_requirements.weight) + (6.25 * self.energy_requirements.height) - (4.92 * self.energy_requirements.age) + 5
        expected_TDEE = expected_RMR * 1.55  #moderately active

        self.assertEqual(self.energy_requirements.TDEE, expected_TDEE)
        self.assertEqual(self.energy_requirements.activitylevel, "Moderately Active")
        self.assertEqual(self.energy_requirements.name, "John")
        self.assertEqual(self.energy_requirements.age, 25)
        self.assertEqual(self.energy_requirements.height, 170)
        self.assertEqual(self.energy_requirements.weight, 70)
        self.assertEqual(self.energy_requirements.gender, "M")

    @patch('builtins.input', side_effect=["John", "170", "70", "25", "M", "Sedentary"])
    def test_calculate_TDEE_sedentary_activity(self, mock_input):
        
        self.energy_requirements.collect_info()

        self.energy_requirements.calculate_TDEE()

        expected_RMR = (9.99 * self.energy_requirements.weight) + (6.25 * self.energy_requirements.height) - (4.92 * self.energy_requirements.age) + 5
        expected_TDEE = expected_RMR * 1.2  #sedentary

        self.assertEqual(self.energy_requirements.TDEE, expected_TDEE)
        self.assertEqual(self.energy_requirements.activitylevel, "Sedentary")

    @patch('builtins.input', side_effect=["John", "170", "70", "25", "M", "Very Active"])
    def test_calculate_TDEE_very_active(self, mock_input):
        
        self.energy_requirements.collect_info()

        self.energy_requirements.calculate_TDEE()

        expected_RMR = (9.99 * self.energy_requirements.weight) + (6.25 * self.energy_requirements.height) - (4.92 * self.energy_requirements.age) + 5
        expected_TDEE = expected_RMR * 1.725  #very active

        self.assertEqual(self.energy_requirements.TDEE, expected_TDEE)
        self.assertEqual(self.energy_requirements.activitylevel, "Very Active")
