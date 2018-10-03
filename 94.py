class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return list()
        stack = list()
        res = list()
        while True:
            if root.left is not None:
                stack.append(root)
                root = root.left
            else:
                res.append(root.val)
                if root.right is not None:
                    root = root.right
                else:
                    if len(stack)>0:
                        root = stack.pop()
                        root.left=None
                    else:
                        break
        return res