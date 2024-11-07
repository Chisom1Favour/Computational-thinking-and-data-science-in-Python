""" Implentation of the Ford-Fulkerson algorithm that uses Depth First Search (DFS) to find augumenting paths. The code defines a flow network, finds, augumenting path, and auguments the flow until no more augumenting paths are found"""
class FordFulkerson:
    def __init__(self, graph):
        # Graph represented as an adjacency matrix
        self.graph = graph
        self.n = len(graph)

    def dfs(self, source, sink, parent, residual_graph):
        """Performs a DFS to find an augumenting path in the residual graph"""
        visited = [False] * self.n
        stack = [source]
        visited[source] = True

        while stack:
            u = stack.pop()

            for v in range(self.n):
                # If there's a path with available capacity and v is not defined
                if not visited[v] and residual_graph[u][v] > 0:
                    stack.append(v)
                    visited[v] = True
                    parent[v] = u
                    if v == sink:
                        return True
        return False

    def ford_fulkerson(self, source, sink):
        """Finds the maximum flow from source to sink in the graph"""
        # Create a residual graph and initialize it to be the same as original grap
        residual_graph = [row[:] for row in self.graph]
        # Initialize the maximum flow to 0
        max_flow = 0
        # This array will store the path from source to sink
        parent = [-1] * self.n
        # Augument the flow while there is an augumentiing path in the residual graph
        while self.dfs(source, sink, parent, residual_graph):
            # Find the maximum  flow in the path found by DFS
            path_flow = float('Inf')
            s = sink

            while s != source:
                path_flow = min(path_flow, residual_graph[parent[s]][s])
                s = parent[s]


            # Update the residual capacities of the edges and reverse edges
            v = sink
            while v != source:
                u = parent[v]
                residual_graph[u][v] -= path_flow
                residual_graph[v][u] += path_flow
                v = parent[v]

            # Add the flow of the current path to the total maximum flow
            max_flow += path_flow
        
        return max_flow


# Example usage
# Graph representattion as an adjacency matrix (capacities)

graph = [
    [0, 10, 5, 0, 0, 0],   # A -> B (10) A -> C (5)
    [0, 0, 15, 0, 0, 0],   # B -> C (15)
    [0, 0, 0, 10, 10, 0],  # C -> D (10), C -> E (10)
    [0, 0, 0, 0, 0, 10],   # D -> F (10)
    [0, 0, 0, 0, 0, 10],   # E -> F (10)
    [0, 0, 0, 0, 0, 0]     # F has no outgoing edges
    ]
#Create an instance of the FordFulkerson class
ff = FordFulkerson(graph)
#Call the ford-fulkerson method to find the maximum flow from source (0) to sink (5)
source = 0
sink = 5
max_flow = ff.ford_fulkerson(source, sink)
print(f"The maximum flow for source {source} to sink {sink} is : {max_flow}")
