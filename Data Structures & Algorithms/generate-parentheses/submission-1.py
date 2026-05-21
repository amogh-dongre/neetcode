class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack , res = [] , []

        def backtrack(openbrack , closedbrack):
            if openbrack == closedbrack == n:
                res.append("".join(stack))
                return

            if openbrack < n:
                stack.append("(")
                backtrack(openbrack + 1, closedbrack)
                stack.pop()
            if closedbrack < openbrack:
                stack.append(")")
                backtrack(openbrack, closedbrack + 1)
                stack.pop()
        backtrack(0,0)
        return res