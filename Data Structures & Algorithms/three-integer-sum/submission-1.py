class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        arr_of_sols = []
        nums.sort()
        j = 0

        for i in range(0,len(nums)):
            target  = 0 - nums[i]
            left = i + 1
            right = len(nums) - 1
            while(left < right):
                if nums[left] + nums[right] == target and right != i and left != i:
                    return_list = [nums[i],nums[left],nums[right]]
                    return_list.sort()
                    if(return_list not in arr_of_sols):
                        arr_of_sols.append(return_list)
                    left+=1
                elif nums[left] + nums[right] > target or right == i:
                    right-=1
                else:
                    left+=1

        return arr_of_sols