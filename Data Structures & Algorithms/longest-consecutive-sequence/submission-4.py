class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        print(nums)
        max_consec = 0
        if len(nums) > 0:
            current_num = nums[0]
            total_consec = 1
            max_consec = 1
        
        for i in range(1,len(nums)):
            if current_num == nums[i]:
                continue
            elif current_num + 1 == nums[i] or current_num == nums[i]:
                total_consec+=1
                if total_consec > max_consec:
                    max_consec = total_consec
            else:
                total_consec = 1
            current_num = nums[i]


        return max_consec
        