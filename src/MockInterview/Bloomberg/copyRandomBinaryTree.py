# Definition for Node.
# class Node:
#     def __init__(self, val=0, left=None, right=None, random=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.random = random

class Solution:
    def copyRandomBinaryTree(self, root: 'Optional[Node]') -> 'Optional[NodeCopy]':
        if not root:
            return None

        clones = {root: NodeCopy(root.val)}
        queue = [root]

        while queue:
            node = queue.pop(0)
            clone = clones[node]

            for child in [node.left, node.right, node.random]:
                if child:
                    if child not in clones:
                        clones[child] = NodeCopy(child.val)
                        queue.append(child)

            clone.left = clones.get(node.left)
            clone.right = clones.get(node.right)
            clone.random = clones.get(node.random)

        return clones[root]
