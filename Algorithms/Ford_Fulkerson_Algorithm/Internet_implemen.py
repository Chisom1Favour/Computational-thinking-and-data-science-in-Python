class Fulkerson:
    def __init__(self, graph):
        """ Initializes thr Ford_Fulkerson Algorithm with a given graph.
            : param graph: 2D list representing the adjacency matrix of the network.
            graph[i][j] is the capacity of the edge from node i to node j."""
        self.graph = graph
        self.n = len(graph) # Number of routers (nodes) in the network
    def dfs(self, source, sink, parent, residual_graph):
        """
        Depth-First Search (DFS) to find an augumenting path from source to sink.
        :param source: The stating node (source router).
        :param sink: The destination node (sink router).
        :param parent: List to store the path, i.e, the parent of each node.
        :param residual graph: The residual graph showing available that shows available capacity.
        :return: True if an augumenting path is found, False otherwise."""
        visited = [False] * self.n
        stack = [source]
        visited[source] = True

        while stack:
            u = stack.pop()

            for v in range(self.n):
                # If there's available capacity and the node hasn't been visted yet
                if not visited[v] and residual_graph[u][v] > 0:
                    stack.append(v)
                    visited[v] = True
                    parent[v] = u
                    if v == sink: # Found an augumenting path to the sink
                        return True
        return False

    def ford_fulkerson(self, source, sink):
        """ The Ford-Fulkerson method to calcutae the maximum flow from source to snk.
        :param source: The starting node (source router).
        :param sink: The destination node (sink router).
        :return: The maximum flow from source to sink."""
        # Create a residual graph and initialize it as the same as the original graph
        residual_graph = [row[:] for row in self.graph]
        max_flow = 0 
        parent = [-1] * self.n  # To store the path from source to sink

        # Augument the flow while there's an augumenting path in the residual graph
        while self.dfs(source, sink, parent, residual_graph):
            # Find the minimun capacity in the augumenting path
            path_flow = float('Inf')
            s = sink

            while s != source:
                path_flow = min(path_flow, residual_graph[parent[s]][s])
                s = parent[s]

            # Update the residual capacities along the path
            v = sink
            while v != source:
                u = parent[v]
                residual_graph[u][v] -= path_flow # Reduce the forward capacity
                residual_graph[v][u] += path_flow # Increase the reverse capacity (back flow)
                v = parent[v]
            # Add the path flow to the total flow
            max_flow += flow
        return max_flow

# Example usage

