# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root==None:
            return 0
        tail_tree=self.max_tail_tree(root)
        maxi=[None]
        self.dfs(tail_tree,maxi)
        return maxi[0]
    
    def dfs(self,root,maxi):
        l = 0 if root.left==None else root.left.val
        r = 0 if root.right==None else root.right.val
        if l>0 and r>0:
            res = l+r+root.val-max(l,r)
        else:
            res = root.val
        if maxi[0]==None or res>maxi[0]:
            maxi[0]=res
        if root.left is not None:
            self.dfs(root.left,maxi)
        if root.right is not None:
            self.dfs(root.right,maxi)
        
    def max_tail_tree(self,root):
        if root.left==None and root.right==None:
            return TreeNode(root.val)
        if root.left==None:
            right = self.max_tail_tree(root.right)
            val = (right.val+root.val) if right.val>0 else root.val
            n_root=TreeNode(val)
            n_root.right=right
        elif root.right==None:
            left = self.max_tail_tree(root.left)
            val = (left.val + root.val) if left.val>0 else root.val
            n_root=TreeNode(val)
            n_root.left=left
        else:
            right = self.max_tail_tree(root.right)
            left = self.max_tail_tree(root.left)
            val = max(left.val,right.val)
            val = (val + root.val) if val>0 else root.val
            n_root=TreeNode(val)
            n_root.left=left
            n_root.right=right
        return n_root
        