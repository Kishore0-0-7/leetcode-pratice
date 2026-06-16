class Solution(object):
    def processStr(self, s):
        """
        :type s: str
        :rtype: str
        """
        res=[]
        for ch in s:
            if ch.islower():
                res.append(ch)
            if ch=="*":
                if res:
                    res.pop()
            if ch=="#":
                res+=res
            if ch=='%':
                res.reverse()
        return "".join(res)