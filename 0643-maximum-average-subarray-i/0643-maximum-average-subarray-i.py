class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        lenght = len(nums) - k + 1
        best_sum = sum(nums[:k])
        sum_temp = best_sum

        for i in range(k, len(nums)):
            sum_temp = sum_temp + nums[i] - nums[i - k]
            best_sum = max(best_sum, sum_temp)

        return best_sum / k
