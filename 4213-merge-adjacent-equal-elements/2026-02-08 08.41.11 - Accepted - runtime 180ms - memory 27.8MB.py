class Solution(object):
    def mergeAdjacent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        stack=[]
        for x in nums:
            while stack and stack[-1]==x:
                x+=stack.pop()
            stack.append(x)
        return stack