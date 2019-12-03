from Lab6.GraphAL import GraphAL
from Lab6.GraphAM import GraphAM
from Lab6.DSF import DisjointSetForest

class Edge(object):
    def __init__(self, src, dest, weight):
        self.src = src
        self.dest = dest
        self.weight = weight

    def __repr__(self):
        return repr(self.src, self.dest, self.weight)


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
        # result_graph.am[edge.dest][edge.src] = edge.weight

    return result_graph


def al_kruskal():  # TODO

    return


def am_topological_sort():  # TODO
    return


def al_topological_sort():  # TODO:
    return


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