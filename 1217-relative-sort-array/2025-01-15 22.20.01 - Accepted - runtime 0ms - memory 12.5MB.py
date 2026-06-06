class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        freq = {}
        for num in arr1:
            if num in freq:
                freq[num]+=1
            else:
                freq[num]=1  
        res = []
        for num in arr2:
            res.extend([num]*freq[num])
            del freq[num]
        
        nums = freq.keys()
        nums.sort()
        for num in nums:
            res.extend([num]*freq[num])
        return res