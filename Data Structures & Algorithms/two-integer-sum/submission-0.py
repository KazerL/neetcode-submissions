class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pos = 0
        pos1 = 1


        pivot = 0
        goal = 0


        while True:
            goal = nums[pos] + nums[pos1]


            if goal == target:
                return [pos,pos1]
            else:
                pos1 += 1


                if pos1 >= len(nums):
                    pivot += 1
                    pos = pivot
                    pos1 = pos + 1


                    if pos == (len(nums) - 1):
                        return "failure"
                    continue
        