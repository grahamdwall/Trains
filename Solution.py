#
# * Copyright (c) Graham Wall
# *


class Solution:
    """"Class representing a solution to an optimization problem specified on a directed weighted graph"""

    def __init__(self, problem_number: int, solution):
        assert problem_number > 0, "Solution improperly specified: problem number must be > 0"
        self.solution = solution
        self.problem_number = problem_number

    def get_solution(self):
        return self.solution

    def print(self):
        assert isinstance(self.problem_number, int)
        print("Output #{0}: {1}".format(str(self.problem_number), str(self.solution)))
