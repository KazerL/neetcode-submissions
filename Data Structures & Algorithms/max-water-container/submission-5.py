class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # initial variables
        maxArea = 0
        width = len(heights) - 1

        # pointers
        left = 0
        right = len(heights) - 1

        # initial max area
        maxArea = min(heights[left], heights[right]) * width

        while True:
            # break condition
            if left >= right or right <= left:
                break

            tempArea = min(heights[left], heights[right]) * width

            if tempArea > maxArea:
                maxArea = tempArea

            
            if heights[left] == heights[right]:
                left += 1
                width -= 1
                continue
            elif min(heights[left], heights[right]) == heights[left]:
                left += 1
                width -= 1
                continue
            elif min(heights[left], heights[right]) == heights[right]:
                right -= 1
                width -= 1
                continue


            
            

        return maxArea
