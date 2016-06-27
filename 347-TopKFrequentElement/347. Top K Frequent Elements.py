__author__ = 'liuxiyun'
from collections import defaultdict
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if k == 0:
            return []
        res = []
        max_fre = 0
        num_to_fre = defaultdict(int)
        for num in nums:
            num_to_fre[num]+=1
            max_fre = max(num_to_fre[num],max_fre)
        print num_to_fre
        fre_to_num = [[] for x in xrange(max_fre)]
        print fre_to_num
        for num in num_to_fre.keys():
            fre_to_num[num_to_fre[num]-1].append(num) # same frequency
        print fre_to_num
        for i in range(max_fre-1,-1,-1):
            if fre_to_num[i]!=[] and k>0:
                for num in fre_to_num[i]:
                    if k>0:
                        res.append(num)
                        k-=1
                    else:
                        break
        return res
