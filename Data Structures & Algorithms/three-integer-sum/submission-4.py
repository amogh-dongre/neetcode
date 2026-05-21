class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for m in range(1 ,len(nums) - 1):
            l , r = 0 , len(nums) -1
            while l<m and r>m:
                target = nums[l] + nums[m] + nums[r]

                if target == 0 and [nums[l] , nums[m] , nums[r]] not in res :
                    res.append([nums[l] , nums[m] , nums[r]])
                    l+=1
                    r-=1
                elif target < 0:
                    l+=1
                else:
                    r -= 1
        return res








"""
Binary Search is best
mid+l+r == 0 >>[l,m,r]
mid+l+r
[-4,[-1,-1,0,1],2]
           ^  
"""