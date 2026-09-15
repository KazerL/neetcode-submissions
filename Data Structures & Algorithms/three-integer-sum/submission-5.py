class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        finArray = []

        #pointers
        i = 0
        lo = 0
        hi = 0
        offset = 0

        for index in range(len(nums)):
            # initial pointer positions
            i = index
            lo = index + 1
            hi = len(nums) - 1
            
            # reference for the iteration
            offset = 0 - nums[index]
            
            # skips duplicates
            if i > 0 and nums[index] == nums[index - 1]:
                continue

            while True:
                # break condition
                if lo >= hi or hi <= lo:
                    break
                # check for duplicates 
                if lo - 1 != i and nums[lo - 1] == nums[lo]:
                    lo += 1
                    continue
                # have to move hi pointer
                if nums[lo] + nums[hi] > offset:
                    hi -= 1
                    continue
                # have to move lo pointer
                elif nums[lo] + nums[hi] < offset:
                    lo += 1
                    continue
                # add condition
                elif nums[lo] + nums[hi] == offset:
                    finArray.append([nums[i],nums[lo],nums[hi]])
                    lo += 1
                    hi -= 1
                    continue

        return finArray



            