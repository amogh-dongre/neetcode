class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = []
        l , r = 0 , len(numbers)-1
        while(l<r):
            curr_sum = numbers[l] + numbers[r]
            if curr_sum < target : 
                l+=1
            elif curr_sum > target :
                r-=1
            else:
                res.append(l+1)
                res.append(r+1)
                return res
        return res