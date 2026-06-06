class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        st=[]
        for i in arr:
            if len(st)==0 or st[-1]<=i:
                st.append(i)
            else:
                ma=st[-1]
                if st and st[-1]>i:
                    ma=max(ma,st.pop())
                st.append(ma)
        return len(st)
        