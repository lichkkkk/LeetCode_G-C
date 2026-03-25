'''
this does not pass -- TLE

What we actually need is just a sorted list or balanced BST -- will redo

'''

import heapq
from collections import Counter

class Solution:

    def update_res(self, min_heap, removed_min, max_heap, removed_max, res):
        max_heap_size = len(max_heap) - removed_max.total()
        min_heap_size = len(min_heap) - removed_min.total()
        if min_heap_size == max_heap_size:
            res.append((min_heap[0] + max_heap[0])/2)
        elif min_heap_size > max_heap_size:
            res.append(min_heap[0])
        else:
            res.append(max_heap[0])

    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        res = []
        # initialize (can be optimized)
        min_heap = sorted(list(nums[:k]))
        max_heap = list(min_heap[:k//2])
        heapq.heapify_max(max_heap)
        min_heap = min_heap[k//2:]
        heapq.heapify(min_heap)
        removed_min, removed_max = Counter(), Counter()
        
        self.update_res(min_heap, removed_min, max_heap, removed_max, res)
        
        # calculate, move, udpate
        left, right = 0, k
        
        while right < len(nums):
            # print(max_heap, min_heap)
            # find and pop left
            if min_heap and nums[left] >= min_heap[0]:
                if nums[left] == min_heap[0]:
                    heapq.heappop(min_heap)
                else:
                    removed_min[nums[left]] += 1
            else:
                if nums[left] == max_heap[0]:
                    heapq.heappop_max(max_heap)
                else:
                    removed_max[nums[left]] += 1
            # insert the right
            if max_heap and nums[right] <= max_heap[0]:
                if removed_max[nums[right]] > 0:
                    removed_max[nums[right]] -= 1
                else:
                    heapq.heappush_max(max_heap, nums[right])
            else:
                if removed_min[nums[right]] > 0:
                    removed_min[nums[right]] -= 1
                else:
                    heapq.heappush(min_heap, nums[right])
            # re balance
            max_heap_size = len(max_heap) - removed_max.total()
            min_heap_size = len(min_heap) - removed_min.total()
            if max_heap_size > min_heap_size + 1:
                move_cnt = (max_heap_size - min_heap_size) // 2
                while move_cnt > 0:
                    num_to_move = heapq.heappop_max(max_heap)
                    if removed_max[num_to_move]:
                        removed_max[num_to_move] -= 1
                    else:
                        heapq.heappush(min_heap, num_to_move)
                        move_cnt -= 1
            if min_heap_size > max_heap_size + 1:
                move_cnt = (min_heap_size - max_heap_size) // 2
                while move_cnt > 0:
                    num_to_move = heapq.heappop(min_heap)
                    if removed_min[num_to_move]:
                        removed_min[num_to_move] -= 1
                    else:
                        heapq.heappush_max(max_heap, num_to_move)
                        move_cnt -= 1
            # clean heap top
            while max_heap and removed_max[max_heap[0]] > 0:
                removed_max[max_heap[0]] -= 1
                heapq.heappop_max(max_heap)
            while min_heap and removed_min[min_heap[0]] > 0:
                removed_min[min_heap[0]] -= 1
                heapq.heappop(min_heap)
            # update
            self.update_res(min_heap, removed_min, max_heap, removed_max, res)
            left += 1
            right += 1
        return res
