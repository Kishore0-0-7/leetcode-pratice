class Solution(object):
    def heightChecker(self, heights):
        a=sorted(heights)
        c=0
        for i in range(len(heights)):
            if heights[i]!=a[i]:
                c+=1
        return c
        