# Can be solved by both BFS & DFS
class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        res = 0
        def go_deeper(nl, depth):
            nonlocal res
            for ni in nl:
                if ni.isInteger():
                    res += ni.getInteger() * depth
                else:
                    go_deeper(ni.getList(), depth + 1)
        go_deeper(nestedList, 1)
        return res
