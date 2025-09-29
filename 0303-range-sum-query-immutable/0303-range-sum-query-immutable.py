class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.cumsum = [nums[0]]
        for i in range(1, len(self.nums)):
            self.cumsum.append(self.cumsum[i-1]+self.nums[i])

    def sumRange(self, left: int, right: int) -> int:
        if left > 0:
            return self.cumsum[right] - self.cumsum[left-1]
        else:
            return self.cumsum[right]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)