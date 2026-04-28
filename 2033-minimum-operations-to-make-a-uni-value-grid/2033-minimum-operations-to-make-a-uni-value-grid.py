class Solution(object):
    def minOperations(self, grid, x):
        """
        :type grid: List[List[int]]
        :type x: int
        :rtype: int
        """
        arr=[]
        for row in grid:
            for val in row:
                arr.append(val)
        arr.sort()
        median=arr[len(arr)//2]
        operations=0
        for val in arr:
            if (val-arr[0])%x!=0:
                return -1
            operations+=abs(val-median)//x
        return operations