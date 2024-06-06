class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        res = []
        curr_start, curr_end = intervals[0]
        for i in range(1, len(intervals)):
          new_start, new_end = intervals[i]
          if new_start > curr_end:
            res.append([curr_start, curr_end])
            curr_start, curr_end = new_start, new_end
          else:
            curr_end = max(curr_end, new_end)
        res.append([curr_start, curr_end])
        return res

    def merge_wo_sort(self, intervals: List[List[int]]) -> List[List[int]]:
        mask = [0] * 10001
        zero_len_set = [0] * 10001
        for s, e in intervals:
          if s == e:
            zero_len_set[s] = 1
          else:
            mask[s] += 1
            mask[e] -= 1
        curr_start = None
        cnt = 0
        res = []
        for i in range(len(mask)):
          cnt += mask[i]
          if cnt > 0 and curr_start == None:
            curr_start = i
          elif cnt == 0 and curr_start != None:
            res.append([curr_start, i])
            curr_start = None
          elif cnt == 0 and curr_start == None and zero_len_set[i]:
            res.append([i, i])
        return res
