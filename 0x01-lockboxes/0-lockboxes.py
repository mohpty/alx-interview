#!/usr/bin/python3
'''Alx-interviews Lockboxes'''


def dfs(current, graph, visited, total):
    for edge in graph[current]:
        if not visited[edge]:
            visited[edge] = 1
            total += 1
            if total == len(graph.keys()):
                return True
            return dfs(edge, graph, visited, total)
    return False


def canUnlockAll(boxes):
    '''Solving the lockboxes challenge'''

    # Store the graph
    graph = {}
    for i in range(len(boxes)):
        graph[i] = boxes[i]
    # create the visited array
    visited = [0 for i in range(len(boxes))]

    # traverse, mark, repeat
    return dfs(0, graph, visited, 1)
