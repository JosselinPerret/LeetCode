class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic = {}

        for i in range(len(nums2)):
            dic[nums2[i]] = i 

        result = []

        for num in nums1:
            stack = [num for num in nums2[dic[num]:]]

            while stack != []:
                out = stack[0]
                
                if out > num:
                    result.append(out)
                    break
        
                del stack[0]
        
            if stack == []:
                result.append(-1)
        
        return result
        