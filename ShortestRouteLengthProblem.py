#
# * Copyright (c) 2020 Graham Wall
# *
import Problem
import Solution
import DirectedGraph


# *
# * This class solves a problem on a directed graph with weighted edges to calculate the shortest length of a route
# *  between 2 vertices using Dijkstra's algorithm.
# *
# * Adapted from "Dijkstra's Algorithm", Wikipedia
# *
# * @author Graham Wall
# *
# *
class ShortestRouteLengthProblem(Problem.Problem):
    """Class specifying a distance problem on a directed graph"""

    def __init__(self, problem_number: int, directed_graph: DirectedGraph, begin_vertex: str,
                 end_vertex: str) -> Solution:
        """

        :rtype: Solution
        """
        assert directed_graph.get_num_vertices() > 0, \
            "DistanceProblem improperly specified: number of vertices must be > 0"
        assert directed_graph.get_num_edges() > 0, \
            "DistanceProblem improperly specified: number of edges must be > 0"
        assert (type(begin_vertex) is str) and (len(begin_vertex) > 0), \
            "NumberOfTripsProblem improperly specified: beginning vertex must be a non-empty string"
        assert begin_vertex in directed_graph.get_vertices(), \
            "NumberOfTripsProblem improperly specified: unknown beginning vertex"
        assert (type(end_vertex) is str) and (len(end_vertex) > 0), \
            "NumberOfTripsProblem improperly specified: ending vertex must be a non-empty string"
        assert end_vertex in directed_graph.get_vertices(), \
            "NumberOfTripsProblem improperly specified: unknown ending vertex"
        super().__init__(problem_number, directed_graph)
        self.begin_vertex = begin_vertex
        self.end_vertex = end_vertex

    def solve(self):
        # we need a concept of "infinity" but Python has no limit for integer infinity, so we calculate a value
        #  to use that will be large enough for the specified graph (larger than the sum of all its edges)
        max_length = 0
        for edge in self.directed_graph.get_edges():
            max_length = max_length + edge[0].get_length()
        max_length = max_length + 1
        shortest_path = [self.begin_vertex]
        shortest_distance: int = 0

        # implement Dijkstra's algorithm for finding shortest path between 2 nodes on a
        #  directed graph with positive weights

        # mark all nodes as unvisited
        unvisited_vertices = self.directed_graph.get_vertices()
        # assign "infinity" to each unvisited node for tentative distance
        tentative_distances = {vertex: max_length for vertex in unvisited_vertices}
        # except for the initial node, which we set to 0 for tentative distance
        tentative_distances[self.begin_vertex] = 0

        # consider all the neighbours of the current node and calculate the tentative distance through each node
        current_vertex = self.begin_vertex
        while len(unvisited_vertices) > 0:
            min_tentative_distance = max_length
            for edge in self.directed_graph.iter(current_vertex):
                neighbour = edge.get_to_vertex()
                if neighbour in unvisited_vertices:
                    tentative_distance = tentative_distances[current_vertex] + edge.get_length()
                    #  if the newly calculated tentative distance is less than the current tentative distance for
                    #  that node, update it with the lesser value
                    if tentative_distance < tentative_distances[neighbour]:
                        tentative_distances[neighbour] = tentative_distance
                    # keep a running total of the distance of the shortest path
                    if tentative_distances[neighbour] < min_tentative_distance:
                        min_tentative_distance = tentative_distances[neighbour]
                        min_tentative_distance_vertex = neighbour
            # remove this vertex from visited list unless we are calculating length of shortest cycle
            #   (beginning and ending vertices are the same)
            if not self.end_vertex == self.begin_vertex:
                unvisited_vertices.pop(unvisited_vertices.index(current_vertex))
            # visit the next unvisited node that has the shortest tentative distance
            current_vertex = min_tentative_distance_vertex
            # and update the shortest path to include it
            shortest_path.append(current_vertex)
            # since we are looking for just the shortest distance between beginning and ending vertices
            if current_vertex == self.end_vertex:
                break
            # check if we are done: shortest distance at this point is "infinity" (no path exists)
            if tentative_distances[current_vertex] >= max_length:
                break

        # remove redundant copies of the same path
        for index in range(len(shortest_path)-1):
            vertex = shortest_path[index]
            next_vertex = shortest_path[index+1]
            for edge in self.directed_graph.iter(vertex):
                if edge.get_to_vertex() == next_vertex:
                    shortest_distance = shortest_distance + edge.get_length()

        return Solution.Solution(self.problem_number, shortest_distance)
