class Solution(object):
    def lexSmallestNegatedPerm(self, n, target):
        """
        :type n: int
        :type target: int
        :rtype: List[int]
        """
        ms=n*(n+1)//2
        if abs(target)>ms: return []
        arr=[-i for i in range (1,n+1)]
        if target==-1: return arr
        cs=-ms
        diff=target-cs
        for i in range(n-1,-1,-1):
            v=i+1
            gain=2*v
            if diff>=gain:
                arr[i]=v
                diff-=gain
            if diff==0: break
        if diff!=0:
            return []
        return sorted([-i for i in arr])