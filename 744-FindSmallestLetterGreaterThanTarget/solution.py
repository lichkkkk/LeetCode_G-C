class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if letters[-1] <= target[0] or letters[0] > target[0]:
            return letters[0]
        l, r = 0, len(letters) - 1
        while l + 1 < r:
            mid = l + (r - l) // 2
            if letters[mid] > target[0]:
                r = mid
            else:
                l = mid
        return letters[r]
