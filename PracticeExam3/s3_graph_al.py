class Edge:
    def __init__(self, dest, weight=1):
        self.dest = dest
        self.weight = weight


class GraphAL:
    # Constructor
    def __init__(self, vertices, weighted=False, directed=False):
        self.al = [[] for i in range(vertices)]
        self.weighted = weighted
        self.directed = directed
        self.representation = 'AL'

    def is_valid_vertex(self, u):
        return 0 <= u < len(self.al)

    def insert_vertex(self):
        self.al.append([])

        return len(self.al) - 1  # Return id of new vertex

    def insert_edge(self, source, dest, weight=1):
        if not self.is_valid_vertex(source) or not self.is_valid_vertex(dest):
            print('Error, vertex number out of range')
        elif weight != 1 and not self.weighted:
            print('Error, inserting weighted edge to unweighted graph')
        else:
            self.al[source].append(Edge(dest, weight))
            if not self.directed:
                self.al[dest].append(Edge(source, weight))

    def delete_edge(self, source, dest):
        if source >= len(self.al) or dest >= len(self.al) or source < 0 or dest < 0:
            print('Error, vertex number out of range')
        else:
            deleted = self._delete_edge(source, dest)
            if not self.directed:
                deleted = self._delete_edge(dest, source)
            if not deleted:
                print('Error, edge to delete not found')

    def _delete_edge(self, source, dest):
        i = 0
        for edge in self.al[source]:
            if edge.dest == dest:
                self.al[source].pop(i)
                return True
            i += 1
        return False

    def num_vertices(self):
        return len(self.al)

    def vertices_reachable_from(self, src):
        reachable_vertices = set()

        for edge in self.al[src]:
            reachable_vertices.add(edge.dest)

        return reachable_vertices

    def is_identical(self, graph):

        if len(self.al) != len(graph.al):
            return False

        for i in range(len(self.al)):
            s1 = set()
            s2 = set()

            for edge in self.al[i]:
                s1.add(edge.dest)

            for edge in graph.al[i]:
                s2.add(edge.dest)

            if len(s1.intersection(s2)) != len(s1.union(s2)):
                return False

        return True

    # --------------------------------------------------------------------------------------------------------------
    # Problem 15
    # --------------------------------------------------------------------------------------------------------------
    def is_there_an_edge(self, src, dest):
        if not self.is_valid_vertex(src) or not self.is_valid_vertex(dest):
            return

        # Your code goes here

        return False

    # --------------------------------------------------------------------------------------------------------------
    # Problem 16
    # --------------------------------------------------------------------------------------------------------------
    def compute_out_degree(self, v):
        if not self.is_valid_vertex(v) or not self.is_valid_vertex(v):
            return

        out_degree_count = 0

        # Your code goes here

        return out_degree_count

    # --------------------------------------------------------------------------------------------------------------
    # Problem 17
    # --------------------------------------------------------------------------------------------------------------
    def is_isolated(self, v):
        if not self.is_valid_vertex(v) or not self.is_valid_vertex(v):
            return

        # Your code goes here

        return True

    # --------------------------------------------------------------------------------------------------------------
    # Problem 18
    # --------------------------------------------------------------------------------------------------------------
    @staticmethod
    def create_backward_circle_graph(n):
        if n < 3:  # n must be at least 3
            return

        graph = GraphAL(vertices=1234, weighted=False, directed=False)  # Feel free to modify this line

        # Your code goes here

        return graph
