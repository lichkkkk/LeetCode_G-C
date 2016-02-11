__author__ = 'liuxiyun'
# Idea: first, sort the intervals by earliest end time
# Everytime have a new meeting, check if there are available room based on the following rule:
# # if the start time is eariler than any end time of the intervals that currently running, this intervals need a new room
# # else: we can fit this interval into the available room. We choose the room with latest end time who still earlier than the start time of the current interval
# #       update the end time of this room.
# #       sort the end time in increasing order

# Time complexity: sort the intervals: n log n ; go through every interval: n ; in each loop, minheap keep the order in logn;
#                  In total: O(n log n)

import heapq
class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if intervals == []:
            return 0
        intervals.sort(key=lambda x : x.end)
        h = []
        for meet in intervals:
            if h==[] or meet.start<h[0]:
                heapq.heappush(h,meet.end)
            else:
                for endtime in reversed(h):
                    if endtime <= meet.start:
                        h.remove(endtime)
                        heapq.heappush(h,meet.end)
                        break
        return len(h)