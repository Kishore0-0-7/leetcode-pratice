class Solution(object):
    def stringMatching(self, words):
        n=len(words)
        st=set()
        words.sort(key=len)
        for i in range(n):
            for j in range(i+1,n):
                if words[i] in words[j]:
                    st.add(words[i])
        return list(st)