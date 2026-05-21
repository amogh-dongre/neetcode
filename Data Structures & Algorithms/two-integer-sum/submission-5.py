class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      diff_set = {}
      for i , n in enumerate(nums):
        diff = target - n
        if diff in diff_set:
            return [diff_set[diff] , i]
        diff_set[n] = i
           