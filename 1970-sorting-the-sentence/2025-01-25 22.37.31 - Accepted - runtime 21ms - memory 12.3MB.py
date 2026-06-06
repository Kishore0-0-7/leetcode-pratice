class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        lst=s.split()
        st=""
        for i in range(1,len(lst)+1):
            for w in lst:
                if w[-1]==str(i):
                    st+=" "+w[:-1]
        return st.strip()