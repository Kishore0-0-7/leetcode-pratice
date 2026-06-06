class Solution(object):
    def rotatedDigits(self,n):
        """
        :type n: int
        :rtype: int
        """
        count=0
        for i in range(1,n+1):
            s=str(i)
            change=False
            valid=True
            for ch in s:
                if ch in ['3','4','7']:
                    valid=False
                    break
                elif ch not in ['0','1','8']:
                    change=True
            if change and valid:
                count+=1
        return count