# https://leetcode.com/problems/binary-tree-postorder-traversal/description/?envType=study-plan&id=data-structure-i


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return 
        
        def dfs(root):
            if root is None:
                return
            
            dfs(root.left)
            dfs(root.right)
            res.append(root.val)

        res = []
        dfs(root)
        return res