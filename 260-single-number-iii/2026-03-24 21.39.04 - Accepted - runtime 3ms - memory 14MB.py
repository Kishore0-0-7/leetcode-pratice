class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count={}
        for num in nums:
            count[num]=count.get(num,0)+1
        result=[]
        for num in nums:
            if count[num]==1:
                result.append(num)
        return result
 
