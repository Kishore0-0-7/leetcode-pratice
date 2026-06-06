class Solution(object):
    def maxFreqSum(self, s):
        """
        :type s: str
        :rtype: int
        """
        vo={}
        co={}
        vowles="aeiou"
        for i in s:
            if i in vowles:
                vo[i]=vo.get(i,0)+1
            else:
                co[i]=co.get(i,0)+1
        voc=max(vo.values()) if vo else 0
        coc=max(co.values()) if co else 0
        return voc+coc
        
                
        