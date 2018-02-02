class Solution:
  # @param root Root of tree
  # @return Height of tree
    def findHeight(self, root):
        if not root:
            return 0

        lh = findHeight(root.left)
        rh = findHeight(root.right)
        if lh > rh:
            return lh + 1
        else:
            return rh + 1