class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        arr=[]
        nums=list(range(left,right+1))
        for i in nums:
            if(len(str(i))==1):
                arr.append(i)
            else:
                if("0" in str(i)):
                    continue
                else:
                    c=0
                    for j in str(i):
                        if(int(i)%int(j)==0):
                            c+=1
                    if(c==len(str(i))):
                        arr.append(int(i))
        return arr