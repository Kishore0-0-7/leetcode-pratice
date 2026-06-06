class Solution(object):
    def maxArea(self, height):
        le=0
        ri=len(height)-1
        m=min(height[le],height[ri])*(ri-le)
        while(le<ri):
            if height[le] < height[ri]:
                le+=1
            else:
                ri-=1
            m=max(m,min(height[le],height[ri])*(ri-le))
        return m