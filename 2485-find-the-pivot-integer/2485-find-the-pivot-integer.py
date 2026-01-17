class Solution:
    def pivotInteger(self, n: int) -> int:
        if sqrt(n*(n+1) / 2).is_integer():
            return int(sqrt(n*(n+1) / 2))
        return -1

