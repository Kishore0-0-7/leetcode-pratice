class Solution(object):
    def closestTarget(self, words, target, startIndex):
        """
        :type words: List[str]
        :type target: str
        :type startIndex: int
        :rtype: int
        """
        n=len(words)
        md=float('inf')
        for i in range(n):
            if words[i]==target:
                ld=(i-startIndex+n)%n
                rd=(startIndex-i+n)%n
                md=min(md,ld,rd)
        return -1 if md==float('inf') else md