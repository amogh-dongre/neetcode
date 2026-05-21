class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
       
        mp = {}      ## this will store the character , and its frequency
        l , r = 0 , len(s) -1 ## left and right pointers
        res = 0
        maxfreq = 0
        for r in range(len(s)):
            mp[s[r]] = 1+ mp.get(s[r] , 0)
            maxfreq = max(maxfreq, mp[s[r]])

            while r-l+1 - maxfreq > k:
                mp[s[l]] -=1
                l+=1
            res = max(res , r - l + 1)
        return res

        
        