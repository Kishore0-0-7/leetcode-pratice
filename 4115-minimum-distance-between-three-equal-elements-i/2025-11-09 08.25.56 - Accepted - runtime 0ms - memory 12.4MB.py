class Solution(object):
    def minimumDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pos=defaultdict(list)
        for i,v in enumerate(nums):
            pos[v].append(i)
        a=float('inf')
        for v,p in pos.items():
            if len(p)<3:
                continue
            for i in range(len(p)-2):
                dis=2*(p[i+2]-p[i])
                if dis<a:
                    a=dis
        return a if a!=float('inf') else -1
            