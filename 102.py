# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root==None:
            return list()
        layer = [root]
        res = list()
        while True:
            if len(layer)==0:
                break
            n_layer=list()
            layer_res=list()
            for node in layer:
                layer_res.append(node.val)
                if node.left is not None:
                    n_layer.append(node.left)
                if node.right is not None:
                    n_layer.append(node.right)
            layer = n_layer
            res.append(layer_res)

        return res