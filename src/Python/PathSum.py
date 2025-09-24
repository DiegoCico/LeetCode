# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        return self.pathSum(root, targetSum, 0)

    def pathSum(self, root, target, current):
        if root: 
            current += root.val

        if not root.left and not root.right:
            return target == current
        
        if root.left and root.right:
            return self.pathSum(root.left, target, current) or self.pathSum(root.right,target,current)
        elif root.left:
            return self.pathSum(root.left, target, current)
        else:
            return self.pathSum(root.right,target,current)

        
        