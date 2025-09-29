class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l,r = 0, len(nums) - 1

        result = []
        
        while len(result) != len(nums):
            if nums[l]**2 > nums[r]**2:
                result.append(nums[l]**2)
                l += 1
            else:
                result.append(nums[r]**2)
                r -= 1
                
        return result[::-1]