class Solution(object):
    def maxPathScore(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        m,n=len(grid),len(grid[0])
        dp=[[{} for _ in range (n)]for _ in range(m)]
        v=grid[0][0]
        score=v
        cost=0 if v==0 else 1
        if cost<=k:
            dp[0][0][cost]=score
        for i in range(m):
            for j in range(n):
                if i==0 and j==0:
                    continue
                v=grid[i][j]
                add_score=v
                add_cost=0 if v==0 else 1
                c=[]
                if i>0:
                    c.append(dp[i-1][j])
                if j>0:
                    c.append(dp[i][j-1])
                for p in c:
                    for pc,ps in p.items():
                        nc=pc+add_cost
                        if nc<=k:
                            ns=ps+add_score
                            if nc not in dp[i][j] or ns>dp[i][j][nc]:
                                dp[i][j][nc]=ns
        last=dp[m-1][n-1]
        return max(last.values()) if last else -1