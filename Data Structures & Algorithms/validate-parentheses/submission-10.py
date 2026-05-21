class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True
        char_map = {'}' : '{' , ']':'[' , ')' : '('}
        stack = []

        for st in s:
            if st not in char_map:
                stack.append(st)
            else:
                if stack and stack[-1] == char_map[st]:
                    stack.pop()
                else:
                    return False
        return True if not stack else False