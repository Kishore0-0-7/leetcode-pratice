class Solution(object):
    def countBeautifulPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        t=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if self.gcd(int(str(nums[i])[0]),int(str(nums[j])[-1]))==1:
                    t+=1
        return t
    def gcd(self,x,y):
        while y:
            x,y=y,x%y
        return abs(x)