#
# * Copyright (c) 2020 Graham Wall
# *


# *
# * This software solves "Problem One: Trains"
# *
# * @author Graham Wall
# *
# * A directed graph is specified, and a series of optimization problems are solved.
# *   The solution to each problem is output to the console.
# *
class DirectedEdge:
    """"Class representing a directed edge with a direction and a length"""

    def __init__(self, to_vertex, length):
        assert length > 0, "DirectedEdge improperly specified: edge length must be > 0"
        assert type(to_vertex) is str, "DirectedEdge improperly specified: to_vertex must be string"
        assert len(to_vertex) > 0, "DirectedEdge improperly specified: to_vertex must be string of length > 0"
        self.to_vertex = to_vertex
        self.length = length

    def get_to_vertex(self):
        return self.to_vertex

    def get_length(self):
        return self.length

    def print(self):
        print("\t" + self.to_vertex + str(self.length))
