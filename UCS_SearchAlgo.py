from collections import deque
from queue import PriorityQueue


class Edge:
    def __init__(self, src, nbr, wt=None):
        self.src = src
        self.nbr = nbr
        self.wt = wt

    def __str__(self):
        if self.wt:
            return f"({self.src}, {self.nbr}, {self.wt})"
        return f"({self.src}, {self.nbr})"


def ucs(graph, start, goal):
    pq = PriorityQueue()
    pq.put((0, start))
    closed_list = set()
    # HERE Open list is PQ
    while not pq.empty():
        cost, node = pq.get()
        if node == goal:
            return node, closed_list
        if node not in closed_list:
            closed_list.add(node)
            for neighbor in graph[node]:
                if neighbor.nbr not in closed_list:
                    new_cost = cost + neighbor.wt
                    pq.put((new_cost,neighbor.nbr))
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
print(ucs(graph, 0, goal))
