#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict, deque
# Complete the findShortest function below.

#
# For the weighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] to <name>_to[i].
#
#
def bfs(start, adj_dict, color, visited, color_lookup):
    q = deque([(start, 0)])
    while len(q):
        node, distance = q.pop()
        for next_node in adj_dict[node]:
            if next_node not in visited:
                visited.add(next_node)
                if color_lookup[next_node] == color:
                    return distance+1, next_node
                q.appendleft((next_node, distance+1))
    return -1, None
def get_adj_dict(graph_nodes, graph_from, graph_to):
    adj_dict = defaultdict(list)
    for i, start in enumerate(graph_from):
        adj_dict[start].append(graph_to[i])
        adj_dict[graph_to[i]].append(start)
    return adj_dict
def get_color_lookup(ids):
    color_lookup = {}
    for i, color in enumerate(ids):
        color_lookup[i+1] = color
    return color_lookup

def findShortest(graph_nodes, graph_from, graph_to, ids, val):
    adj_dict = get_adj_dict(graph_nodes, graph_from, graph_to)
    color_lookup = get_color_lookup(ids)
    try:
        node = ids.index(val) + 1
    except:
        return -1
    visited = set([node])
    out = float('inf')
    while len(visited) < graph_nodes:
        x, node = bfs(node, adj_dict, val, visited, color_lookup)
        if x == -1:
            break
        elif x < out:
            out = x
    return -1 if out == float('inf') else out
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    graph_nodes, graph_edges = map(int, input().split())

    graph_from = [0] * graph_edges
    graph_to = [0] * graph_edges

    for i in range(graph_edges):
        graph_from[i], graph_to[i] = map(int, input().split())

    ids = list(map(int, input().rstrip().split()))

    val = int(input())

    ans = findShortest(graph_nodes, graph_from, graph_to, ids, val)

    fptr.write(str(ans) + '\n')

    fptr.close()

