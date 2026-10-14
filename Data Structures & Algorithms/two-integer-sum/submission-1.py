class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0,len(nums)):
            if nums[i] > target:
                continue
            for j in range(0,len(nums)):
                if nums[j] > target:
                    continue
                if nums[i] + nums[j] == target:
                    return_list = [i,j]
                    return return_list