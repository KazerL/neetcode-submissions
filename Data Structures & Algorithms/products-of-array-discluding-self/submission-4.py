import math 

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        finArray = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            finArray[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            finArray[i] *= suffix
            suffix *= nums[i]

        return finArray

            
        
