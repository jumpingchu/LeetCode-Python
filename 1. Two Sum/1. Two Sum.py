# Runtime: 57 ms, Beats: 97.3%
# Memory: 17.6 MB: Beats: 34.70%

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_num_idx = {}
        for i, num in enumerate(nums):
            if (target - num) in dict_num_idx:
                return [dict_num_idx[target - num], i]
            dict_num_idx[num] = i 
        return []


# Runtime: 518 ms, Beats: 41.40%
# Memory: 17.1 MB, Beats: 76.66%

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num in enumerate(nums):
            diff = target - num
            if diff in nums and nums.index(diff) != i:
                return [i,nums.index(diff)]
      
