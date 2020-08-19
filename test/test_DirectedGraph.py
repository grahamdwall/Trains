from unittest import TestCase
import DirectedGraph


class TestDirectedGraph(TestCase):
    def setUp(self):
        self.directed_graph = DirectedGraph.DirectedGraph()
        self.directed_graph.add_directed_edge('A', 'B', 1)
        self.directed_graph.add_directed_edge('B', "foo", 2)
        self.directed_graph.add_directed_edge("foo", 'A', 3)

        got_expected_assertion = False
        try:
            self.directed_graph.add_directed_edge(5, 'A', 0)
        except AssertionError as e:
            got_expected_assertion = True
        if not got_expected_assertion:
            self.fail()

        got_expected_assertion = False
        try:
            self.directed_graph.add_directed_edge("", 'A', -1)
        except AssertionError as e:
            got_expected_assertion = True
        if not got_expected_assertion:
            self.fail()

    def test_get_num_vertices(self):
        self.assertEqual(self.directed_graph.get_num_vertices(), 3)

    def test_get_vertices(self):
        self.assertEqual(len(self.directed_graph.get_vertices()), 3)

    def test_get_num_edges(self):
        self.assertEqual(self.directed_graph.get_num_edges(), 3)

    def test_get_edges(self):
        self.assertEqual(len(self.directed_graph.get_edges()), 3)

    def test_add_directed_edge(self):
        # tested in test setUp
        pass

    def test_get_path_length(self):
        path_length0 = self.directed_graph.get_path_length([])
        self.assertEqual(path_length0, 0)

        got_expected_exception = False
        try:
            self.directed_graph.get_path_length(["bar", "foo"])
        except ValueError as e:
            got_expected_exception = True
        if not got_expected_exception:
            self.fail()

        path_length2 = self.directed_graph.get_path_length(['A', 'A'])
        self.assertEqual(path_length2, 0)

        path_length3 = self.directed_graph.get_path_length(['A', "foo"])
        self.assertEqual(path_length3, 0)

        path_length4 = self.directed_graph.get_path_length(['A', 'B', "foo"])
        self.assertEqual(path_length4, 3)

        path_length5 = self.directed_graph.get_path_length(['A', 'B', "foo", 'A'])
        self.assertEqual(path_length5, 6)

    def test_iter(self):
        count = 0
        for edge in self.directed_graph.iter("foo"):
            count = count + 1
        self.assertEqual(count, 1)

        got_expected_exception = False
        try:
            self.directed_graph.iter("bar")
        except ValueError as e:
            got_expected_exception = True
        if not got_expected_exception:
            self.fail()

    def test_print(self):
        self.directed_graph.print()
