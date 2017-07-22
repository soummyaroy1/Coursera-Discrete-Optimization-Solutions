#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import numpy as np
from utils import parse_input, build_graph





def solve_it_trivial(node_count, edge_count, edges):
    """Return a trivial solution: every node gets its own color

    Parameters
    ---------
    node_count -- number of nodes
    edge_count -- number of edges
    edges      -- list (e_i1, e_i2) tuples representing edges

    Returns
    -------
    optimal     -- is this a proven optimal solution
    output_data -- string formatting of the solution as specified in the handout
    """
    optimal = 0
    solution = range(0, node_count)
    return (optimal, solution)


def solve_it_nontrivial(node_count, edge_count, edges):
    """
    """
    #Create the adjacency matrix representing the graph
    optimal = 1
    graph = build_graph(node_count, edge_count, edges)

    #Get the cardinalities sorted with corresponding row indices
    cardinalities = np.sum(graph, axis=1)
    cardinalities = [(i, int(cardinalities[i])) for i in range(len(cardinalities))]
    cardinalities.sort(key=lambda x: -x[1])

    #Create the colors array
    colors = [0] * node_count
    visited = [0] * node_count

    #Print out any information
    #print(edges)
    #print(graph)
    #print(colors)
    #print(cardinalities)


    #Begin with the most connected node
    #to follow first-fail principle
    for index, node in enumerate(cardinalities):
        row = node[0]
        visited[row] = 1

        #Get the list of unvisited neighbors
        #and sort their visitation order by their cardinality
        neighbors = [col for col in range(node_count) if graph[row, col] == 1 and visited[col] == 0]
        neighbors.sort(key = lambda x: np.sum(graph[x:]))

        #For each neighbor, find the maximal color of that neighbor's neighborss
        #and assign the neighbor max_color + 1
        for neighbor in neighbors:
            neighbors_neighbors = [col for col in range(node_count) if graph[neighbor, col] == 1]
            max_color = max([colors[neighbors_neighbor] for neighbors_neighbor in neighbors_neighbors])
            colors[neighbor] = max_color + 1

        #After updating for a particular node, print the resulting colors array
        print("Update result")
        print(row, neighbors, colors)
    print("Solution: " + str(colors))
    return (optimal, colors)






def solve_it(input_data):
    # Modify this code to run your optimization algorithm

    node_count, edge_count, edges = parse_input(input_data)

    #optimal, solution = solve_it_trivial(node_count, edge_count, edges)
    optimal, solution = solve_it_nontrivial(node_count, edge_count, edges)

    # prepare the solution in the specified output format
    output_data = str(len(set(solution))) + ' ' + str(optimal) + '\n'
    output_data += ' '.join(map(str, solution))

    return output_data




if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
        print(solve_it(input_data))
    else:
        print('This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/gc_4_1)')