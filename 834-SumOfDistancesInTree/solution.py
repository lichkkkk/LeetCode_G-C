class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        """
        Solution 1: DFS/BFS from each node. Because each DFS/BFS only goes through
            each node/edge once, so overall time complexity is O(N) * O(N) = O(N^2)
        Solution 2: DFS/BFS + cache table. The table stores the distance from node_i
            to node_j. The time complexity is still O(N^2).
        Solution 3: For each edge, actually we do not need to dive into it every time
            in DFS/BFS. We only need to know how many nodes are behind that edge and
            the sum of distance to reach those nodes from that edge. For each edge,
            we need to cache those info (i.e. #node & total distance) for both directions.
            The overall time complexity would be O(N). So this is actually a DP + DFS
            problem.
            
        Implementation version 1: 1524 ms, not very fast. Needs to be improved.
        """
        # First, let's make it easier to do node-edge lookup
        # cell[i] is a list of edges connected to node_i
        node_to_edges = [[] for i in range(n)]
        for i, [l_node, r_node] in enumerate(edges):
            node_to_edges[l_node].append(tuple(edges[i]))
            node_to_edges[r_node].append(tuple(reversed(edges[i])))

        # Second, let's build the edge-distance cache: <edge> -> <total_distance, #nodes>
        edge_distance_cache = {}
        def get_edge_distance_and_node_count(edge):
            if edge not in edge_distance_cache:
                total_distance, node_count = 0, 0
                for sub_edge in node_to_edges[edge[1]]:
                    if sub_edge == tuple(reversed(edge)):
                        continue
                    sub_distance, sub_count = get_edge_distance_and_node_count(sub_edge)
                    total_distance += sub_distance
                    node_count += sub_count
                node_count += 1
                total_distance += node_count
                edge_distance_cache[edge] = (total_distance, node_count)
            return edge_distance_cache[edge]

        # Thrid, compte the total distance
        res = [0] * n
        for node in range(n):
            for edge in node_to_edges[node]:
                _distance, _ = get_edge_distance_and_node_count(edge)
                res[node] += _distance
        return res
