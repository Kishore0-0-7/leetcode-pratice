class Solution(object):
    def kthLargestNumber(self, nums, k):
        """
        :type nums: List[str]
        :type k: int
        :rtype: str
        """
        result=list(int(x) for x in nums)  
        result.sort()
        return str(result[-k])