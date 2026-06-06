from collections import Counter
class Solution(object):
    def countWordOccurrences(self, chunks, queries):
        """
        :type chunks: List[str]
        :type queries: List[str]
        :rtype: List[int]
        """
        s="".join(chunks)
        fr=Counter()
        word=""
        n=len(s)
        for i in range(n):
            ch=s[i]
            if 'a'<=ch<='z':
                word+=ch
            elif ch=='-':
                if (i>0 and i<n-1 and 'a'<=s[i+1]<='z' and 'a'<=s[i-1]<='z'):
                    word+=ch
                else:
                    if word:
                        fr[word]+=1
                    word=""
            else:
                if word:
                    fr[word]+=1
                word=""
        if word:
            fr[word]+=1
        ans=[]
        for q in queries:
            ans.append(fr[q])
        return ans