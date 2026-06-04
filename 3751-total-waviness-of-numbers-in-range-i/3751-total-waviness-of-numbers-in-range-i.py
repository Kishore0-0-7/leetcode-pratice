class Solution(object):
    def totalWaviness(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        t=0
        for n in range(num1,num2+1):
            s=str(n)
            if len(s)<3: continue
            wav=0
            for i in range(1,len(s)-1):
                l=int(s[i-1])
                m=int(s[i])
                r=int(s[i+1])
                if m>l and m>r: wav+=1
                elif m<l and m<r: wav+=1
            t+=wav
        return t