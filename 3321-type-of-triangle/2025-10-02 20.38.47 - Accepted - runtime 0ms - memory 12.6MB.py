class Solution(object):
    def triangleType(self,nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        a,b,c=sorted(nums)
        if a+b>c:
            if a==c:
                return "equilateral"
            elif a==b or b==c:
                return "isosceles"
            else:
                return "scalene"
        return "none"
