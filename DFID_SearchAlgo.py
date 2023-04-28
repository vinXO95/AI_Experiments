from collections import deque


class Edge:
    def __init__(self, src, nbr, wt=None):
        self.src = src
        self.nbr = nbr
        self.wt = wt

    def __str__(self):
        if self.wt:
            return f"({self.src}, {self.nbr}, {self.wt})"
        return f"({self.src}, {self.nbr})"


def iddfs(graph, start, goal):
    depth = 0
    while True:
        result, closed = dls(graph, start, goal, depth)
        if result is not None:
            return result
        depth += 1


def dls(graph, start, goal, max_depth, open_list=None, closed_list=None):
    if open_list is None:
        open_list = []
    if closed_list is None:
        closed_list = set()
    print("\nMax Depth: ", max_depth)
    open_list.append((start, 0))
    while open_list:
        node, depth = open_list.pop()
        closed_list.add(node)
        if node == goal:
            print("*******Reached Goal state******")
            print("Open List: ", open_list)
            print("Closed List: ", closed_list)
            return node, closed_list
        if depth < max_depth:
            for neighbor in graph[node]:
                if neighbor.nbr not in closed_list:
                    open_list.append((neighbor.nbr, depth + 1))

    print("*** Goal NOT Found ********")
    print("Open List: ", open_list)
    print("Closed List: ", closed_list)

    return None, closed_list


def create_graph():
    num_vertices = int(input("Enter the number of vertices: "))
    graph = [[] for _ in range(num_vertices)]

    num_edges = int(input("Enter the number of edges: "))
    for i in range(num_edges):
        src, nbr = map(int, input(f"Enter edge {i}: ").split())
        wt = int(input(f"Enter weight for edge {i} (press enter if it has no weight): ") or 0)
        # so this is for undirected graph
        graph[src].append(Edge(src, nbr, wt))
        graph[nbr].append(Edge(nbr, src, wt))

    return graph


graph = create_graph()
goal = int(input("\nEnter goal state: "))
print(iddfs(graph, 0, goal))
