class Solution(object):
    def minSwaps(self, nums, forbidden):
        """
        :type nums: List[int]
        :type forbidden: List[int]
        :rtype: int
        """
        n=len(nums)
        val_counts={}
        for x in nums:
            val_counts[x]=val_counts.get(x,0)+1
        for val,count in val_counts.items():
            forbidden_count=sum(1 for f in forbidden if f==val)
            if count>(n-forbidden_count):
                return -1
        res_nums=list(nums)
        swaps_count=0
        for i in range(n):
            if res_nums[i]==forbidden[i]:
                for j in range(i+1,n):
                    if res_nums[j]==forbidden[j]:
                       if res_nums[j]!=forbidden[i] and res_nums[i]!=forbidden[j]:
                          res_nums[i],res_nums[j]=res_nums[j],res_nums[i]
                          swaps_count+=1
                          break
                for i in range(n):
            if res_nums[i]==forbidden[i]:
                if i==j:
                    continue
                if res_nums[j]!=forbidden[i]and res_nums[i]!=forbidden[j]:
                    res_nums[i],res_nums[j]=res_nums[j],res_nums[i]
                    swaps_count+=1
                    break 
        for i in range(n):
            if res_nums[i]==forbidden[i]:
                return -1
        return swaps_count

















                
        # bad=[i for i in range(n) if nums[i]==forbidden[i]]
        # if not bad:
        #     return 0
        # self.min_s=float('inf')
        # def solve(idx,current_nums,swaps):
        #     if swap>=self.min_s:
        #         return
        #     while idx<n and current_nums[idx]!=forbidden[idx]:
        #         idx+=1
        #     if idx==n:
        #         self.min_s=min(self.min_s,swaps)
        #         return
        #     for j in range(n):
        #         if i!=j:
        #             if current_nums[j]!=forbidden[idx]and current_nums[idx]!=forbidden[j]:
        #                 current_nums[idx],current_nums[j]=current_nums[j],current_nums[idx]
        #                 solve(idx+1,current_nums,swap+1)
        #                 current_nums[idx],current_nums[j]=current_nums[j],current_nums[idx]
        #     res_nums=list(nums)
        #     swaps_count=0
        #     for i in range(n):
        #         if res_nums[i]==forbidden[i]:
        #             for j in range(n):
        #                 if res_nums[j]!=forbidden[i]and res_nums[i]!=forbidden[j]:
        #                     res_nums[i],res_nums[j]=res+nums[j],res_nums[i]
        #                     swaps_count+=1
        #                     break
        #     for i in range(n):
        #         if res_nums[i]==forbidden[i]:
        #             return -1
        #     return swaps_count