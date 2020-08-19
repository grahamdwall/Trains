from unittest import TestCase
import Solution


class TestSolution(TestCase):
    def setUp(self):
        got_expected_assertion = False
        try:
            Solution.Solution(0, "foo")
        except AssertionError as e:
            got_expected_assertion = True
        if not got_expected_assertion:
            self.fail()

        self.solution = Solution.Solution(1, "foo")

    def test_print(self):
        self.solution.print()
