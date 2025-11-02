class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = 0
        count = 0
        m = len(flowerbed)

        while i < m and count < n:
            if flowerbed[i] == 1:
                i += 2
            else:
                empty_left = (i == 0) or (flowerbed[i - 1] == 0)
                empty_right = (i == m - 1) or (flowerbed[i + 1] == 0)
                if empty_left and empty_right:
                    count += 1
                    flowerbed[i] = 1
                    i += 2
                else:
                    i += 1

        return count >= n
