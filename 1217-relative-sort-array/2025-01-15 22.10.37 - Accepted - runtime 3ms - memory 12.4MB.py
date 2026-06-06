class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        ans=[]
        for i in arr2:
            while i in arr1:
                ans.append(i)
                arr1.remove(i)
        return ans+sorted(arr1)