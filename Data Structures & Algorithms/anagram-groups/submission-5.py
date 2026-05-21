class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups= defaultdict(list)
        
        for st in strs:
            sorted_s = ''.join(sorted(st))
            groups[sorted_s].append(st)
        return list(groups.values())
