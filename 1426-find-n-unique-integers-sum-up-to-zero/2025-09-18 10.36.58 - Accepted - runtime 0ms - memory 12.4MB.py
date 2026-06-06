class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        arr=[0]*n
        k=1
        for i in range(n//2):
            arr[i]=k
            arr[n-i-1]=-k
            k+=1
        return arr