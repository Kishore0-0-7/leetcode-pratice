class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq=Counter(nums)
        dup=sum(1 for v in freq.values() if v>1)
        op=0
        i=0
        n=len(nums)
        while dup>0:
            op+=1
            for _ in range(3):
                if i==n:
                    return op
                    val=nums[i]
                    freq[val]-=1
                    if freq[val]==1:
                        dup-=1
                    elif freq[val]==0:
                        del freq[val]
                    i+=1
            return op