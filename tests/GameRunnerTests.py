import unittest
from src.GameRunner import get_board_params

class testGetBoardParams(unittest.TestCase):
    def testGetBoardParamsValidInput(self):
        expected_value = (5, 5, 5)
        observed_value = get_board_params(args=["GameRunner.py", "5", "5", "5"])
        self.assertEqual(expected_value, observed_value)

    def testGetBoardParamsTooManyInputs(self):
        expected_value = (None, None, None)
        observed_value = get_board_params(args=["GameRunner.py", "5", "5", "5", "5"])
        self.assertEqual(expected_value, observed_value)

    def testGetBoardParamsInvalidInput(self):
        expected_value = (None, None, None)
        observed_value = get_board_params(args=["GameRunner.py", "Not", "a", "number"])
        self.assertEqual(expected_value, observed_value)

    def testGetBoardParamsTooFewInputs(self):
        expected_value = (None, None, None)
        observed_value = get_board_params(args=["GameRunner.py"])
        self.assertEqual(expected_value, observed_value)


if __name__ == "__main__":
    unittest.main()