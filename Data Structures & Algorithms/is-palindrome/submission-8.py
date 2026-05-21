class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0:
            return True
         
        st =''
        for sts in s:
            if sts.isalnum():
                st += sts.lower()
        l , r = 0 , len(st) - 1
        while l < r:
            if st[l] != st[r]:
                return False
            l += 1
            r -= 1
        return True
        # st_rev = st[::-1]
        # print(st)
        # print(st_rev)
        # return st == st_rev
