# https://leetcode.com/problems/binary-tree-preorder-traversal


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return 
        
        def dfs(root):
            if root is None:
                return

            res.append(root.val)
            dfs(root.left)
            dfs(root.right)
        
        res = []
        dfs(root)
        return res