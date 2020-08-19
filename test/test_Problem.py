from unittest import TestCase
import DirectedGraph
import Problem


class TestProblem(TestCase):
    def setUp(self):
        directed_graph = DirectedGraph.DirectedGraph()

        got_expected_assertion = False
        try:
            Problem.Problem(-1, directed_graph)
        except AssertionError as e:
            got_expected_assertion = True
        if not got_expected_assertion:
            self.fail()

        got_expected_assertion = False
        try:
            Problem.Problem(1, directed_graph)
        except AssertionError as e:
            got_expected_assertion = True
        if not got_expected_assertion:
            self.fail()
