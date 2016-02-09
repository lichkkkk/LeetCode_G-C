__author__ = 'liuxiyun'
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

# If unsorted, first sort the list
# Insert newInterval into it
# merge
# O(n) 92%

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        if intervals == []:
            return [newInterval]
        for i,interval in enumerate(intervals):
            if newInterval.start<=interval.start:
                intervals.insert(i,newInterval)
                break
        if newInterval.start>intervals[-1].start:
            intervals.append(newInterval)
        newList = []
        i=0
        while i<len(intervals):
            j=i
            start,end = intervals[i].start,intervals[i].end
            while j<len(intervals)-1 and end >= intervals[j+1].start: # COMPARE with end
                j+=1
                end = max(end,intervals[j].end) # UPDATE end
            newInt = Interval(start,end)
            newList.append(newInt)
            i=j+1 # UPDATE i
        return newList