from collections import deque

def bfs_search(graph, start, goal):

    seen = set()
    q = deque([start])

    while q:

        current = q.popleft()

        if current in seen:
            continue

        print("Visited Node:", current)

        seen.add(current)

        if current == goal:
            print("Goal Node Found")
            return

        for n in graph[current]:
            q.append(n)

graph = {
'A':['B','C'],
'B':['D','E'],
'C':['F'],
'D':[],
'E':[],
'F':[]
}

bfs_search(graph,'A','F')