class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(0, len(nums)):
            if (nums[i] in nums[:i]) and (nums[i] in nums[i:]):
                return True
        
        return False
        