class Solution(object):
    def findXSum(self, nums, k, x):
        """
        :type nums: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        def x_sum(arr,x):
            d={}
            res=[]
            for i in nums:
                d[i]=arr.count(i)
            for i in d.keys():
                res.append([d[i],i])
            res.sort(reverse=True)
            f_res=[]
            for i in range(x):
                for j in range(res[i][0]):
                    f_res.append(res[i][1])
            return f_res
        n=len(nums)
        des=[]
        for i in range(n-k+1):
            des.append(sum(x_sum(nums[i:i+k],x)))
        return des