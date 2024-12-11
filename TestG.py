
import unittest
from package.subpckg1.Goals import Goals

from unittest.mock import patch

class TestGoals(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Setting up the test class for Goals.")
        cls.test_client = Goals()  # Initialize the Goals object

    @classmethod
    def tearDownClass(cls):
        print("Tearing down the test class for Goals.")
        del cls.test_client  # Cleanup the test client

    def setUp(self):
        # Set initial test data
        self.test_client.name = "John"
        self.test_client.height = 170
        self.test_client.weight = 70
        self.test_client.age = 25
        self.test_client.gender = "M"
        self.test_client.activitylevel = "Moderately Active"  # Set activity level

    def tearDown(self):
        pass

    # Mock user input for the whole test method
    @patch('builtins.input', side_effect=["weight loss", "20", "90"])  # Mocking input for goal, weight loss, and timeline
    def test_goal_setting_loss(self, mock_input):
        # Call method without needing user input (we're setting the goal directly in the test)
        self.test_client.goal_setting()  # Assumed method to set the goal

        # Assertions
        self.assertIsNotNone(self.test_client.TDEE)  # Ensure TDEE is calculated
        self.assertEqual(self.test_client.goal, "weight loss")  # Ensure goal is set correctly
        self.assertEqual(self.test_client.weight_loss, 20)  # Ensure weight loss is set correctly
        self.assertEqual(self.test_client.timeline, 90)  # Ensure timeline is set correctly

    # Mocking input for goal, weight loss, and timeline
    @patch('builtins.input', side_effect=["weight loss", "30", "180"])  # Mocking user input for another test
    def test_caloric_change_loss(self, mock_input):
        # Set parameters again
        self.test_client.goal = "weight loss"
        self.test_client.weight_loss = 30
        self.test_client.timeline = 180

        # Call method and calculate caloric change
        caloric_change_value = self.test_client.caloric_change()  # Assuming this calculates and returns the caloric change

        # Assertions
        self.assertIsNotNone(caloric_change_value)  # Ensure caloric change is calculated
        self.assertEqual(round(caloric_change_value), -583)  # Ensure the caloric change is correct (rounded)

    # Mocking input for goal, weight loss, and timeline for caloric intake test
    @patch('builtins.input', side_effect=["weight loss", "50", "360"])  # Mocking input for goal, weight loss, and timeline
    def test_caloric_intake(self, mock_input):
        # Set parameters
        self.test_client.goal = "weight loss"
        self.test_client.weight_loss = 50
        self.test_client.timeline = 360
        self.test_client.TDEE = 2000  # Assuming TDEE is set manually or calculated earlier

        # Calculate caloric change first
        self.test_client.caloric_change()

        # Call caloric_intake method
        daily_caloric_intake = self.test_client.caloric_intake()  # Assuming this calculates the caloric intake based on caloric change

        # Assertions
        self.assertIsNotNone(daily_caloric_intake)  # Ensure daily caloric intake is calculated
        self.assertEqual(daily_caloric_intake, 1514)  # Ensure the intake is calculated correctly
