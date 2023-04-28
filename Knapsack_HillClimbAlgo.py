
class Edge:
    def __init__(self,src,nbr,wt=None):
        self.src = src
        self.nbr = nbr
        self.wt = wt


def take_input():
    n = int(input("Enter number of edges: "))
    graph = [[] for _ in range(n)]
    num_edges = int(input("enter number of edges: "))
    for i in range(num_edges):
        src,nbr = map(int,input(f"Enter edges{i}: ").split())
        wt = int(input(f"Enter wt of the edge{i} (else if no wt press enter): ") or 0)
        graph[src].append(Edge(src,nbr,wt))
        graph[nbr].append(Edge(nbr,src,wt))

    return graph


def dfs(graph,start):
    open_list = [start]
    closed_list = set()

    while open_list:
        node = open_list.pop()
        if node not in closed_list:
            closed_list.add(node)
            for neighbor in graph[node]:
                nbr = neighbor.nbr
                if nbr not in open_list:
                    open_list.append(nbr)

    return closed_list
