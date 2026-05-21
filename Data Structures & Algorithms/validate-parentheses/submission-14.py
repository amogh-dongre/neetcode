class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True
        stack = []
        char_map = {'}' : '{' , ']':'[' , ')' : '('}

        for st in s:
            if st not in char_map:
                stack.append(st)
            else:
                if stack and stack[-1] == char_map[st]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0