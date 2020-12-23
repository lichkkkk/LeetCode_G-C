# Dec. 24, 2020, London
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        up_edges = [(l, -1 * h, r) for l ,r, h in buildings]
        # set 1 for the second field such that it's always larger than up_edges
        down_edges = [(r, 1, None) for l ,r, h in buildings]
        edges = sorted(up_edges + down_edges, reverse=True)
        res = []
        curr_buildings = []
        while len(edges):
            curr_pos = edges[-1][0]
            while len(edges) and edges[-1][0] == curr_pos:
                curr_edge = edges.pop()
                if curr_edge[2] != None:
                    heapq.heappush(curr_buildings, (curr_edge[1], curr_edge[2]))
            # we do not need to remove all stale buildings, just those with highest heights
            while len(curr_buildings) and curr_buildings[0][1] <= curr_pos:
                heapq.heappop(curr_buildings)
            curr_height = -1 * curr_buildings[0][0] if len(curr_buildings) else 0
            if len(res) == 0 or curr_height != res[-1][1]:
                res.append([curr_pos, curr_height])
        return res
