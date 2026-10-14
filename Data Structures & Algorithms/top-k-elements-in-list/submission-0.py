class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_of_nums = {}
        for num in nums:
            num_of_nums[num] = num_of_nums.get(num, 0) + 1
        
        sorted_dict = dict(sorted(num_of_nums.items(), key=lambda item: item[1], reverse=True))

        output_list = []
        for key in sorted_dict:
            if k < 1:
                break
            output_list.append(key)
            k-=1
        return list(output_list)
        