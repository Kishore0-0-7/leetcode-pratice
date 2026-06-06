class Solution(object):
    def countMajoritySubarrays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        p=0
        f=defaultdict(int)
        f[0]=1
        ans=0
        for i in nums:
            p+=1 if i==target else -1
            for ps in f:
                if ps<p:
                    ans+=f[ps]
            f[p]+=1
        return ans