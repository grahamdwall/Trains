from unittest import TestCase
import DirectedEdge


class TestDirectedEdge(TestCase):
    def setUp(self):
        self.directed_edge0 = DirectedEdge.DirectedEdge('A', 1)

        got_expected_assertion = False
        try:
            self.directed_edge1 = DirectedEdge.DirectedEdge('B', 0)
        except AssertionError as e:
            got_expected_assertion = True
        if not got_expected_assertion:
            self.fail()

        got_expected_assertion = False
        try:
            self.directed_edge2 = DirectedEdge.DirectedEdge('C', -1)
        except AssertionError as e:
            got_expected_assertion = True
        if not got_expected_assertion:
            self.fail()

        self.directed_edge3 = DirectedEdge.DirectedEdge("foo", 1)

        got_expected_assertion = False
        try:
            self.directed_edge4 = DirectedEdge.DirectedEdge("", 1)
        except AssertionError as e:
            got_expected_assertion = True
        if not got_expected_assertion:
            self.fail()

        got_expected_assertion = False
        try:
            self.directed_edge5 = DirectedEdge.DirectedEdge(5, 1)
        except AssertionError as e:
            got_expected_assertion = True
        if not got_expected_assertion:
            self.fail()

    def test_get_to_vertex(self):
        self.assertGreater(len(self.directed_edge0.get_to_vertex()), 0)
        self.assertGreater(len(self.directed_edge3.get_to_vertex()), 0)

    def test_get_length(self):
        self.assertGreater(self.directed_edge0.get_length(), 0)
        self.assertGreater(self.directed_edge3.get_length(), 0)

    def test_print(self):
        self.directed_edge0.print()
