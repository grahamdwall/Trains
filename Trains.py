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

import DirectedGraph
import RouteDistanceProblem
import NumberOfTripsProblem
import ShortestRouteLengthProblem
import NumberOfDifferentRoutesProblem


def read_input_data(graph, input_file_name='inputdata.txt'):
    try:
        input_file = open(input_file_name, 'r')
    except FileNotFoundError as e:
        print(e)
        exit(1)
    if len(input_file.read()) > 0:
        input_file.seek(0)
        for line in input_file:
            fields_list = str.split(line, ',')
            if not len(fields_list) == 3:
                print("Incorrectly specified input file: use format: "'"[vertex name]"'", "'"[vertex name]"'", "
                      "[edge length] to specify a directed graph edge on each line of the text file"
                      " and where vertex name is a character string, and edge_length is a positive integer")
                input_file.close()
                exit(1)
            from_vertex = 0
            to_vertex = 0
            edge_length = 0
            for index in range(len(fields_list)):
                field = str.rstrip(str.lstrip(fields_list[index]))
                if index == 0:
                    try:
                        from_vertex = str(field)
                    except Exception as e:
                        print(e)
                if index == 1:
                    try:
                        to_vertex = str(field)
                    except Exception as e:
                        print(e)
                if index == 2:
                    try:
                        edge_length = int(field)
                    except Exception as e:
                        print(e)
            if (type(from_vertex) is str) and (len(from_vertex) > 0) and (type(to_vertex) is str) and \
                     (len(to_vertex) > 0) and (type(edge_length) is int) and (edge_length > 0):
                from_vertex = str.rstrip(str.lstrip(from_vertex, '"'), '"')
                to_vertex = str.rstrip(str.lstrip(to_vertex, '"'), '"')
                if (type(from_vertex) is str) and (len(from_vertex) > 0) and (type(to_vertex) is str) and \
                        (len(to_vertex) > 0) and (type(edge_length) is int) and (edge_length > 0):
                    graph.add_directed_edge(from_vertex, to_vertex, edge_length)
                else:
                    print("Incorrectly specified input file: use format: "'"[vertex name]"'", "'"[vertex name]"'", "
                          "[edge length] to specify a directed graph edge on each line of the text file"
                          " and where vertex name is a character string, and edge_length is a positive integer")
                    input_file.close()
                    exit(1)
            else:
                print("Incorrectly specified input file: use format: "'"[vertex name]"'", "'"[vertex name]"'", "
                      "[edge length] to specify a directed graph edge on each line of the text file"
                      " and where vertex name is a character string, and edge_length is a positive integer")
                input_file.close()
                exit(1)
    else:
        print("Incorrectly specified input file: use format: "'"[vertex name]"'", "'"[vertex name]"'", "
              "[edge length] to specify a directed graph edge on each line of the text file"
              " and where vertex name is a character string, and edge_length is a positive integer")
        input_file.close()
        exit(1)
    input_file.close()


if __name__ == "__main__":
    directed_graph = DirectedGraph.DirectedGraph()
    read_input_data(directed_graph)

    RouteDistanceProblem.RouteDistanceProblem(1, directed_graph, ['A', 'B', 'C']).solve().print()
    RouteDistanceProblem.RouteDistanceProblem(2, directed_graph, ['A', 'D']).solve().print()
    RouteDistanceProblem.RouteDistanceProblem(3, directed_graph, ['A', 'D', 'C']).solve().print()
    RouteDistanceProblem.RouteDistanceProblem(4, directed_graph, ['A', 'E', 'B', 'C', 'D']).solve().print()
    RouteDistanceProblem.RouteDistanceProblem(5, directed_graph, ['A', 'E', 'D']).solve().print()

    NumberOfTripsProblem.NumberOfTripsProblem(6, directed_graph, 'C', 'C', 3,
                                              'CUMULATIVE_STOPS_UPPER_LIMIT').solve().print()
    NumberOfTripsProblem.NumberOfTripsProblem(7, directed_graph, 'A', 'C', 4, 'EXACT_NUMBER_OF_STOPS').solve().print()

    ShortestRouteLengthProblem.ShortestRouteLengthProblem(8, directed_graph, 'A', 'C').solve().print()
    ShortestRouteLengthProblem.ShortestRouteLengthProblem(9, directed_graph, 'B', 'B').solve().print()

    NumberOfDifferentRoutesProblem.NumberOfDifferentRoutesProblem(10, directed_graph, 'C', 'C', 30).solve().print()
