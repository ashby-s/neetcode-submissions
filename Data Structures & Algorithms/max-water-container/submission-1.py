class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1
        max_water = 0

        while(left < right):
            if heights[left] < heights[right]:
                current_water = (right-left) * heights[left]
                left+=1
            else:
                current_water = (right-left) * heights[right]
                right-=1
            
            if max_water < current_water:
                max_water = current_water
        
        return max_water