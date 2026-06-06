class Solution(object):
    def countDistinct(self, n):
        """
        :type n: int
        :rtype: int
        """
        s=str(n)
        l=len(s)
        di=list(map(int,s))
        A=(9*(9**(l-1)-1))//8 if l>1 else 0
        B=0
        all_non_zero=True
        for i,d in enumerate(di):
            if d==0:
                all_non_zero=False
                break
            sc=d-1
            rem=l-1-i
            B+=sc*(9**rem)
        if all_non_zero:
            B+=1
        return A+B