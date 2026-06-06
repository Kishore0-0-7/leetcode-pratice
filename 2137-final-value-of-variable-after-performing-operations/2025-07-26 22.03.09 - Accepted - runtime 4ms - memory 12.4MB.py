class Solution(object):
    def finalValueAfterOperations(self, operations):
        res=0
        for i in operations:
            if i=="++X" or i=="X++":
                res+=1
            elif i=="--X" or i=="X--":
                res-=1
        return res