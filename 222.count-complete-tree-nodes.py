# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        count = 1
        stack = [root]
        while stack:
            node = stack.pop(0)
            if node.left:
                stack.append(node.left)
                count+=1
            if node.right:
                stack.append(node.right)
                count+=1
        return count