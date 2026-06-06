class Solution(object):
    def countLocalMaximums(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        n=len(matrix)
        ans=0

        for i in range(n):
            for j in range(n):
                x=matrix[i][j]
                if x==0:
                    continue
                is_local=True
                for r in range(max(0,i-x),min(n,i+x+1)):
                    for c in range(max(0,j-x),min(n,j+x+1)):
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