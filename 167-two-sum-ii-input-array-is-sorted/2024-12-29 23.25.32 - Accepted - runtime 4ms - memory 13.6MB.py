class Solution(object):
    def twoSum(self, numbers, target):
        ns={}
        for i in range(len(numbers)):
            t=target-numbers[i]
            if t in ns:
                return [ns[t]+1,i+1]
            ns[numbers[i]]=i
        return []