class Solution(object):
    def wordSquares(self, words):
        """
        :type words: List[str]
        :rtype: List[List[str]]
        """
        n=len(words)
        res=[]
        for i  in range (n):
            t=words[i]
            for j in range(n):
                if j==i:
                    continue
                left=words[j]
                if t[0]!=left[0]:
                    continue
                for k in range(n):
                    if k==i or k==j:
                        continue
                    r=words[k]
                    if t[3]!=r[0]:
                        continue
                    for l in range (n):
                        if l==i or l==j or l==k:
                            continue
                        b=words[l]
                        if b[0]!=left[3]:
                            continue
                        if b[3]!=r[3]:
                            continue
                        res.append([t,left,r,b])
        res.sort()
        return res