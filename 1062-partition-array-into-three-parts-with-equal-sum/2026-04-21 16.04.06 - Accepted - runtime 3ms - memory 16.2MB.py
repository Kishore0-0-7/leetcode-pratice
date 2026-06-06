class Solution(object):
    def canThreePartsEqualSum(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        total_sum=sum(arr)
        if total_sum%3!=0:
            return False
        target=total_sum//3
        current_sum=0
        count=0
        for i in range(len(arr)-1):
            current_sum+=arr[i]
            if current_sum==target:
                current_sum=0
                count+=1
                if count==2:
                    return True
        return False