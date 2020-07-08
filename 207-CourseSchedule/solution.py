class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        unlock_dict = [[] for _ in range(numCourses)]
        blocker_cnt = [0] * numCourses
        for first, second in prerequisites:
            unlock_dict[second].append(first)
            blocker_cnt[first] += 1
        dq = deque([i for i in range(numCourses) if blocker_cnt[i] == 0])
        finished = 0
        while len(dq) > 0:
            course = dq.popleft()
            finished += 1
            for unlock in unlock_dict[course]:
                blocker_cnt[unlock] -= 1
                if blocker_cnt[unlock] == 0:
                    dq.append(unlock)
        return finished == numCourses
