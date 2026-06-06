class Solution(object):
    def largestSubmatrix(self,matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        rows,cols=len(matrix),len(matrix[0])
        max_area=0

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c]==1 and r>0:
                    matrix[r][c]+=matrix[r-1][c]
            heights=sorted(matrix[r])
            for i in range(cols-1,-1,-1):
                width=cols-i
                area=heights[i]*width
                max_area=max(max_area,area)
        return max_area