class Solution(object):
    def getSneakyNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        freq={}
        res=[]
        for num in nums:
            freq[num]=freq.get(num,0)+1
            if freq[num]==2:
                res.append(num)
        return res