# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(preorder)==0:
            return None
        root =TreeNode(preorder[0])
        left = inorder.index(root.val)
        root.left = self.buildTree(preorder[1:left+1],inorder[:left])
        root.right = self.buildTree(preorder[left+1:],inorder[left+1:])
        return root