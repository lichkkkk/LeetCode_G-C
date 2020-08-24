class Solution:
    def thousandSeparator(self, n: int) -> str:
        res = []
        while n > 1000:
            res.append(("00" + str(n % 1000))[-3:])
            n //= 1000
        res.append(str(n))
        return ".".join(reversed(res))
