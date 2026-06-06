class Solution(object):
    def maximumSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        r0,r1,r2=[],[],[]
        for n in nums:
            rem=n%3
            if rem==0:
                r0.append(n)
            elif rem==1:
                r1.append(n)
            else:
                r2.append(n)
        r0.sort(reverse=True)
        r1.sort(reverse=True)
        r2.sort(reverse=True)
        ans=0
        if len(r0)>=3:
            ans=max(ans,sum(r0[:3]))
        if len(r1)>=3:
                ans=max(ans,sum(r1[:3]))
        if len(r2)>=3:
                ans=max(ans,sum(r2[:3]))
        if len(r0)>=1 and len(r1)>=1 and len(r2)>=1:
                ans=max(ans,r0[0]+r1[0]+r2[0])
        return ans