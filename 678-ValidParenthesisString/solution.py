"""
678. Valid Parenthesis String
licha@London, Apr. 16, 2020
WARNING: This solution is not optimal, please check LeetCode discussion for a better O(n) approach
"""
class Solution:
    def checkValidString(self, s: str) -> bool:
        return self.helper(0, s, 0, [{} for i in range(len(s))])
    
    def helper(self, left_count, s, idx, cache):
        if idx == len(s):
            return left_count == 0
        if left_count in cache[idx]:
            return cache[idx][left_count]
        if s[idx] in '*(':
            if self.helper(left_count + 1, s, idx + 1, cache) == True:
                cache[idx][left_count] = True
                return True
        if s[idx] in '*)':
            if left_count > 0 and self.helper(left_count - 1, s, idx + 1, cache) == True :
                cache[idx][left_count] = True
                return True
        if s[idx] == '*':
            if self.helper(left_count, s, idx + 1, cache) == True:
                cache[idx][left_count] = True
                return True
        cache[idx][left_count] = False
        return False
        
