from TestER import TestEnergyRequirements
from TestG import TestGoals
from TestWorkout import TestWorkoutSchedule
from TestMacro import TestMacros
from TestPS import TestPersonalSummary
import unittest

def suite():
    suite = unittest.TestSuite()

    suite.addTest(unittest.makeSuite(TestPersonalSummary))
    suite.addTest(unittest.makeSuite(TestEnergyRequirements))
    suite.addTest(unittest.makeSuite(TestGoals))
    suite.addTest(unittest.makeSuite(TestWorkoutSchedule))
    suite.addTest(unittest.makeSuite(TestMacros))

    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())
