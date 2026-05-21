class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
       nums.sort()
       nums_set = set(nums)
       count = 0
    #    print(nums_set)
       for i in nums_set:
        if i-1 not in nums_set:
            curr_num = i
            curr_length = 1
            while curr_num + 1 in nums_set:
                 curr_num += 1
                 curr_length += 1 
            count = max(count , curr_length)
       return count
        


"""
[2,3,4,5,10,20] 
     ^
"""
