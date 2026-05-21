class Solution:
    def isPalindrome(self, s: str) -> bool:
        sts = ""
        for st in s:
            if st.isalnum():
                sts+=st.lower()
        
        
        l , r  = 0 , len(sts) -1

        while l < r:
            if sts[l] == sts[r]:
                l += 1
                r -= 1
            else:
                return False
        return True

        

        
        
      
        