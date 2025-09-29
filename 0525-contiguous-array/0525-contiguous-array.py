class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        dic = {}
        dic[0] = -1
        ans = 0
        sum = 0

        for i in range(len(nums)):
            sum += 2*nums[i]-1
            
            if sum in dic:
                ans = max(ans, i - dic[sum])
            else:
                dic[sum] = i
        
        return ans