class Solution(object):
    def maxArea(self, height):
        le=0
        ri=len(height)-1
        m=0
        while(le<ri):
            m=max(m,min(height[le],height[ri])*(ri-le))
            if height[le] < height[ri]:
                le=le+1
            else:
                ri=ri-1
        return m