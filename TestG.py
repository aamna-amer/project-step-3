
import unittest
from package.subpckg1.Goals import Goals

from unittest.mock import patch

class TestGoals(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Setting up the test class for Goals.")
        cls.test_client = Goals()  

    @classmethod
    def tearDownClass(cls):
        print("Tearing down the test class for Goals.")
        del cls.test_client  

    def setUp(self):
        #set initial data
        self.test_client.name = "John"
        self.test_client.height = 170
        self.test_client.weight = 70
        self.test_client.age = 25
        self.test_client.gender = "M"
        self.test_client.activitylevel = "Moderately Active"  

    def tearDown(self):
        pass

    #mock input
    @patch('builtins.input', side_effect=["weight loss", "20", "90"])  
    def test_goal_setting_loss(self, mock_input):
      
        self.test_client.goal_setting()  

        self.assertIsNotNone(self.test_client.TDEE)  
        self.assertEqual(self.test_client.goal, "weight loss")  
        self.assertEqual(self.test_client.weight_loss, 20)  
        self.assertEqual(self.test_client.timeline, 90)  

    #mock input
    @patch('builtins.input', side_effect=["weight loss", "30", "180"])  
    def test_caloric_change_loss(self, mock_input):
       
        self.test_client.goal = "weight loss"
        self.test_client.weight_loss = 30
        self.test_client.timeline = 180

        caloric_change_value = self.test_client.caloric_change()  

        self.assertIsNotNone(caloric_change_value)  
        self.assertEqual(round(caloric_change_value), -583)  

    #mock input
    @patch('builtins.input', side_effect=["weight loss", "50", "360"])  
    def test_caloric_intake(self, mock_input):
        
        self.test_client.goal = "weight loss"
        self.test_client.weight_loss = 50
        self.test_client.timeline = 360
        self.test_client.TDEE = 2000  

        self.test_client.caloric_change()

        daily_caloric_intake = self.test_client.caloric_intake()  

        self.assertIsNotNone(daily_caloric_intake)  
        self.assertEqual(daily_caloric_intake, 1514)  
