import unittest
from math_quiz import generate_random_integer, select_random_operator, generate_math_problem

class TestMathGame(unittest.TestCase):

    def test_generate_random_integer(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test multiple values for thoroughness
            rand_num = generate_random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_select_random_operator(self):
        # Test if the operator returned is one of '+', '-', or '*'
        for _ in range(100):  # Test multiple times for consistency
            operator = select_random_operator()
            self.assertIn(operator, ['+', '-', '*'])

    def test_generate_math_problem(self):
        # Define test cases with number1, number2, operator, expected problem string, and expected answer
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (5, 2, '-', '5 - 2', 3),
            (5, 2, '*', '5 * 2', 10),
            (10, 5, '+', '10 + 5', 15),
            (10, 5, '-', '10 - 5', 5),
            (10, 5, '*', '10 * 5', 50),
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            problem_statement, answer = generate_math_problem(num1, num2, operator)
            self.assertEqual(problem_statement, expected_problem)
            self.assertEqual(answer, expected_answer)

if __name__ == "__main__":
    unittest.main()
 