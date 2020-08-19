from unittest import TestCase
import DirectedGraph
import ShortestRouteLengthProblem


class TestShortestRouteLengthProblem(TestCase):
    def setUp(self):
        self.directed_graph = DirectedGraph.DirectedGraph()

        got_expected_assertion = False
        try:
            ShortestRouteLengthProblem.ShortestRouteLengthProblem(1, self.directed_graph, 'A', 'B')
        except AssertionError:
            got_expected_assertion = True
        if not got_expected_assertion:
            self.fail()

        self.directed_graph.add_directed_edge('A', 'B', 3)
        self.directed_graph.add_directed_edge('B', 'C', 2)
        self.directed_graph.add_directed_edge('C', 'A', 1)

        got_expected_assertion = False
        try:
            ShortestRouteLengthProblem.ShortestRouteLengthProblem(0, self.directed_graph, 'A', 'B')
        except AssertionError:
            got_expected_assertion = True
        if not got_expected_assertion:
            self.fail()

        got_expected_assertion = False
        try:
            ShortestRouteLengthProblem.ShortestRouteLengthProblem(1, self.directed_graph, 'A', 1)
        except AssertionError:
            got_expected_assertion = True
        if not got_expected_assertion:
            self.fail()

        got_expected_assertion = False
        try:
            ShortestRouteLengthProblem.ShortestRouteLengthProblem(1, self.directed_graph, 'A', "")
        except AssertionError:
            got_expected_assertion = True
        if not got_expected_assertion:
            self.fail()

        got_expected_assertion = False
        try:
            ShortestRouteLengthProblem.ShortestRouteLengthProblem(1, self.directed_graph, 'A', 'D')
        except AssertionError:
            got_expected_assertion = True
        if not got_expected_assertion:
            self.fail()

        got_expected_assertion = False
        try:
            ShortestRouteLengthProblem.ShortestRouteLengthProblem(1, self.directed_graph, 1, 'B')
        except AssertionError:
            got_expected_assertion = True
        if not got_expected_assertion:
            self.fail()

        got_expected_assertion = False
        try:
            ShortestRouteLengthProblem.ShortestRouteLengthProblem(1, self.directed_graph, "", 'B')
        except AssertionError:
            got_expected_assertion = True
        if not got_expected_assertion:
            self.fail()

        got_expected_assertion = False
        try:
            ShortestRouteLengthProblem.ShortestRouteLengthProblem(1, self.directed_graph, 'D', 'B')
        except AssertionError:
            got_expected_assertion = True
        if not got_expected_assertion:
            self.fail()

        ShortestRouteLengthProblem.ShortestRouteLengthProblem(1, self.directed_graph, 'A', 'B')

    def test_solve(self):
        solution1 = ShortestRouteLengthProblem.ShortestRouteLengthProblem(1, self.directed_graph, 'A', 'C').solve()
        self.assertEqual(solution1.get_solution(), 5)

        solution2 = ShortestRouteLengthProblem.ShortestRouteLengthProblem(1, self.directed_graph, 'B', 'B').solve()
        self.assertEqual(solution2.get_solution(), 6)

        solution3 = ShortestRouteLengthProblem.ShortestRouteLengthProblem(1, self.directed_graph, 'C', 'C').solve()
        self.assertEqual(solution3.get_solution(), 6)

        self.directed_graph.add_directed_edge('C', 'D', 1)
        self.directed_graph.add_directed_edge('D', 'E', 2)
        self.directed_graph.add_directed_edge('E', 'F', 3)
        self.directed_graph.add_directed_edge('F', 'C', 1)

        solution4 = ShortestRouteLengthProblem.ShortestRouteLengthProblem(1, self.directed_graph, 'A', 'C').solve()
        self.assertEqual(solution4.get_solution(), 5)

        solution5 = ShortestRouteLengthProblem.ShortestRouteLengthProblem(1, self.directed_graph, 'B', 'B').solve()
        self.assertEqual(solution5.get_solution(), 6)

        solution6 = ShortestRouteLengthProblem.ShortestRouteLengthProblem(1, self.directed_graph, 'C', 'C').solve()
        self.assertEqual(solution6.get_solution(), 6)

        solution7 = ShortestRouteLengthProblem.ShortestRouteLengthProblem(1, self.directed_graph, 'A', 'F').solve()
        self.assertEqual(solution7.get_solution(), 11)
