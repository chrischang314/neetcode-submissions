# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def traverse(root):
            if not root:
                return 0, 0
            leftChild, leftPath = traverse(root.left)
            rightChild, rightPath = traverse(root.right)
            return 1 + max(leftChild, rightChild), max(1 + leftChild + rightChild, leftPath, rightPath)
        _, path = traverse(root)
        return path - 1