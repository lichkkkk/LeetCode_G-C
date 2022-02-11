class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        stack = []
        for pos, h in enumerate(heights):
            while len(stack) > 0 and stack[-1][1] <= h:
                stack.pop()
            stack.append((pos, h))
        return [pos for pos,h in stack]
