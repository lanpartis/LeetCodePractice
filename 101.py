# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root==None:
            return True
        return self.symmetric(root.left,root.right)
    
    def symmetric(self,l,r):
        if l==None and r==None:
            return True
        if l==None or r==None:
            return False
        if l.val!=r.val:
            return False
        return self.symmetric(l.left,r.right) and self.symmetric(l.right,r.left)