
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        max_width = 0
        queue = [(root, 0)]
        
        while queue:
            level_length = len(queue)
            _, first_index = queue[0]
            _, last_index = queue[-1]
            max_width = max(max_width, last_index - first_index + 1)
            
            new_queue = []
            for node, idx in queue:
                rel_idx = idx - first_index
                if node.left:
                    new_queue.append((node.left, 2 * rel_idx))
                if node.right:
                    new_queue.append((node.right, 2 * rel_idx + 1))
            queue = new_queue
        
        return max_width