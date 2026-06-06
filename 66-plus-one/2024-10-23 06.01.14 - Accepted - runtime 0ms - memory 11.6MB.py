class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num=""
        for i in digits:
            num+=str(i)
        num=int(num)
        num=num+1
        num=str(num)
        arr=[]
        for i in range(len(num)):
            arr+=[int(num[i])]
        return arr