__author__ = 'liuxiyun'

# Follow up for H-Index: What if the citations array is sorted in ascending order? Could you optimize your algorithm?
# The basic idea of this solution is
# First reverse the list
# THen, use binary search to find the minimum index such that
# citations[index] >= index + 1

# After finding this index, the answer is index + 1.


# Time: O(log n)
# Space: O(1)

class Solution(object):

    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.reverse()
        if citations == [] or citations[0] == 0:
            return 0
        # print citations
        n = len(citations)
        start = 0 #always points to # of citation >= index+1
        end = n-1 #always points to # of citation < index+1
        if citations[start] < start + 1:# check start
            return start + 1
        if citations[end] >= end + 1:# check end
            return end + 1

        while start+1 < end:
            mid = (start+end)/2
            if citations[mid] == mid + 1:
                return mid + 1
            if citations[mid] > mid + 1:
                start = mid
            else:
                end = mid
        return start+1
        # return start+1 since start now points to last one whose # ofcitation >= index+1
# Test case
# [7,7,7,7,7,7,7]
# []
# [0,0,0,]
# [11,15]