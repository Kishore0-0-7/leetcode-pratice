class Solution(object):
    def residuePrefixes(self, s):
        """
        :type s: str
        :rtype: int
        """
        se=set(s)
        print(se)
        return len(se) if len(se)%3!=0 else len(se)-1