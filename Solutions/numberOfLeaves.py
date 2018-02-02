class Solution:

    def countLeaves(self, root):
        if node is None:
            return 0
        if(node.left is None and node.right is None):
            return 1
        else:
            return getLeafCount(node.left) + getLeafCount(node.right)