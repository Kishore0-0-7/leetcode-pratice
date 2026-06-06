class Solution(object):
    def findGoodIntegers(self, n):
        from collections import defaultdict
        c=[]
        i=1
        while i**3 <=n:
            c.append(i**3)
            i+=1
        count=defaultdict(int)
        leng=len(c)
        for i in range(leng):
            for j in range(i,leng):
                s=c[i]+c[j]
                if s>n:
                    break
                count[s]+=1
        res=[]
        for k,v in count.items():
            if v>=2:
                res.append(k)
        return sorted(res)