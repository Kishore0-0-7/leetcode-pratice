class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        st=sentence.split(" ")
        for i in range(len(st)):
            if st[i].startswith(searchWord):
                return i+1
        return -1
        