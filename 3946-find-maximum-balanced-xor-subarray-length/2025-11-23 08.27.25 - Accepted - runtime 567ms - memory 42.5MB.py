class Solution(object):
    def maxBalancedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        px=0
        diff=0
        seen={(0,0):-1}
        l=0
        for i,v in enumerate(nums):
            px^=v
            if v&1==0:
                diff+=1
            else:
                diff-=1
            k=(px,diff)
            if  k in seen:
                l=max(l,i-seen[k])
            else:
                seen[k]=i
        return l