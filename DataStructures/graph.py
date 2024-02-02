# Adjacency Matrix
class Graph_Matrix:
    def __init__(self, num_vertices):
        self.graph = []
        for i in range(num_vertices):
            row = []
            for j in range(num_vertices):
                row.append(False)
            self.graph.append(row)

    def add_edge(self, u, v):
        self.graph[u][v] = True
        self.graph[v][u] = True

    def edge_exists(self, u, v):
        if u < 0 or u >= len(self.graph):
            return False
        if len(self.graph) == 0:
            return False
        row1 = self.graph[0]
        if v < 0 or v >= len(row1):
            return False
        return self.graph[u][v]

# Adjecency List  
class Graph_List:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u in self.graph.keys():
            self.graph[u].add(v)
        else:
            self.graph[u] = set(v)
        if v in self.graph.keys():
            self.graph[v].add(u)
        else:
            self.graph[v] = set([u])

    def edge_exists(self, u, v):
        if u in self.graph and v in self.graph:
            return (v in self.graph[u]) or (u in self.graph[v])
        return False
    
    def adjacent_nodes(self, node):
        return list(self.graph[node])
    
    def unconnected_vertices(self):
        unconnected = []
        for vertex, connections in self.graph.items():
            if not connections:
                unconnected.append(vertex)
        return unconnected
    
    # Breadth First Search (BFS) is an algorithm for traversing
    # or searching tree or graph data structures.
    # It starts at the tree root (or some arbitrary node of a graph), and
    # explores all of the neighbor nodes at the present depth before
    # moving on to the nodes at the next depth level.
    def breadth_first_search(self, v):
        visited = []
        to_visit = [v]
        while to_visit:
            visited.append(to_visit.pop(0))
            neighbors = sorted(self.graph[visited[-1]])
            for neighbor in neighbors:
                if neighbor not in visited and neighbor not in to_visit:
                    to_visit.append(neighbor)
        return visited
    
    # Depth First Search (DFS) is an algorithm for traversing or
    # searching tree or graph data structures. The algorithm starts
    # at the root node (selecting some arbitrary node as the root node
    # in the case of a graph) and explores as far as possible along
    # each branch before backtracking.
    def depth_first_search(self, start_vertex):
        visited = []
        self.depth_first_search_r(visited, start_vertex)
        return visited
    
    def depth_first_search_r(self, visited, current_vertex):
        visited.append(current_vertex)
        neighbors = sorted(self.graph[current_vertex])
        for neighbor in neighbors:
            if neighbor not in visited:
                self.depth_first_search_r(visited, neighbor)

    # Find the shortest path: Rather than traversing the entire graph,
    # we need to find the shortest path between two points in our graph
    # using BFS. This will allow players to quickly navigate between locations in the game.
    def bfs_path(self, start, end):
        visited = []
        to_visit = [start]
        path = {start: None}
        while to_visit:
            current_vertex = to_visit.pop(0)
            visited.append(current_vertex)
            if current_vertex == end:
                path_list = []
                while current_vertex is not None:
                    path_list.append(current_vertex)
                    current_vertex = path[current_vertex]
                path_list.reverse()
                return path_list
            
            sorted_neighbors = sorted(self.graph[current_vertex])
            for neighbor in sorted_neighbors:
                if neighbor not in visited and neighbor not in to_visit:
                    to_visit.append(neighbor)
                    path[neighbor] = current_vertex
        return None