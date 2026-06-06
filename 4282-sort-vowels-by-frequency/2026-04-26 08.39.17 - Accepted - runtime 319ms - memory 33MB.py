class Solution(object):
    def sortVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        from collections import Counter
        vowels=set('aeiou')
        pos=[]
        vl=[]
        for i,ch in enumerate(s):
            if ch  in vowels:
                pos.append(i)
                vl.append(ch)
        freq=Counter(vl)
        fi={}
        for i,ch in enumerate(s):
            if ch in vowels and ch not in fi:
                fi[ch]=i
        sorted_vowels=sorted(vl,key=lambda x:(-freq[x],fi[x]))
        res=list(s)
        for i,ch in zip(pos,sorted_vowels):
            res[i]=ch
        return "".join(res)