# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        lst=[]
        if root:
            lst.extend(self.postorderTraversal(root.left))
            lst.extend(self.postorderTraversal(root.right))
            lst.append(root.val)
        return lst
        