class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_k = sorted(nums)
        seen = {}

        for i in nums_k:
            seen[i] = 1 + seen.get(i, 0)
        print(seen)
        res = sorted(seen , key = seen.get , reverse=True)
        return res[:k]           
        