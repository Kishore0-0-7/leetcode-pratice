class Solution(object):
    def countLocalMaximums(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        rows=len(matrix)
        cols=len(matrix[0])
        ans=0

        for i in range(rows):
            for j in range(cols):
                x=matrix[i][j]
                if x==0:
                    continue
                is_local=True
                for r in range(max(0,i-x),min(rows,i+x+1)):
                    for c in range(max(0,j-x),min(cols,j+x+1)):
                        if abs(r-i)==x and abs(c-j)==x:
                            continue
                        if matrix[r][c]>x:
                            is_local=False
                            break
                    if not is_local:
                        break
                if is_local:
                    ans+=1
        return ans