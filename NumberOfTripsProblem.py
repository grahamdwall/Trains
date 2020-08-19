#
# * Copyright (c) 2020 Graham Wall
# *
import Problem
import Solution
import DirectedGraph


# *
# * This class solves a problem on a directed graph with weighted edges
# *   to calculate the number of stops made on a trip with given constraints.
# *
# * @author Graham Wall
# *
# *
class NumberOfTripsProblem(Problem.Problem):
    """Class specifying a number of trips problem on a directed graph"""

    def __init__(self, problem_number: int, directed_graph: DirectedGraph, begin_vertex: str, end_vertex: str,
                 num_stops: int, constraint_type: str) -> Solution:
        """

        :rtype: Solution
        """
        assert directed_graph.get_num_vertices() > 0, \
            "NumberOfTripsProblem improperly specified: number of vertices must be > 0"
        assert directed_graph.get_num_edges() > 0, \
            "NumberOfTripsProblem improperly specified: number of edges must be > 0"
        assert num_stops >= 0, \
            "NumberOfTripsProblem improperly specified: number of stops must be >= 0"
        assert (type(begin_vertex) is str) and (len(begin_vertex) > 0), \
            "NumberOfTripsProblem improperly specified: beginning vertex must be a non-empty string"
        assert begin_vertex in directed_graph.get_vertices(), \
            "NumberOfTripsProblem improperly specified: unknown beginning vertex"
        assert (type(end_vertex) is str) and (len(end_vertex) > 0), \
            "NumberOfTripsProblem improperly specified: ending vertex must be a non-empty string"
        assert end_vertex in directed_graph.get_vertices(), \
            "NumberOfTripsProblem improperly specified: unknown ending vertex"
        assert (constraint_type == 'EXACT_NUMBER_OF_STOPS') or (constraint_type == 'CUMULATIVE_STOPS_UPPER_LIMIT'), \
            "NumberOfTripsProblem improperly specified: constraint type must be either " \
            "EXACT_NUMBER_OF_STOPS or CUMULATIVE_STOPS_UPPER_LIMIT"
        super().__init__(problem_number, directed_graph)
        self.begin_vertex = begin_vertex
        self.end_vertex = end_vertex
        self.num_stops = num_stops
        self.constraint_type = constraint_type

    def solve(self):
        # Walk all available edges for the required number of iterations,
        #   keeping track of all paths that terminate at the ending vertex
        # The number of edges we will walk is num_stops-1 since an edge connects 2 vertices
        num_trips_final_iteration: int = 0
        num_trips_cumulative: int = 0
        solution = 0
        # we build a list of lists, where each sublist is a series of vertices on the path
        paths = [[self.begin_vertex]]
        new_paths = []
        for iteration in range(self.num_stops):
            for path in paths:
                # get the last vertex in the path
                vertex = path[-1]
                # bifurcate each path for each additional new branch
                for edge in self.directed_graph.iter(vertex):
                    # deep copy path to new_path
                    new_path = []
                    for vertex in path:
                        new_path.append(vertex)
                    new_path.append(edge.get_to_vertex())
                    new_paths.append(new_path)
                    if iteration == self.num_stops - 1:
                        if new_path[-1] == self.end_vertex:
                            num_trips_final_iteration = num_trips_final_iteration + 1
                    if new_path[-1] == self.end_vertex:
                        num_trips_cumulative = num_trips_cumulative + 1
            # deep copy the new paths to paths
            paths.clear()
            for new_path in new_paths:
                paths.append(new_path)
            new_paths.clear()

        if self.constraint_type == 'EXACT_NUMBER_OF_STOPS':
            solution = num_trips_final_iteration
        if self.constraint_type == 'CUMULATIVE_STOPS_UPPER_LIMIT':
            solution = num_trips_cumulative

        return Solution.Solution(self.problem_number, solution)
