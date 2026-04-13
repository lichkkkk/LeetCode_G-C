class Solution:
    def sumGame(self, num: str) -> bool:
        mid = len(num) // 2
        left_sum = sum([int(c) for c in num[:mid] if c.isdigit()])
        right_sum = sum([int(c) for c in num[mid:] if c.isdigit()])
        left_qmark = sum([1 for c in num[:mid] if not c.isdigit()])
        right_qmark = sum([1 for c in num[mid:] if not c.isdigit()])
        if left_sum == right_sum and left_qmark == 0 and right_qmark == 0:
            return False
        qmark_diff, sum_diff = None, None
        if left_qmark > right_qmark:
            qmark_diff = left_qmark - right_qmark
            sum_diff = right_sum - left_sum
        else:
            qmark_diff = right_qmark - left_qmark
            sum_diff = left_sum - right_sum
        if qmark_diff % 2 != 0:
            return True
        if sum_diff < 0:
            return True
        half_qmark_diff = qmark_diff // 2
        max_bad_diff = half_qmark_diff * 9
        return sum_diff != max_bad_diff
