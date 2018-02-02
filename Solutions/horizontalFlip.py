class Solution:
    def flipHorizontalAxis(self, matrix):
        for i in range(0,matrix.length / 2):
            tmp = matrix[i]
            matrix[i] = matrix[matrix.length - 1 - i]
            matrix[matrix.length - 1 - i] = tmp