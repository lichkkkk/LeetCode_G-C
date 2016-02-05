__author__ = 'liuxiyun'

# Fill nums1 backward.
# Compare two ele from back to front, in each loop, choose the larger number added to l1.
# If there is no more element need to fill in num1 or num2, use another list to fill nums1

# Time: O(m+n)

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        i,j,k = m-1,n-1,m+n-1
        while i>=0 and j>=0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i-=1
            else:
                nums1[k] = nums2[j]
                j-=1
            k-=1
        while j>=0:
            nums1[k] = nums2[j]
            k-=1
            j-=1
# Test case:
# [1],1,[],0
# [1,0],1,[2],1
