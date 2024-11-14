class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        def inorder_traversal(node, values):
            if node:
                inorder_traversal(node.left, values)
                values.add(node.val)
                inorder_traversal(node.right, values)

        def check_complement(node, values, target):
            if node:
                if (target - node.val) in values:
                    return True
                return check_complement(node.left, values, target) or check_complement(node.right, values, target)
            return False

        values = set()
        inorder_traversal(root1, values)
        return check_complement(root2, values, target)
