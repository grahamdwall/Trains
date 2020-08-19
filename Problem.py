#
# * Copyright (c) 2020 Graham Wall
# *

# *
# * This class solves a generic problem on a directed graph with weighted edges.
# *
# * @author Graham Wall
# *
# *
class Problem:
    """Class specifying a generic problem on a directed graph"""
    def __init__(self, problem_number, directed_graph):
        assert problem_number > 0, "Problem improperly specified: problem number must be > 0"
        assert directed_graph.get_num_vertices() > 0, \
            "Problem improperly specified: number of vertices must be > 0"
        assert directed_graph.get_num_edges() > 0, "Problem improperly specified: number of edges must be > 0"
        self.problem_number = problem_number
        self.directed_graph = directed_graph
