class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        diff = [arr[i+1] - arr[i] for i in range(len(arr)-1)]
        return len(set(diff)) == 1