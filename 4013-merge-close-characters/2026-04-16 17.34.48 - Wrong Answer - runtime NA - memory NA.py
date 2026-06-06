class Solution(object):
    def mergeCharacters(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        ls={}
        res=[]
        for i,ch in enumerate(s):
            if ch in ls and i-ls[ch]<=k:
                continue
            else:
                res.append(ch)
                ls[ch]=i
        return "".join(res)