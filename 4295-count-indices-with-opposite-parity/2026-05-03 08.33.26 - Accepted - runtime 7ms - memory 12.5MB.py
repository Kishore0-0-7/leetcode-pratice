class Solution(object):
    def countOppositeParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        r=[0]*n
        ec=0
        oc=0
        for i in range(n-1,-1,-1):
            if nums[i]%2==0:
                r[i]=oc
                ec+=1
            else:
                r[i]=ec
                oc+=1
        return r