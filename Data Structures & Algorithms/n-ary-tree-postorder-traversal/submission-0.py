"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []
        def traverse(node):
            if node:
                for c in node.children:
                    traverse(c)
                res.append(node.val)
        traverse(root)
        return res