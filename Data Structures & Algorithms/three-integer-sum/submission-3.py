class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        arr_of_sols = []
        nums.sort()

        for i in range(0,len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            target  = 0 - nums[i]
            left = i + 1
            right = len(nums) - 1
            while(left < right):
                if nums[left] + nums[right] == target:
                    return_list = [nums[i],nums[left],nums[right]]
                    return_list.sort()
                    if(return_list not in arr_of_sols):
                        arr_of_sols.append(return_list)
                    left+=1
                elif nums[left] + nums[right] > target:
                    right-=1
                else:
                    left+=1

        return arr_of_sols