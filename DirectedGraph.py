#
# * Copyright (c) 2020 Graham Wall
# *
import DirectedEdge


# *
# * This class implements a directed graph with weighted edges.
# *
# * @author Graham Wall
# *
# * Adapted from the "Adjacency Lists" approach from "Robert Sedgewick and Kevin Wayne, "Section 4.2 Directed Graphs"
#     in <i>Algorithms (4th Edition)</i>, Addison Wesley; (March 24, 2011)"
# *
class DirectedGraph:
    """Class representing a directed graph"""

    def __init__(self):
        self.num_edges = 0
        self.num_vertices = 0
        self.adjacent_edges = {}

    def get_num_vertices(self):
        return len(self.adjacent_edges.keys())

    def get_vertices(self):
        return list(self.adjacent_edges.keys())

    def get_num_edges(self):
        return len(self.adjacent_edges.values())

    def get_edges(self):
        return list(self.adjacent_edges.values())

    def add_directed_edge(self, from_vertex, to_vertex, length):
        assert type(from_vertex) is str, \
            "add_directed_edge():from_vertex improperly specified: from_vertex must be string"
        assert len(from_vertex) > 0, \
            "add_directed_edge():from_vertex improperly specified: from_vertex must be string of length > 0"
        try:
            # get list of outgoing edges already incident from this vertex, if any
            values = self.adjacent_edges[from_vertex]
            # add the new edge
            values.append(DirectedEdge.DirectedEdge(to_vertex, length))
            # save the update list
            self.adjacent_edges[from_vertex] = values
        except KeyError as e:
            # no edges yet adjacent to this vertex, add it to a new list
            self.adjacent_edges[from_vertex] = [DirectedEdge.DirectedEdge(to_vertex, length)]

    def get_path_length(self, vertex_list):
        # calculate length of path
        path_length = 0
        for index in range(len(vertex_list) - 1):
            vertex = vertex_list[index]
            next_vertex = vertex_list[index + 1]
            try:
                for edge in self.iter(vertex):
                    if edge.get_to_vertex() == next_vertex:
                        path_length = path_length + edge.get_length()
            except ValueError as e:
                # re-raise the exception from DirectedEdge
                raise e
        return path_length

    def print(self):
        for vertex in self.adjacent_edges.keys():
            print(vertex + "->")
            for edge in self.adjacent_edges[vertex]:
                edge.print()

    def iter(self, vertex):
        if vertex in list(self.adjacent_edges.keys()):
            return self.adjacent_edges[vertex]
        else:
            raise ValueError('DirectedGraph:iter() unknown vertex')
