class Solution(object):
    def earliestTime(self, tasks):
        maxi=tasks[0][0]+tasks[0][1]
        for i in range (len(tasks)):
                maxi=min(maxi,tasks[i][0]+tasks[i][1])
        return maxi