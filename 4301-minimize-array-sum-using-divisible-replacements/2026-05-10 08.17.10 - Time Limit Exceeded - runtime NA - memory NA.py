class Solution(object):
    def minArraySum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        exist=set(nums)
        ans=0
        for x in nums:
            b=x
            d=1
            while d*d<=x:
                if x%d==0:
                    if d in exist:
                        b=min(b,d)
                    o=x//d
                    if o in exist:
                        b=min(b,o)
                d+=1            
            ans+=b
        return ans