class Solution(object):
    def minimumIndex(self, capacity, itemSize):
        """
        :type capacity: List[int]
        :type itemSize: int
        :rtype: int
        """
        s=-1
        for i in range(len(capacity)):
            if capacity[i]>=itemSize:
                s=s if s!=-1 and capacity[i]>=capacity[s] else i
        # print(s)
        return s
        