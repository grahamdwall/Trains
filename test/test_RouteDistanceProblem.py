from unittest import TestCase
import RouteDistanceProblem
import DirectedGraph


class TestRouteDistanceProblem(TestCase):
    def setUp(self):
        self.directed_graph = DirectedGraph.DirectedGraph()

        got_expected_assertion = False
        try:
            RouteDistanceProblem.RouteDistanceProblem(1, self.directed_graph, ['A', 'B', 'C'])
        except AssertionError:
            got_expected_assertion = True
        if not got_expected_assertion:
            self.fail()

        got_expected_assertion = False
        try:
            RouteDistanceProblem.RouteDistanceProblem(0, self.directed_graph, ['A', 'B', 'C'])
        except AssertionError:
            got_expected_assertion = True
        if not got_expected_assertion:
            self.fail()

        self.directed_graph.add_directed_edge('A', 'B', 3)
        self.directed_graph.add_directed_edge('B', 'C', 2)
        self.directed_graph.add_directed_edge('C', 'A', 1)

        got_expected_assertion = False
        try:
            RouteDistanceProblem.RouteDistanceProblem(1, self.directed_graph, ['A'])
        except AssertionError:
            got_expected_assertion = True
        if not got_expected_assertion:
            self.fail()

        got_expected_assertion = False
        try:
            RouteDistanceProblem.RouteDistanceProblem(1, self.directed_graph, [])
        except AssertionError:
            got_expected_assertion = True
        if not got_expected_assertion:
            self.fail()


        got_expected_assertion = False
        try:
            RouteDistanceProblem.RouteDistanceProblem(1, self.directed_graph, [])
        except AssertionError:
            got_expected_assertion = True
        if not got_expected_assertion:
            self.fail()

        self.route_distance_problem1 = RouteDistanceProblem.RouteDistanceProblem(1, self.directed_graph, ['A', 'B', 'C'])

    def test_solve(self):
        self.route_distance_problem1.solve()

        got_expected_exception = False
        try:
            RouteDistanceProblem.RouteDistanceProblem(1, self.directed_graph, ['A', "foo", 'C']).solve()
        except ValueError:
            got_expected_exception = True
        if not got_expected_exception:
            self.fail()

        got_expected_exception = False
        try:
            RouteDistanceProblem.RouteDistanceProblem(1, self.directed_graph, ['A', '', 'C']).solve()
        except ValueError:
            got_expected_exception = True
        if not got_expected_exception:
            self.fail()

        solution1 = RouteDistanceProblem.RouteDistanceProblem(1, self.directed_graph, ['A', 'B', 'C']).solve()
        self.assertEqual(solution1.get_solution(), 5)

        solution2 = RouteDistanceProblem.RouteDistanceProblem(1, self.directed_graph, ['A', 'B', 'A']).solve()
        self.assertEqual(solution2.get_solution(), "NO SUCH ROUTE")

        solution3 = RouteDistanceProblem.RouteDistanceProblem(1, self.directed_graph, ['A', 'B', 'C', 'A']).solve()
        self.assertEqual(solution3.get_solution(), 6)

