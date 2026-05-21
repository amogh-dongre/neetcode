class Solution:
    def isPalindrome(self, s: str) -> bool:
        sts = ""
        for st in s:
            if st.isalnum():
                sts+=st.lower()
        print(sts)
        
        return sts == sts[::-1]
        # l , r  = 0 , len(sts) -1

        # while l < r:
        #     if sts[l] == sts[r]:
        #         continue
        #     else:
        #         return False
        # return True

        

        
        
      
        