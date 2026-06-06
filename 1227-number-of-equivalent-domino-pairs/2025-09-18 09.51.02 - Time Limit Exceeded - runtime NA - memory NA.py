class Solution(object):
    def numEquivDominoPairs(self, dominoes):
        """
        :type dominoes: List[List[int]]
        :rtype: int
        """
        count=0
        for i in range(len(dominoes)-1):
            for j in range(i+1,len(dominoes)):
                if((dominoes[i][0]==dominoes[j][0]) and (dominoes[i][1]==dominoes[j][1]) or (dominoes[i][0]==dominoes[j][1]) and (dominoes[i][1]==dominoes[j][0]) ):
                    count+=1
        return count