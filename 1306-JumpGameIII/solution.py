"""
1306. Jump Game III
licha@London, Apr. 2, 2020
"""
class Solution(object):
    def canReach(self, arr, start):
        """
        :type arr: List[int]
        :type start: int
        :rtype: bool
        """
        curr_level = set()
        curr_level.add(start)
        visited = set()
        while len(curr_level) > 0:
            next_level = set()
            for pos in curr_level:
                # Onlu need to reach ANY pos with value 0
                if (arr[pos] == 0):
                    return True
                visited.add(pos)
                next_pos_1, next_pos_2 = pos + arr[pos], pos - arr[pos]
                if next_pos_1 >= 0 and next_pos_1 < len(arr) and next_pos_1 not in visited:
                    next_level.add(next_pos_1)
                if next_pos_2 >= 0 and next_pos_2 < len(arr) and next_pos_2 not in visited:
                    next_level.add(next_pos_2)
            curr_level = next_level
        return False
