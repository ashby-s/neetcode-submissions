class Solution:
    def trap(self, height: List[int]) -> int:
        total_water = 0

        max_val = 0
        left_maxes = []
        for val in height:
            left_maxes.append(max_val)
            if max_val < val:
                max_val = val

        i = len(height) - 1
        max_val = 0
        right_maxes = []
        while i != -1:
            right_maxes.append(max_val)
            if max_val < height[i]:
                max_val = height[i] 
            i-=1
        
        right_maxes.reverse()

        for i in range(0,len(height)):
            total_water += max(min(left_maxes[i], right_maxes[i]) - height[i],0)

        return total_water 
        