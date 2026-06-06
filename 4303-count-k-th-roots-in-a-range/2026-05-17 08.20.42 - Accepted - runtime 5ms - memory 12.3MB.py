class Solution(object):
    def countKthRoots(self, l, r, k):
        """
        :type l: int
        :type r: int
        :type k: int
        :rtype: int
        """
        def kth(x,k):
            low,high=0,x
            while low<=high:
                mid=low+(high-low)//2
                if mid**k<=x:
                    low=mid+1
                else:
                    high=mid-1
            return high
        right=kth(r,k)
        left=kth(l-1,k)
        return right-left