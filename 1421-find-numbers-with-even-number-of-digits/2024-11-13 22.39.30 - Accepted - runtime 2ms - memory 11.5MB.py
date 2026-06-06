class Solution(object):
    def findNumbers(self, nums):
        m = 0 
        for num in nums:
            if (len(str(num)) % 2 == 0):
                m +=1
        return m