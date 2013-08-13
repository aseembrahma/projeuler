import sys
from copy import copy
from time import time, sleep
from math import sqrt, floor, ceil

total = 0
debug = 0
all_data = list(set([x for x in open("keylog.txt").read().split('\n') if len(x) > 0]))
all_data = [map(int, list(x)) for x in all_data]
# Note [3,1,2] is graphed out as 3->1->2

def find_depth(n):
    #return 1+min([find_depth(x) for x in adjacency])
    pass

if __name__ == "__main__":
    time_start = time()
    limit = 1000
    limit_lower = 0
    total = 0
    
    #depths = [find_depth(x) for x in range(10)]
    #depths = 10*[None]
    #print adjacency_list
    #print inverse_adjacency_list
    
    adjacency_matrix = [10*[0] for x in range(10)]
    inverse_adjacency_matrix = [10*[0] for x in range(10)]
    adjacency_list = [set() for x in range(10)]
    inverse_adjacency_list = [set() for x in range(10)]
    for x in all_data:
        adjacency_matrix[x[0]][x[1]] = 1
        adjacency_matrix[x[1]][x[2]] = 1
        inverse_adjacency_matrix[x[1]][x[0]] = 1
        inverse_adjacency_matrix[x[2]][x[1]] = 1
        adjacency_list[x[0]].add(x[1])
        adjacency_list[x[1]].add(x[2])
        inverse_adjacency_list[x[1]].add(x[0])
        inverse_adjacency_list[x[2]].add(x[1])
    total_outgoing_links = [sum(x) for x in adjacency_matrix]
    total_incoming_links = [sum(x) for x in inverse_adjacency_matrix]
    total_graph_links = sum(total_outgoing_links)
    password = []
    node_queue = range(10)
    node_queue.sort(key=lambda x: sum(inverse_adjacency_matrix[x]))
    for i in range(10):
        if sum(inverse_adjacency_matrix[node_queue[i]]) > 0:
            node_queue = node_queue[:i]
            break
    
    while total_graph_links > 0:
        current_node = node_queue.pop(0)
        if total_outgoing_links[current_node] == 0 and total_incoming_links[current_node] == 0:
            continue
        password.append(current_node)
        for i in range(10):
            if adjacency_matrix[current_node][i] == 1:
                node_queue.append(i)
                adjacency_matrix[current_node][i] = 0
                inverse_adjacency_matrix[i][current_node] = 0
                total_graph_links = total_graph_links - 1
        node_queue = list(set(node_queue))
        node_queue.sort(key=lambda x: sum(inverse_adjacency_matrix[x]))
        if total_graph_links == 0:
            password.extend(node_queue)
    
    #    nodes.sort
    time_end = time()
    print "Answer:", ''.join([str(x) for x in password])
    print "Time taken", time_end-time_start
