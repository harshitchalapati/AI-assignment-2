def dfs_search(graph, start, target):

    visited = set()
    stack = [start]

    while stack:

        node = stack.pop()

        if node not in visited:

            print("Explored:", node)
            visited.add(node)

            if node == target:
                print("Target Found")
                return

            for child in graph[node]:
                stack.append(child)

graph = {
'A':['B','C'],
'B':['D','E'],
'C':['F'],
'D':[],
'E':[],
'F':[]
}

dfs_search(graph,'A','F')