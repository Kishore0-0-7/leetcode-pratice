class Solution(object):
    def alternatingXOR(self, nums, target1, target2):
        """
        :type nums: List[int]
        :type target1: int
        :type target2: int
        :rtype: int
        """
        MOD=10**9 + 7
        from collections import defaultdict
        px=0
        n=len(nums)
        need0=defaultdict(int)
        need1=defaultdict(int)
        need0[0]=1
        dp0=dp1=0
        for num in nums:
            px^=num
            dp1=need0[px^target1]%MOD
            dp0=need1[px^target2]%MOD
            need0[px]=(need0[px]+dp0)%MOD
            need1[px]=(need1[px]+dp1)%MOD
        return (dp0+dp1)%MOD