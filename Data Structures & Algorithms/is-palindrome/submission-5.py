class Solution:
    def isPalindrome(self, s: str) -> bool:
        st =''
        for sts in s:
            if sts.isalnum():
                st += sts.lower()
        
        st_rev = st[::-1]
        print(st)
        print(st_rev)
        return st == st_rev
