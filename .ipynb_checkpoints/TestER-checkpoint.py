import unittest
from package.subpckg1.EnergyRequirements import EnergyRequirements

# class TestEnergyRequirements(unittest.TestCase):
#
#     @classmethod
#     def setUpClass(cls):
#         print("Setting up the test class.")
#         cls.test_client = EnergyRequirements()
#
#     @classmethod
#     def tearDownClass(cls):
#         print("Tearing down the test class.")
#         del cls.test_client
#
#     def setUp(self):
#         #initialize the EnergyRequirements object
#         self.energy_requirements = EnergyRequirements()
#
#         #set initial test data for each test
#         self.energy_requirements.name = "John"
#         self.energy_requirements.height = 175
#         self.energy_requirements.weight = 70
#         self.energy_requirements.age = 30
#         self.energy_requirements.gender = "M"
#
#     def tearDown(self):
#         pass
#
#     def test_calculate_TDEE_moderate_activity(self):
#         #manually assign activity level to "Moderately Active"
#         self.energy_requirements.activitylevel = "Moderately Active"
#
#         #call calculate_TDEE
#         print("Please enter Moderately Active for activity level")
#         self.energy_requirements.calculate_TDEE()
#
#         #calculate expected RMR
#         expected_RMR = (9.99 * self.energy_requirements.weight) + (6.25 * self.energy_requirements.height) - (4.92 * self.energy_requirements.age) + 5
#         expected_TDEE = expected_RMR * 1.55
#
#         #assertions
#         self.assertIsNotNone(self.energy_requirements.activitylevel)
#         self.assertEqual(self.energy_requirements.TDEE, expected_TDEE)
#         self.assertEqual(self.energy_requirements.RMR, expected_RMR)
#         self.assertEqual(self.energy_requirements.activitylevel, "Moderately Active")
#
#     def test_calculate_TDEE_sedentary_activity(self):
#         #manually assign the activity level to "Sedentary"
#         self.energy_requirements.activitylevel = "Sedentary"
#
#         #call calculate_TDEE
#         print("Please enter Sedentary for activity level")
#         self.energy_requirements.calculate_TDEE()
#
#         #calculate expected RMR first
#         expected_RMR = (9.99 * self.energy_requirements.weight) + (6.25 * self.energy_requirements.height) - (4.92 * self.energy_requirements.age) + 5
#         expected_TDEE = expected_RMR * 1.2
#
#         #assertions
#         self.assertIsNotNone(self.energy_requirements.activitylevel)
#         self.assertEqual(self.energy_requirements.TDEE, expected_TDEE)
#         self.assertEqual(self.energy_requirements.RMR, expected_RMR)
#         self.assertEqual(self.energy_requirements.activitylevel, "Sedentary")
#
#     def test_calculate_TDEE_very_activity(self):
#         #manually assign the activity level to "Very Active"
#         self.energy_requirements.activitylevel = "Very Active"
#
#         #call calculate_TDEE
#         print("Please enter Very Active for activity level")
#         self.energy_requirements.calculate_TDEE()
#
#         #calculate expected RMR first
#         expected_RMR = (9.99 * self.energy_requirements.weight) + (6.25 * self.energy_requirements.height) - (4.92 * self.energy_requirements.age) + 5
#         expected_TDEE = expected_RMR * 1.725
#
#         #assertions
#         self.assertIsNotNone(self.energy_requirements.activitylevel)
#         self.assertEqual(self.energy_requirements.TDEE, expected_TDEE)
#         self.assertEqual(self.energy_requirements.RMR, expected_RMR)
#         self.assertEqual(self.energy_requirements.activitylevel, "Very Active")


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
        # Initialize the EnergyRequirements object
        self.energy_requirements = EnergyRequirements()

    def tearDown(self):
        pass

    # Mock input for the entire test class
    @patch('builtins.input', side_effect=["John", "170", "70", "25", "M", "Moderately Active"])
    def test_calculate_TDEE_moderate_activity(self, mock_input):
        # Call the method to collect information using the mocked input
        self.energy_requirements.collect_info()
        
        # Now call calculate_TDEE
        self.energy_requirements.calculate_TDEE()

        # Manually calculate expected TDEE
        expected_RMR = (9.99 * self.energy_requirements.weight) + (6.25 * self.energy_requirements.height) - (4.92 * self.energy_requirements.age) + 5
        expected_TDEE = expected_RMR * 1.55  # For Moderately Active

        # Assertions
        self.assertEqual(self.energy_requirements.TDEE, expected_TDEE)
        self.assertEqual(self.energy_requirements.activitylevel, "Moderately Active")
        self.assertEqual(self.energy_requirements.name, "John")
        self.assertEqual(self.energy_requirements.age, 25)
        self.assertEqual(self.energy_requirements.height, 170)
        self.assertEqual(self.energy_requirements.weight, 70)
        self.assertEqual(self.energy_requirements.gender, "M")

    @patch('builtins.input', side_effect=["John", "170", "70", "25", "M", "Sedentary"])
    def test_calculate_TDEE_sedentary_activity(self, mock_input):
        # Call the method to collect information using the mocked input
        self.energy_requirements.collect_info()
        
        # Now call calculate_TDEE
        self.energy_requirements.calculate_TDEE()

        # Manually calculate expected TDEE
        expected_RMR = (9.99 * self.energy_requirements.weight) + (6.25 * self.energy_requirements.height) - (4.92 * self.energy_requirements.age) + 5
        expected_TDEE = expected_RMR * 1.2  # For Sedentary

        # Assertions
        self.assertEqual(self.energy_requirements.TDEE, expected_TDEE)
        self.assertEqual(self.energy_requirements.activitylevel, "Sedentary")

    @patch('builtins.input', side_effect=["John", "170", "70", "25", "M", "Very Active"])
    def test_calculate_TDEE_very_active(self, mock_input):
        # Call the method to collect information using the mocked input
        self.energy_requirements.collect_info()

        # Now call calculate_TDEE
        self.energy_requirements.calculate_TDEE()

        # Manually calculate expected TDEE
        expected_RMR = (9.99 * self.energy_requirements.weight) + (6.25 * self.energy_requirements.height) - (4.92 * self.energy_requirements.age) + 5
        expected_TDEE = expected_RMR * 1.725  # For Very Active

        # Assertions
        self.assertEqual(self.energy_requirements.TDEE, expected_TDEE)
        self.assertEqual(self.energy_requirements.activitylevel, "Very Active")






