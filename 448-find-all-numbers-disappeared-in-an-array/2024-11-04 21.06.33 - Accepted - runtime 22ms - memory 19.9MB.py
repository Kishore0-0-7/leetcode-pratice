class Solution(object):
    def findDisappearedNumbers(self, nums):
        a=set(nums)
        lst=[]
        for i in range(1,len(nums)+1):
            if i not in a:
                lst.append(i)
        return lst