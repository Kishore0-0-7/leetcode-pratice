class Solution(object):
    def sumAndMultiply(self, s, queries):
        """
        :type s: str
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        mod=10**9+7
        n=len(s)
        cnt=[0]*(n+1)
        sm=[0]*(n+1)
        val=[0]*(n+1)
        p10=[1]*(n+1)
        for i in range(1,n+1):
            p10[i]=(p10[i-1]*10)%mod
        for i in range(n):
            digit=ord(s[i])-48
            cnt[i+1]=cnt[i]
            sm[i+1]=sm[i]
            val[i+1]=val[i]
            if digit!=0:
                cnt[i+1]+=1
                sm[i+1]+=digit
                val[i+1]=(val[i]*10+digit)%mod
        ans=[]
        for l,r in queries:
            td=cnt[r+1]-cnt[l]
            if td==0:
                ans.append(0)
                continue 
            sd=sm[r+1]-sm[l]
            x=(val[r+1]-(val[l]*p10[td])%mod+mod)%mod
            ans.append((x*sd)%mod)
        return ans