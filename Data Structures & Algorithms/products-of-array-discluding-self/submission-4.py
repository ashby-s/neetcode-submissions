class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        left_products = [1,nums[0]]
        for i in range(1, len(nums)-1):
            left_products.append(left_products[i]*nums[i])
        
        right_products = [1,nums[len(nums)-1]]
        i = len(nums)-2
        while i > 0:
            right_products.append(right_products[len(nums) - i - 1]*nums[i])
            i-=1

        right_products.reverse()

        output_arr = []
        for i in range(0,len(nums)):
            output_arr.append(left_products[i]*right_products[i])

        return output_arr
