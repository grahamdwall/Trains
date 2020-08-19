from unittest import TestCase
import DirectedGraph
import NumberOfTripsProblem


class TestNumberOfTripsProblem(TestCase):
    def setUp(self):
        self.directed_graph = DirectedGraph.DirectedGraph()

        got_expected_assertion = False
        try:
            NumberOfTripsProblem.NumberOfTripsProblem(1, self.directed_graph, 'A', 'B', 1,
                                                      'CUMULATIVE_STOPS_UPPER_LIMIT')
        except AssertionError:
            got_expected_assertion = True
        if not got_expected_assertion:
            self.fail()

        self.directed_graph.add_directed_edge('A', 'B', 3)
        self.directed_graph.add_directed_edge('B', 'C', 2)
        self.directed_graph.add_directed_edge('C', 'A', 1)

        got_expected_assertion = False
        try:
            NumberOfTripsProblem.NumberOfTripsProblem(0, self.directed_graph, 'A', 'B', 1,
                                                      'CUMULATIVE_STOPS_UPPER_LIMIT')
        except AssertionError:
            got_expected_assertion = True
        if not got_expected_assertion:
            self.fail()

        got_expected_assertion = False
        try:
            NumberOfTripsProblem.NumberOfTripsProblem(1, self.directed_graph, 'A', 'B', -1,
                                                      'CUMULATIVE_STOPS_UPPER_LIMIT')
        except AssertionError:
            got_expected_assertion = True
        if not got_expected_assertion:
            self.fail()

        got_expected_assertion = False
        try:
            NumberOfTripsProblem.NumberOfTripsProblem(1, self.directed_graph, 'A', 1, 1, 'CUMULATIVE_STOPS_UPPER_LIMIT')
        except AssertionError:
            got_expected_assertion = True
        if not got_expected_assertion:
            self.fail()

        got_expected_assertion = False
        try:
            NumberOfTripsProblem.NumberOfTripsProblem(1, self.directed_graph, 'A', "", 1,
                                                      'CUMULATIVE_STOPS_UPPER_LIMIT')
        except AssertionError:
            got_expected_assertion = True
        if not got_expected_assertion:
            self.fail()

        got_expected_assertion = False
        try:
            NumberOfTripsProblem.NumberOfTripsProblem(1, self.directed_graph, "", 'B', 1,
                                                      'CUMULATIVE_STOPS_UPPER_LIMIT')
        except AssertionError:
            got_expected_assertion = True
        if not got_expected_assertion:
            self.fail()

        got_expected_assertion = False
        try:
            NumberOfTripsProblem.NumberOfTripsProblem(1, self.directed_graph, 'A', 'D', 1,
                                                      'CUMULATIVE_STOPS_UPPER_LIMIT')
        except AssertionError:
            got_expected_assertion = True
        if not got_expected_assertion:
            self.fail()

        got_expected_assertion = False
        try:
            NumberOfTripsProblem.NumberOfTripsProblem(1, self.directed_graph, 'D', 'B', 1,
                                                      'CUMULATIVE_STOPS_UPPER_LIMIT')
        except AssertionError:
            got_expected_assertion = True
        if not got_expected_assertion:
            self.fail()

        NumberOfTripsProblem.NumberOfTripsProblem(1, self.directed_graph, 'A', 'B', 0, 'EXACT_NUMBER_OF_STOPS')

        NumberOfTripsProblem.NumberOfTripsProblem(1, self.directed_graph, 'A', 'B', 0, 'CUMULATIVE_STOPS_UPPER_LIMIT')

    def test_solve(self):
        solution1 = NumberOfTripsProblem.NumberOfTripsProblem(1, self.directed_graph, 'C', 'C', 3,
                                                              'CUMULATIVE_STOPS_UPPER_LIMIT').solve()
        self.assertEqual(solution1.get_solution(), 1)

        solution2 = NumberOfTripsProblem.NumberOfTripsProblem(1, self.directed_graph, 'A', 'C', 4,
                                                              'EXACT_NUMBER_OF_STOPS').solve()
        self.assertEqual(solution2.get_solution(), 0)

        self.directed_graph.add_directed_edge('C', 'D', 1)
        self.directed_graph.add_directed_edge('D', 'E', 2)
        self.directed_graph.add_directed_edge('E', 'F', 3)
        self.directed_graph.add_directed_edge('F', 'C', 1)

        solution3 = NumberOfTripsProblem.NumberOfTripsProblem(1, self.directed_graph, 'A', 'A', 6,
                                                              'EXACT_NUMBER_OF_STOPS').solve()
        self.assertEqual(solution3.get_solution(), 1)

        solution4 = NumberOfTripsProblem.NumberOfTripsProblem(1, self.directed_graph, 'A', 'C', 6,
                                                              'CUMULATIVE_STOPS_UPPER_LIMIT').solve()
        self.assertEqual(solution4.get_solution(), 3)

        solution5 = NumberOfTripsProblem.NumberOfTripsProblem(1, self.directed_graph, 'A', 'C', 5,
                                                              'EXACT_NUMBER_OF_STOPS').solve()
        self.assertEqual(solution5.get_solution(), 1)

        solution6 = NumberOfTripsProblem.NumberOfTripsProblem(1, self.directed_graph, 'A', 'C', 2,
                                                              'EXACT_NUMBER_OF_STOPS').solve()
        self.assertEqual(solution6.get_solution(), 1)

        solution7 = NumberOfTripsProblem.NumberOfTripsProblem(1, self.directed_graph, 'A', 'C', 1,
                                                              'EXACT_NUMBER_OF_STOPS').solve()
        self.assertEqual(solution7.get_solution(), 0)
