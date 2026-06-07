class Solution(object):
    def generateValidStrings(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[str]
        """
        res=[]
        def dfs(p,c,po,s):
            if p==n:
                res.append(s)
                return
            dfs(p+1,c,False,s+"0")
            if not po and c+p<=k:
                dfs(p+1,c+p,True,s+"1")
        dfs(0,0,False,"")
        return res