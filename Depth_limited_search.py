def limited_dfs(graph, node, goal, limit):

    if node == goal:
        return True

    if limit == 0:
        return False

    for nxt in graph[node]:
        if limited_dfs(graph, nxt, goal, limit-1):
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

print("DLS Result:", limited_dfs(graph,'A','F',3))
