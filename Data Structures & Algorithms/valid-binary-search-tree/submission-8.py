# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        return self.dfs(root, float('-inf'), float('inf'))
    
    def dfs(self, root, min_val, max_val):
        if root is None:
            return True
        
        if root.val <= min_val or root.val >= max_val:
            return False
        
        
        left_valid = self.dfs(root.left, min_val, root.val)
        right_valid = self.dfs(root.right, root.val, max_val)
        
        return left_valid and right_valid


"""
simple logic use dfs to traverse
recursively check if left node is less than root node
right node is greater than root node
if not return False
else return True
"""