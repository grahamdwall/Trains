from unittest import TestCase
import DirectedGraph
import Trains


class Test(TestCase):
    def test_read_input_data(self):

        directed_graph = DirectedGraph.DirectedGraph()

        Trains.read_input_data(directed_graph, "./../inputdata.txt")

        got_expected_exception = False
        try:
            Trains.read_input_data(directed_graph, "")
        except SystemExit:
            got_expected_exception = True
        if not got_expected_exception:
            self.fail()

        got_expected_exception = False
        try:
            Trains.read_input_data(directed_graph, "inputdata2.txt")
        except SystemExit:
            got_expected_exception = True
        if not got_expected_exception:
            self.fail()

        got_expected_exception = False
        try:
            Trains.read_input_data(directed_graph, "inputdata3.txt")
        except SystemExit:
            got_expected_exception = True
        if not got_expected_exception:
            self.fail()

        got_expected_exception = False
        try:
            Trains.read_input_data(directed_graph, "inputdata4.txt")
        except SystemExit:
            got_expected_exception = True
        if not got_expected_exception:
            self.fail()

        Trains.read_input_data(directed_graph, "inputdata5.txt")

        got_expected_exception = False
        try:
            Trains.read_input_data(directed_graph, "inputdata6.txt")
        except SystemExit:
            got_expected_exception = True
        if not got_expected_exception:
            self.fail()
