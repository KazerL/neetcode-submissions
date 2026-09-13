class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        map = {}
        counter = 1
        i = 0

        for entry in nums:
            # check out of bounds
            if i + 1 >= len(nums):
                map[i] = counter
                break
            # difference between consecutive next elements
            elif nums[i + 1] - nums[i] == 0:
                i += 1
                continue
            elif nums[i + 1] - nums[i] != 1:
                map[i] = counter
                counter = 1
                i += 1
                continue
            else:
                counter += 1
                i += 1

        finValue = max(map.values(), default = 0)

        return finValue

        
            

