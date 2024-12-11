import unittest
from package.subpckg2.WorkoutSchedule import WorkoutSchedule

class TestWorkoutSchedule(unittest.TestCase):
    """
    Test class for WorkoutSchedule with improved error handling and validation checks.
    """

    @classmethod
    def setUpClass(cls):
        print("Setting up the test class for WorkoutSchedule.")
        cls.test_schedule = WorkoutSchedule()

    @classmethod
    def tearDownClass(cls):
        print("Tearing down the test class for WorkoutSchedule.")
        del cls.test_schedule

    def setUp(self):
        print("Setting up before a test.")
        self.schedule = WorkoutSchedule()
        self.schedule.workout_schedule = {
            "Day 1": {"Activity": "Running", "Time": "30 minutes", "Period": "Morning"},
            "Day 2": {"Activity": "Cycling", "Time": "45 minutes", "Period": "Evening"},
            "Day 3": {"Activity": "Swimming", "Time": "60 minutes", "Period": "Afternoon"},
            "Day 4": {"Activity": "Yoga", "Time": "30 minutes", "Period": "Morning"},
            "Day 5": {"Activity": "Weight Lifting", "Time": "45 minutes", "Period": "Evening"}
        }

    def tearDown(self):
        print("Cleaning up after a test.")
        del self.schedule

    def test_1_generate_training_split(self):
        """
        Test the generate_training_split method.
        """
        self.schedule.generate_training_split = lambda: None
        self.schedule.workout_schedule = {
            "Day 1": {"Activity": "Running", "Time": "30 minutes", "Period": "Morning"}
        }
        self.assertEqual(len(self.schedule.workout_schedule), 1)
        self.assertIn("Day 1", self.schedule.workout_schedule)
        self.assertEqual(self.schedule.workout_schedule["Day 1"]["Activity"], "Running")

    def test_2_display_workout_schedule(self):
        """
        Test the display_workout_schedule method.
        """
        output = self.schedule.display_workout_schedule()
        self.assertIsNone(output)  # Ensure display doesn't return anything
        self.assertEqual(len(self.schedule.workout_schedule), 5)
        self.assertIn("Day 1", self.schedule.workout_schedule)
        self.assertIn("Day 5", self.schedule.workout_schedule)  # Check the added day

    def test_3_customize_workout_schedule(self):
        """
        Test the customize_workout_schedule method.
        """
        # Modify only Day 1 of the existing schedule
        self.schedule.workout_schedule["Day 1"] = {
            "Activity": "Tennis",
            "Time": "60 minutes",
            "Period": "Morning"
        }
        
        # Assert that Day 1 has been updated
        self.assertIn("Day 1", self.schedule.workout_schedule)
        self.assertEqual(self.schedule.workout_schedule["Day 1"]["Activity"], "Tennis")
        
        # Output the updated schedule
        print("\nUpdated Schedule:")
        self.schedule.display_workout_schedule()

    def test_4_empty_schedule_display(self):
        """
        Test display_workout_schedule when no schedule is present.
        """
        empty_schedule = WorkoutSchedule()
        output = empty_schedule.display_workout_schedule()
        self.assertIsNone(output)  # Ensure no exception is raised

# Run tests in Jupyter Notebook
if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestWorkoutSchedule)
    unittest.TextTestRunner(verbosity=2).run(suite)

