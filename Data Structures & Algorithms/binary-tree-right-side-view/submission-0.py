# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        level_map = {}
        right_view = []
        
        self.dfs(root , level_map , 0)
        n = max(level_map.keys())
        
        for i in range(n+1):
            right_view.append(level_map[i][-1])
        
        return right_view
    
    def dfs(self , root , level_map , curr_level):
        if root is None:
            return None
        
        if curr_level not in level_map:
            level_map[curr_level] = []
        
        level_map[curr_level].append(root.val)

        self.dfs(root.left , level_map , curr_level +1)
        self.dfs(root.right , level_map , curr_level +1)

        return root
