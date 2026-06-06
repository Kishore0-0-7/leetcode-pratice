class Solution(object):
    def maxDepthAfterSplit(self, seq):
        """
        :type seq: str
        :rtype: List[int]
        """
        answer=[]
        depth=0
        for e in seq:
            if e=='(':
                depth+=1
            answer.append(depth%2^1)
            if e==')':
                depth-=1
        return answer