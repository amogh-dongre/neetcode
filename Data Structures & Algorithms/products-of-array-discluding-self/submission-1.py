class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
      res = [1] * len(nums)

      for i in range(len(nums)):
        for j in range(len(nums)):
            if j != i:
                res[i] *= nums[j]
      return res


"""
[1,2,4,6]
 ^ (2*4*6)
   ^(1*4*6)
      ^(2*1*6)
        ^(1*2*4) 
"""