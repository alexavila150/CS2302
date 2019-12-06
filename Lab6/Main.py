from Lab6.GraphAL import GraphAL
from Lab6.GraphAM import GraphAM
from Lab6.DSF import DisjointSetForest


class Edge(object):
    def __init__(self, src, dest, weight):
        self.src = src
        self.dest = dest
        self.weight = weight

    def __repr__(self):
        return repr((self.src, self.dest, self.weight))


def am_kruskal(graph: GraphAM):  # TODO
    # get edges and sort them by weight
    edges = list()
    for i in range(len(graph.am)):
        for j in range(len(graph.am[i])):
            if graph.am[i][j] != 0:
                edges.append(Edge(i, j, graph.am[i][j]))

    # put less weighted edges on the result_edges list
    edges = sorted(edges, key=lambda edge: edge.weight)
    dsf = DisjointSetForest(len(graph.am))
    result_edges = set()
    for i in range(len(edges)):
        if dsf.find(edges[i].dest) != dsf.find(edges[i].src):
            result_edges.add(edges[i])
            dsf.union(edges[i].src, edges[i].dest)

    # convert resultant edges into a graph
    result_graph = GraphAM(len(graph.am), graph.weighted, graph.directed)
    for edge in result_edges:
        result_graph.insert_edge(edge.dest, edge.src, edge.weight)

    return result_graph


def al_kruskal(graph: GraphAL):  # TODO
    # get edges and sort them by weight
    edges = list()
    for i in range(len(graph.al)):
        for j in range(len(graph.al[i])):
            if graph.al[i][j] != 0:
                edges.append(Edge(i, graph.al[i][j].dest, graph.al[i][j].weight))

    # put less weighted edges on the result_edges list
    edges = sorted(edges, key=lambda edge_al: edge_al.weight)
    dsf = DisjointSetForest(len(graph.al))
    result_edges = set()
    for i in range(len(edges)):
        if dsf.find(edges[i].dest) != dsf.find(edges[i].src):
            result_edges.add(edges[i])
            dsf.union(edges[i].src, edges[i].dest)

    # convert resultant edges into a graph
    result_graph = GraphAL(len(graph.al), graph.weighted, graph.directed)
    for edge in result_edges:
        result_graph.insert_edge(edge.src, edge.dest, edge.weight)

    return result_graph


def topological_sort(graph):  # TODO
    all_in_degrees = graph.compute_indegree_every_vertex()
    sort_result = []

    queue = []

    for i in range(len(all_in_degrees)):
        if all_in_degrees[i] == 0:
            queue.insert(0, i)

    while len(queue) != 0:
        u = queue.pop()

        sort_result.append(u)

        for adj_vertex in graph.get_adjacent_vertices(u):
            all_in_degrees[adj_vertex] -= 1

            if all_in_degrees[adj_vertex] == 0:
                queue.insert(0, adj_vertex)

    if len(sort_result) != graph.num_vertices():
        return None

    return sort_result

#######################################################################
#                        AM_Kruskal Test
#######################################################################


my_graph = GraphAM(vertices=5, directed=False, weighted=True)
my_graph.insert_edge(0, 1, 10)
my_graph.insert_edge(0, 2, 5)
my_graph.insert_edge(0, 4, 7)
my_graph.insert_edge(1, 2, 9)
my_graph.insert_edge(2, 4, 2)
my_graph.insert_edge(2, 3, 6)
my_graph.insert_edge(3, 4, 1)

result_graph = am_kruskal(my_graph)
print(result_graph.am)

#######################################################################
#                        AL_Kruskal Test
#######################################################################

my_graph = GraphAL(vertices=5, directed=False, weighted=True)
my_graph.insert_edge(0, 1, 10)
my_graph.insert_edge(0, 2, 5)
my_graph.insert_edge(0, 4, 7)
my_graph.insert_edge(1, 2, 9)
my_graph.insert_edge(2, 4, 2)
my_graph.insert_edge(2, 3, 6)
my_graph.insert_edge(3, 4, 1)

result_graph = al_kruskal(my_graph)
result_graph.display()

#######################################################################
#                        Topological Sort Test
#######################################################################
print("")
print("TOPOLOGICAL SORT")
my_graph = GraphAM(6, directed=True, weighted=False)
my_graph.insert_edge(0, 1)
my_graph.insert_edge(0, 4)
my_graph.insert_edge(1, 2)
my_graph.insert_edge(2, 3)
my_graph.insert_edge(4, 1)
my_graph.insert_edge(4, 5)
my_graph.insert_edge(5, 3)

sort_result = topological_sort(my_graph)
print(sort_result)

my_graph = GraphAL(6, directed=True, weighted=False)
my_graph.insert_edge(0, 1)
my_graph.insert_edge(0, 4)
my_graph.insert_edge(1, 2)
my_graph.insert_edge(2, 3)
my_graph.insert_edge(4, 1)
my_graph.insert_edge(4, 5)
my_graph.insert_edge(5, 3)

sort_result = topological_sort(my_graph)
print(sort_result)