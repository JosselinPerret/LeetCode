class Solution:
    def pivotInteger(self, n: int) -> int:
        s = sqrt(n*(n+1) / 2)
        if s.is_integer():
            return int(s)
        return -1

