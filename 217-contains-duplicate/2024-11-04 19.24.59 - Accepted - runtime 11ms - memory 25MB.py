class Solution(object):
    def containsDuplicate(self, nums):
        m=set()
        for i in nums:
            if i in m:
                return True
                break
            m.add(i)
        return False