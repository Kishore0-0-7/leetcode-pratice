class Solution(object):
    def maxArea(self, height):
        m=0
        le=0
        ri=len(height)-1
        while(le<ri):
            l=min(height[le],height[ri])
            b=ri-le
            a=l*b
            m=max(m,a)
            le+=1
        return m