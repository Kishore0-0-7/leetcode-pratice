class Solution(object):
    def canReach(self, arr, start):
        """
        :type arr: List[int]
        :type start: int
        :rtype: bool
        """
        if start<0 or start>=len(arr) or arr[start]<0 :
            return False
        if arr[start]==0:
            return True
        arr[start]=-arr[start]
        ans1=self.canReach(arr,start+arr[start])
        ans2=self.canReach(arr,start-arr[start])
        arr[start]=-arr[start]
        return ans1 or ans2