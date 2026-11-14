class Solution(object):
    def findDegrees(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res=[0]*len(matrix)
        for i in range(len(matrix)):
            deg=0
            for j in range(len(matrix)):
                deg+=matrix[i][j]
            res[i]=deg
        return res        