
import unittest
from package.subpckg1.Goals import Goals
from package.subpckg2.Macros import Macros

class TestMacros(unittest.TestCase):
    """
    Test class for Macros with improved error handling and validation checks.
    """

    @classmethod
    def setUpClass(cls):
        print("Setting up the test class for Macros.")
        cls.test_goals = Goals()
        cls.test_goals.daily_caloric_intake = 2000  # Mock a default daily caloric intake
        cls.test_macros = Macros(cls.test_goals)

    @classmethod
    def tearDownClass(cls):
        print("Tearing down the test class for Macros.")
        del cls.test_macros
        del cls.test_goals

    def test_1_calculate_macro_requirements(self):
        """
        Test the calculate_macro_requirements method.
        """
        macros = self.test_macros.calculate_macro_requirements()
        self.assertIsInstance(macros, dict)
        self.assertIn("Protein (g)", macros)
        self.assertIn("Carbs (g)", macros)
        self.assertIn("Fats (g)", macros)
        self.assertGreater(macros["Protein (g)"], 0)
        self.assertGreater(macros["Carbs (g)"], 0)
        self.assertGreater(macros["Fats (g)"], 0)

    def test_2_customize_macro_distribution(self):
        """
        Test the customize_macro_distribution method.
        """
        self.test_macros.custom_distribution = {
            "Protein": [30, 30, 30, 10],
            "Carbs": [40, 40, 10, 10],
            "Fats": [20, 20, 50, 10]
        }
        self.assertIsInstance(self.test_macros.custom_distribution, dict)
        self.assertEqual(sum(self.test_macros.custom_distribution["Protein"]), 100)
        self.assertEqual(sum(self.test_macros.custom_distribution["Carbs"]), 100)
        self.assertEqual(sum(self.test_macros.custom_distribution["Fats"]), 100)

    def test_3_generate_nutrition_plan(self):
        """
        Test the generate_nutrition_plan method.
        """
        self.test_macros.custom_distribution = {
            "Protein": [30, 30, 30, 10],
            "Carbs": [40, 40, 10, 10],
            "Fats": [20, 20, 50, 10]
        }
        self.test_macros.meal_ratios = [0.3, 0.3, 0.3, 0.1]
        self.test_macros.goals.daily_caloric_intake = 2000

        plan = self.test_macros.generate_nutrition_plan()
        self.assertIsNone(plan)  # Method does not return a value
        print("\nGenerated Nutrition Plan:")
        self.test_macros.generate_nutrition_plan()

    def test_4_ensure_goals_populated(self):
        """
        Test the ensure_goals_populated method.
        """
        self.test_macros.goals.daily_caloric_intake = None
        with self.assertRaises(ValueError):
            self.test_macros.ensure_goals_populated()
# Run tests in Jupyter Notebook
if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestMacros)
    unittest.TextTestRunner(verbosity=2).run(suite)
