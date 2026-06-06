class Solution(object):
    def maxSubsequence(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        w=nums
        nums.sort()
        p=nums[-k:]
        t=[]
        for i in w:
            r=0
            while(r<len(p)):
                if i==p[r]:
                    t.append(i)
                    p.remove(p[r])
                    break
                r+=1
        return t