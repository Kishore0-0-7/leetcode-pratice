class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def is_prime(num):
            if num==1:
                return False
            for i in range(2,int(math.sqrt(num-1)+1)):
                if num%i==0:
                    return False
            return True
        c=0
        for i in range(len(nums)):
            if i%2==0:
                if is_prime(nums[i])==False:
                    c+=1
            elif i%2==1:
                if is_prime(nums[i])==True:
                    c+=1
        return c
                