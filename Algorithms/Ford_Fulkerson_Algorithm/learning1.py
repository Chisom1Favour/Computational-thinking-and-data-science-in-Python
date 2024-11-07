from collection import defaultdict

class Graph:
    def __init__(self, graph):
        self.graph = graph
        self.ROW = len(grapgh)
        # self.COL = len(gr[0])
    def BFS(self, s, t, parent):
        """Returns True if there is a path from source 's' to sink 't' in
            residual graph. Also fills parent[] to store the path."""
        visited = [False]*(self.ROW) # Mark all vertices as not visited.
        queue = [] # Create a queue for BFS
        queue.append(s)
        visited[s] = True

        while queue: # BFS loop
            u = queue.pop(0) # Dequeue a vertex from queue and print it
            # Get all adjacent vetices of the dequeued vertex u
            # If a adjacent has not been visited, then mark it
            # visited, and enqueue it.
            for ind, val in enumerate(self.graph[u]):
                if visited[ind] == False and val > 0:
                    # If we find a connection to the sink node,
                    # then there is no point in BFS anymore
                    # We just have to set its parent and can return true
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u
                    if ind == t:
                        return True
        # We didn't reach sink in BFS starting
        # from source, so return false
        return False

    def FordFulkerson(self, source, sink):
        """Returns the maximum flow from s to t in the given graph"""
        parent = [-1] * (self.ROW) # This array is filled by BFS and to store path
        max_flow = 0  # There is no flow initially
        while self.BFS(source, sink, parent):
            # Augument the flow while there is path from source to sink
            # Find minimal residual capacity of the edges along the 
            # path filled by BFS. Or we can say find the maximum flow
            # through the path found.
            path_flow = float("Inf")
            s = sink
            while (s != source):
                path_flow = min(path_flow, self,graph[parent[s]][s])
                s = parent[s]
                max_flow += path_flow  # Add path flow to overall flow
                # Update the residual capacities of the edges and reverse edges
                # along the path
                v = sink
                while (v != source):
                    u = parent[v]
                    self.graph[u][v] -= path_flow
                    self.graph[v][u] += path_flow
                    v = parent[v]
            return  max_flow
