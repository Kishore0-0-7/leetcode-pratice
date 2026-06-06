class Solution(object):
    def specialNodes(self, n, edges, x, y, z):
        """
        :type n: int
        :type edges: List[List[int]]
        :type x: int
        :type y: int
        :type z: int
        :rtype: int
        """
        g=[[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
    
        def bfs(start):
            dist=[-1] * n
            q=deque([start])
            dist[start]=0
            while q:
                u=q.popleft()
                for v in g[u]:
                    if dist[v]==-1:
                        dist[v]=dist[u] + 1
                        q.append(v)
            return dist
        dx=bfs(x)
        dy=bfs(y)
        dz=bfs(z)
        ans=0
        for i in range(n):
            a,b,c=sorted((dx[i],dy[i],dz[i]))
            if a*a+b*b==c*c:
                ans+=1
        return ans