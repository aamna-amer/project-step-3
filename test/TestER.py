import unittest
from package.subpckg1.EnergyRequirements import EnergyRequirements

class TestEnergyRequirements(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print("Setting up the test class.")
        cls.test_client = EnergyRequirements()  

    @classmethod
    def tearDownClass(cls):
        print("Tearing down the test class.")
        del cls.test_client  

    def setUp(self):
        #initialize the EnergyRequirements object
        self.energy_requirements = EnergyRequirements()

        #set initial test data for each test
        self.energy_requirements.name = "John"
        self.energy_requirements.height = 175  
        self.energy_requirements.weight = 70   
        self.energy_requirements.age = 30
        self.energy_requirements.gender = "M"

    def tearDown(self):
        pass

    def test_calculate_TDEE_moderate_activity(self):
        #manually assign activity level to "Moderately Active"
        self.energy_requirements.activitylevel = "Moderately Active"

        #call calculate_TDEE
        print("Please enter Moderately Active for activity level")
        self.energy_requirements.calculate_TDEE()

        #calculate expected RMR 
        expected_RMR = (9.99 * self.energy_requirements.weight) + (6.25 * self.energy_requirements.height) - (4.92 * self.energy_requirements.age) + 5
        expected_TDEE = expected_RMR * 1.55  

        #assertions
        self.assertIsNotNone(self.energy_requirements.activitylevel)
        self.assertEqual(self.energy_requirements.TDEE, expected_TDEE)
        self.assertEqual(self.energy_requirements.RMR, expected_RMR)  
        self.assertEqual(self.energy_requirements.activitylevel, "Moderately Active")

    def test_calculate_TDEE_sedentary_activity(self):
        #manually assign the activity level to "Sedentary"
        self.energy_requirements.activitylevel = "Sedentary"

        #call calculate_TDEE 
        print("Please enter Sedentary for activity level")
        self.energy_requirements.calculate_TDEE()

        #calculate expected RMR first
        expected_RMR = (9.99 * self.energy_requirements.weight) + (6.25 * self.energy_requirements.height) - (4.92 * self.energy_requirements.age) + 5
        expected_TDEE = expected_RMR * 1.2  

        #assertions 
        self.assertIsNotNone(self.energy_requirements.activitylevel)
        self.assertEqual(self.energy_requirements.TDEE, expected_TDEE)
        self.assertEqual(self.energy_requirements.RMR, expected_RMR)  
        self.assertEqual(self.energy_requirements.activitylevel, "Sedentary")
        
    def test_calculate_TDEE_very_activity(self):
        #manually assign the activity level to "Very Active"
        self.energy_requirements.activitylevel = "Very Active"

        #call calculate_TDEE
        print("Please enter Very Active for activity level")
        self.energy_requirements.calculate_TDEE()

        #calculate expected RMR first
        expected_RMR = (9.99 * self.energy_requirements.weight) + (6.25 * self.energy_requirements.height) - (4.92 * self.energy_requirements.age) + 5
        expected_TDEE = expected_RMR * 1.725

        #assertions
        self.assertIsNotNone(self.energy_requirements.activitylevel)
        self.assertEqual(self.energy_requirements.TDEE, expected_TDEE)
        self.assertEqual(self.energy_requirements.RMR, expected_RMR)  
        self.assertEqual(self.energy_requirements.activitylevel, "Very Active")

#unittest.main(argv=[''], verbosity=2, exit=False)