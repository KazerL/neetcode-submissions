class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map = {}
        index = 0

        if len(nums) == 0:
            return False

        for item in nums:
            if item in map:
                return True
            
            map[nums[index]] = index

            index += 1

            if index >= len(nums):
                return False

            
            