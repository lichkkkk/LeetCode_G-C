class Solution:
    def kthCharacter(self, k: int) -> str:
        curr = 'a'
        while len(curr) < k:
            new_s = ''.join([chr((ord(c) - ord('a') + 1) % 26 + ord('a')) for c in curr])
            print(new_s)
            curr += new_s
        return curr[k-1]
