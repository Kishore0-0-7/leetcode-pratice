class Solution(object):
    def arrayRankTransform(self, arr):
        a=sorted(set(arr))
        p={}
        for i,num in enumerate (a):
            p[num]=i+1
        return [p[num] for num in arr]