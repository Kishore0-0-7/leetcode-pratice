class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freqmp=Counter(nums)
        ans=0
        for num in freqmp:
            if num+1 in freqmp:
                curr= freqmp[num]+freqmp[num+1]
                ans=max(ans,curr)
        return ans
 
