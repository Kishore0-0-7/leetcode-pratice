class Solution:
    def minDeletionSize(self, strs):
        rows=len(strs)
        cols=len(strs[0])
        deleteVal=0
        for i in range(cols):
            for j in range(1,rows):
                if strs[j][i]<strs[j-1][i]:
                    deleteVal+=1
                    break
        return deleteVal