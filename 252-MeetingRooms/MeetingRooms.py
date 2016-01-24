__author__ = 'liuxiyun'
# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.
#
# For example,
# Given [[0, 30],[5, 10],[15, 20]],
# return false.

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

#Idea:
# My idea is : first sort the intervals by the earlist start time
# Then go through all the interval in this order:
# # if the end time of the current interval is later than the start time of the next interval, then there is conflict, return False
# # if no comflict after finishing the loop, return True

# Time complexity: Sorting the requests takes O(n log n) time. check them takes O(n) time. Total: nlogn
# Test case: [], reversed order of intervals, [[1,3][3,5]], [[1,3],[2,4]]
class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        if intervals == []:
            return True
        intervals.sort(key = lambda x:x.start)
        for i in range(len(intervals) - 1):
            if intervals[i].end > intervals[i + 1].start:
                return False
        return True

# Follow up
# Given a few intervals, we want to attend the most number of meeting.
#
# Strategy: Greedy: always take the request with the earliest end time first.
# # Sort requests by the earliest end time
# # For each request in increasing order of end time:
# # # If the request does not conflict with the schedule Add the request to the schedule
# # # This works because if we were able to schedule any more requests instead of the one we choose, they would have an earlier end time.
# #
# Time Complexity:
# # Sorting the requests takes O(R log R) time. Iterating over them takes O(R) time.
# # Thus the whole algorithm takes O(R log R + R) = O​(R log R) t​ime.

class Solution(object):
    def mostAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        if intervals == []:
            return True
        intervals.sort(key = lambda x:x.end)
        res=[]
        res.append(intervals[0])
        for i in range(1, len(intervals)):
            if intervals[i].start > res[-1].end:
                res.append(intervals[i])
        return res