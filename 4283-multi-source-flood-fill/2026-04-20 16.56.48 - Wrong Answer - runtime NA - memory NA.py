class Solution(object):
    def colorGrid(self, n, m, sources):
        """
        :type n: int
        :type m: int
        :type sources: List[List[int]]
        :rtype: List[List[int]]
        """
        from collections import deque
        g=[[0]*m for _ in range(n)]
        time=[[float('inf')]*m for _ in range(n)]
        q=deque()
        for r,c,color in sources:
            g[r][c]=color
            time[r][c]=0
            q.append((r,c,color,0))
        dirs=[(1,0),(-1,0),(0,1),(0,-1)]
        while q:
            r,c,color,t=q.popleft()
            for dr,dc in dirs:
                nr,nc=r+dr,c+dc
                if 0<=nr<n and 0<=nc<m:
                    if time[nr][nc]>t+1:
                        time[nr][nc]=t+1
                        g[nr][nc]=color
                        q.append((nr,nc,color,t+1))
                    elif time[nr][nc]==t+1:
                        if g[nr][nc]<color:
                            g[nr][nc]=color
        return g