#
# * Copyright (c) 2020 Graham Wall
# *
import Problem
import Solution
import DirectedGraph


# *
# * This class solves a problem on a directed graph with weighted edges to calculate the total distance of a route.
# *
# * @author Graham Wall
# *
# *
class RouteDistanceProblem(Problem.Problem):
    """Class specifying a distance problem on a directed graph"""

    def __init__(self, problem_number: int, directed_graph: DirectedGraph, route_vertex_list: list) -> Solution:
        """

        :rtype: Solution
        """
        assert directed_graph.get_num_vertices() > 0, \
            "DistanceProblem improperly specified: number of vertices must be > 0"
        assert directed_graph.get_num_edges() > 0, \
            "DistanceProblem improperly specified: number of edges must be > 0"
        assert len(route_vertex_list) > 1, \
            "DistanceProblem improperly specified: number of route vertices must be > 1"
        super().__init__(problem_number, directed_graph)
        self.route_vertex_list = route_vertex_list

    def solve(self):

        distance: int = 0
        # walk the edges connecting the vertices in the order specified
        #  if a route exists, return the distance walked, otherwise return "NO SUCH ROUTE"
        for index in range(len(self.route_vertex_list) - 1):
            vertex = self.route_vertex_list[index]
            if vertex not in self.directed_graph.get_vertices():
                raise ValueError('RouteDistanceProblem: unknown vertex in route list')
            next_vertex = self.route_vertex_list[index + 1]
            if next_vertex not in self.directed_graph.get_vertices():
                raise ValueError('RouteDistanceProblem: unknown vertex in route list')
            found_edge_for_next_vertex = False
            try:
                for edge in self.directed_graph.iter(vertex):
                    if edge.get_to_vertex() == next_vertex:
                        distance += edge.get_length()
                        found_edge_for_next_vertex = True
                        break
            except ValueError as e:
                # re-raise the exception from DirectedGraph
                raise e
            if not found_edge_for_next_vertex:
                solution = "NO SUCH ROUTE"
                return Solution.Solution(self.problem_number, solution)

        return Solution.Solution(self.problem_number, distance)
