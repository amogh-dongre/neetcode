class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0 :
         return 0
        if len(nums) == 1:
            return 1
        nums.sort()
        nums_set = set(nums)
        count = 1

        for i in nums_set:
            if i + 1  in nums_set:
                curr = i
                curr_length = 1
                while curr + 1 in nums_set:
                    curr +=1 
                    curr_length += 1
                count = max(count , curr_length)
        return count
                
                