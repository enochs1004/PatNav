import heapq
import sys

class ShortestPath():
    """
    Function: Find the shortest way from start point to each other nodes. 
    """
    
    def __init__(self, graph=None):
        """
        graph: graph should be presented as dictionary type.
        distances: edge of each nodes 
        """
        self.inf = 100000
        self.graph = graph
        self.distances = {node: sys.maxsize for node in graph}
    
    def dijkstra(self, start=None):
        """
        start node should be set to "0" 
        start: set the start node to calculate each distance of nodes 
        The reason that set the heapq as (edge, node) is the alignment of heapq module is based on the first data, and minimum heap does not align as expected  when inserted in order (node, edge)
        """
        queue = []
        self.distances[start] = 0
        heapq.heappush(queue, (self.distances[start], start))

        while queue:
            """
            Find the shortest way of node and edge 
            1. Traversing distances from adjacent nodes on the target node
            2. Adds the distance from the current node to the adjacent node
            3. Change the distance of the node if the weight above the stored distance of the array is smaller
            4. Change if the weight is smaller than the distance stored in the array
            """
            current_distance, node = heapq.heappop(queue)
            if self.distances[node] < current_distance: 
                continue 

            for adjacency_node, distance in graph[node].items():
                weighted_distance = current_distance + distance
                if weighted_distance < self.distances[adjacency_node]:
                    self.distances[adjacency_node] = weighted_distance
                    heapq.heappush(queue, (weighted_distance, adjacency_node))

        seq = list(self.distances.keys())

        for i in range(len(self.distances)): 
          if int(self.distances[seq[i]]) > self.inf:
            self.distances[seq[i]] = "There is no connection between two nodes"

        return self.distances


if __name__ == "__main__":
    graph = {
    "1" : {"2":1, "4":2},
    "2" : {"3":2, "4":3},
    "3" : {"5":1},
    "4" : {"5":2},
    "5" : {"6":1},
    "6" : {"4":5}
    }

    sp = ShortestPath(graph=graph)
    result = sp.dijkstra(start="1")
    print(result)
