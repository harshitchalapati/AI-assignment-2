def dls(graph, node, goal, depth):

    if node == goal:
        return True

    if depth <= 0:
        return False

    for nxt in graph[node]:
        if dls(graph, nxt, goal, depth-1):
            return True

    return False


def ids(graph, start, goal, max_depth):

    for level in range(max_depth + 1):

        if dls(graph, start, goal, level):
            return True

    return False


graph = {
'A':['B','C'],
'B':['D','E'],
'C':['F'],
'D':[],
'E':[],
'F':[]
}

print("IDS Result:", ids(graph,'A','F',5))