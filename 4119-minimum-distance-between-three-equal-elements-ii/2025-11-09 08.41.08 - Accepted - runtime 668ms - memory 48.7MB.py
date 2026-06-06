class Solution(object):
    def minimumDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pos=defaultdict(list)
        for i,v in enumerate(nums):
            pos[v].append(i)
        ans=float('inf')
        for v,p in pos.items():
            if len(p)<3:
                continue
            for i in range(len(p)-2):
                dis=2*(p[i+2]-p[i])
                if dis<ans:
                    ans=dis
        return ans if ans!=float('inf') else -1