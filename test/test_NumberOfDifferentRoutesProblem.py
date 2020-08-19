from unittest import TestCase
import DirectedGraph
import NumberOfDifferentRoutesProblem


class TestNumberOfDifferentRoutesProblem(TestCase):
    def setUp(self):
        self.directed_graph = DirectedGraph.DirectedGraph()

        got_expected_assertion = False
        try:
            NumberOfDifferentRoutesProblem.NumberOfDifferentRoutesProblem(1, self.directed_graph, 'A', 'B', 3)
        except AssertionError:
            got_expected_assertion = True
        if not got_expected_assertion:
            self.fail()

        self.directed_graph.add_directed_edge('A', 'B', 3)
        self.directed_graph.add_directed_edge('B', 'C', 2)
        self.directed_graph.add_directed_edge('C', 'A', 1)

        got_expected_assertion = False
        try:
            NumberOfDifferentRoutesProblem.NumberOfDifferentRoutesProblem(1, self.directed_graph, 'A', 'B', 0)
        except AssertionError:
            got_expected_assertion = True
        if not got_expected_assertion:
            self.fail()

        got_expected_assertion = False
        try:
            NumberOfDifferentRoutesProblem.NumberOfDifferentRoutesProblem(1, self.directed_graph, 'A', 'B', -1)
        except AssertionError:
            got_expected_assertion = True
        if not got_expected_assertion:
            self.fail()

        got_expected_assertion = False
        try:
            NumberOfDifferentRoutesProblem.NumberOfDifferentRoutesProblem(1, self.directed_graph, 'A', 'D', 3)
        except AssertionError:
            got_expected_assertion = True
        if not got_expected_assertion:
            self.fail()

        got_expected_assertion = False
        try:
            NumberOfDifferentRoutesProblem.NumberOfDifferentRoutesProblem(1, self.directed_graph, 'A', "", 3)
        except AssertionError:
            got_expected_assertion = True
        if not got_expected_assertion:
            self.fail()

        got_expected_assertion = False
        try:
            NumberOfDifferentRoutesProblem.NumberOfDifferentRoutesProblem(1, self.directed_graph, 'A', 1, 3)
        except AssertionError:
            got_expected_assertion = True
        if not got_expected_assertion:
            self.fail()

        got_expected_assertion = False
        try:
            NumberOfDifferentRoutesProblem.NumberOfDifferentRoutesProblem(1, self.directed_graph, 'D', 'B', 3)
        except AssertionError:
            got_expected_assertion = True
        if not got_expected_assertion:
            self.fail()

        got_expected_assertion = False
        try:
            NumberOfDifferentRoutesProblem.NumberOfDifferentRoutesProblem(1, self.directed_graph, "", 'B', 3)
        except AssertionError:
            got_expected_assertion = True
        if not got_expected_assertion:
            self.fail()

        got_expected_assertion = False
        try:
            NumberOfDifferentRoutesProblem.NumberOfDifferentRoutesProblem(1, self.directed_graph, 1, 'B', 3)
        except AssertionError:
            got_expected_assertion = True
        if not got_expected_assertion:
            self.fail()

        NumberOfDifferentRoutesProblem.NumberOfDifferentRoutesProblem(1, self.directed_graph, 'A', 'B', 3)

    def test_solve(self):
        solution0 = NumberOfDifferentRoutesProblem.NumberOfDifferentRoutesProblem(1, self.directed_graph, 'A', 'B', 1).solve()
        self.assertEqual(solution0.get_solution(), 0)

        solution1 = NumberOfDifferentRoutesProblem.NumberOfDifferentRoutesProblem(1, self.directed_graph, 'A', 'C', 5).solve()
        self.assertEqual(solution1.get_solution(), 0)

        solution2 = NumberOfDifferentRoutesProblem.NumberOfDifferentRoutesProblem(1, self.directed_graph, 'A', 'C', 30).solve()
        self.assertEqual(solution2.get_solution(), 1)

        solution3 = NumberOfDifferentRoutesProblem.NumberOfDifferentRoutesProblem(1, self.directed_graph, 'B', 'B', 1).solve()
        self.assertEqual(solution3.get_solution(), 0)

        solution4 = NumberOfDifferentRoutesProblem.NumberOfDifferentRoutesProblem(1, self.directed_graph, 'C', 'C', 2).solve()
        self.assertEqual(solution4.get_solution(), 0)

        self.directed_graph.add_directed_edge('C', 'D', 1)
        self.directed_graph.add_directed_edge('D', 'E', 2)
        self.directed_graph.add_directed_edge('E', 'F', 3)
        self.directed_graph.add_directed_edge('F', 'C', 1)

        solution5 = NumberOfDifferentRoutesProblem.NumberOfDifferentRoutesProblem(1, self.directed_graph, 'A', 'C', 30).solve()
        self.assertEqual(solution5.get_solution(), 9)

        solution6 = NumberOfDifferentRoutesProblem.NumberOfDifferentRoutesProblem(1, self.directed_graph, 'B', 'B', 30).solve()
        self.assertEqual(solution6.get_solution(), 15)

        solution7 = NumberOfDifferentRoutesProblem.NumberOfDifferentRoutesProblem(1, self.directed_graph, 'C', 'C', 30).solve()
        self.assertEqual(solution7.get_solution(), 16)

        solution8 = NumberOfDifferentRoutesProblem.NumberOfDifferentRoutesProblem(1, self.directed_graph, 'A', 'F', 30).solve()
        self.assertEqual(solution8.get_solution(), 8)
