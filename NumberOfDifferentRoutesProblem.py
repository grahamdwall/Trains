#
# * Copyright (c) 2020 Graham Wall
# *
import Problem
import Solution
import DirectedGraph


# *
# * This class solves a problem on a directed graph with weighted edges to
# *  calculate the number of unique round-trip routes
# *  from a beginning vertex to an ending vertex with distance of less than 30.
# *
# * @author Graham Wall
# *
# *
class NumberOfDifferentRoutesProblem(Problem.Problem):
    """Class specifying a distance problem on a directed graph"""
    def __init__(self, problem_number: int, directed_graph: DirectedGraph, begin_vertex: str, end_vertex: str,
                 max_distance: int) -> Solution:
        """

        :rtype: Solution
        """
        assert directed_graph.get_num_vertices() > 0, "NumberOfDifferentRoutesProblem improperly specified: " \
                                                      "number of vertices must be > 0"
        assert directed_graph.get_num_edges() > 0, "NumberOfDifferentRoutesProblem improperly specified: " \
                                                   "number of edges must be > 0"
        assert (type(begin_vertex) is str) and (len(begin_vertex) > 0), \
            "NumberOfTripsProblem improperly specified: beginning vertex must be a non-empty string"
        assert begin_vertex in directed_graph.get_vertices(), \
            "NumberOfTripsProblem improperly specified: unknown beginning vertex"
        assert (type(end_vertex) is str) and (len(end_vertex) > 0), \
            "NumberOfTripsProblem improperly specified: ending vertex must be a non-empty string"
        assert end_vertex in directed_graph.get_vertices(), \
            "NumberOfTripsProblem improperly specified: unknown ending vertex"
        assert max_distance > 0, "NumberOfDifferentRoutesProblem improperly specified: max_distance must be > 0"
        super().__init__(problem_number, directed_graph)
        self.begin_vertex = begin_vertex
        self.end_vertex = end_vertex
        self.max_distance = max_distance  # strictly less than max_distance

    def solve(self):
        number_of_routes: int = 0

        # Walk all available edges for the required number of iterations,
        #   keeping track of all paths that terminate at the ending vertex
        # The number of edges we will walk is num_stops-1 since an edge connects 2 vertices
        num_trips: int = 0
        # we build a list of lists, where each sublist is a series of vertices on the path
        paths = [[self.begin_vertex]]
        new_paths = []
        exhausted = False
        iteration = 0
        # we carry out an "exhaustive" or brute-force search for all paths of at least the maximum length
        #  that we will trim later
        while not exhausted:
            for path in paths:
                # grow each path that is less than max_distance
                if self.directed_graph.get_path_length(path) < self.max_distance:
                    min_path_length = self.max_distance
                    # get the last vertex in the path
                    vertex = path[-1]
                    for edge in self.directed_graph.iter(vertex):
                        # deep copy path to new_path
                        new_path = []
                        for vertex in path:
                            new_path.append(vertex)
                        new_path.append(edge.get_to_vertex())
                        # calculate length of new path
                        new_path_length = self.directed_graph.get_path_length(new_path)
                        if new_path_length < min_path_length:
                            min_path_length = new_path_length
                        new_paths.append(new_path)
                else:
                    new_paths.append(path)
            # deep copy the new paths to paths
            paths.clear()
            for new_path in new_paths:
                paths.append(new_path)
            new_paths.clear()
            # if we didn't add any new routes on this iteration, then all future paths will be longer than max length
            if min_path_length >= self.max_distance:
                exhausted = True
            iteration = iteration + 1

        # truncate vertices at the end of the paths that are not the specified ending vertex,
        #  and until length is less than max_distance
        new_paths = []
        for path in paths:
            new_start_index = 0
            for vertex in reversed(path):
                if not vertex == self.end_vertex:
                    new_start_index = new_start_index + 1
                else:
                    candidate_path_length = self.directed_graph.get_path_length(path[:len(path) - new_start_index])
                    if candidate_path_length < self.max_distance:
                        break
                    else:
                        new_start_index = new_start_index + 1
            path = path[:len(path) - new_start_index]
            # check if path is non-unique and has more than 1 vertex, and remember it if so
            path_found = False
            for new_path in new_paths:
                if new_path == path:
                    path_found = True
                    break
            if (not path_found) and (len(path) > 1):
                new_paths.append(path)
        number_of_routes = len(new_paths)

        return Solution.Solution(self.problem_number, number_of_routes)
