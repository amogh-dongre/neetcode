class Solution:
    def isValid(self, s: str) -> bool:
        char_map = {'}' : '{' , ']':'[' , ')' : '('}
        stack = []

        for st in s:
            if st in char_map:
                if stack and stack[-1] == char_map[st]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(st)
        return True if not stack else False