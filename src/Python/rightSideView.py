class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        res = []
        level = [root] 

        while level:
            res.append(level[-1].val) 
            next_level = []
            for node in level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            print(next_level)
            level = next_level
        
        return res
