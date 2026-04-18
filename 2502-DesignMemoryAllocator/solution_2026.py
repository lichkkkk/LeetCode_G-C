# TODO - implement a better solution

class Allocator:

    def __init__(self, n: int):
        self.m = [0] * n

    def allocate(self, size: int, mID: int) -> int:
        free_cnt = 0
        for i in range(len(self.m)):
            if self.m[i] != 0:
                if free_cnt == 0:
                    continue
                else:
                    if free_cnt >= size:
                        free_start = i - free_cnt
                        self.m[free_start : free_start + size] = [mID] * size
                        return free_start
                    else:
                        free_cnt = 0
            else:
                free_cnt += 1
        if free_cnt >= size:
            free_start = len(self.m) - free_cnt
            self.m[free_start : free_start + size] = [mID] * size
            return free_start
        return -1

    def freeMemory(self, mID: int) -> int:
        cnt = 0
        for i in range(len(self.m)):
            if self.m[i] == mID:
                self.m[i] = 0
                cnt += 1
        return cnt

# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.freeMemory(mID)
