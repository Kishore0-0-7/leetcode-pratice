class Solution(object):
    def secondHighest(self, s):
        """
        :type s: str
        :rtype: int
        """
        s=set(s)
        nums=[]
        for i in s:
            if i.isdigit()==True:
                nums.append(i)
        if len(nums)<=1:
            return -1
        nums.sort()
        return int(nums[-2])