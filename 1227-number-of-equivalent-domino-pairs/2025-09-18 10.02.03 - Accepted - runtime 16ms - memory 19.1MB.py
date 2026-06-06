class Solution(object):
    def numEquivDominoPairs(self, dominoes):
        """
        :type dominoes: List[List[int]]
        :rtype: int
        """
        di={}
        count=0
        for a,b in dominoes:
            k=(min(a,b),max(a,b))
            count+=di.get(k,0)
            di[k]=di.get(k,0)+1
        return count