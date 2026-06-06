class Solution(object):
    def isInterleave(self, s1, s2, s3):
        if(len(s1) == 0 and len(s2) == 0 and len(s3) == 1):
            return False
        if(len(s1) == 1 and len(s2) == 0 and len(s3) == 1):
            if(s1[0]==s3[0]):
                return true
            return False
        if(len(s1) == 0 and len(s2) == 1 and len(s3) == 0):
            if(s2[0]==s3[0]):
                return true
            return False
        i =0
        fIndex,sIndex =0,0
        while(i <len(s3) and fIndex <len(s1) and sIndex <len(s2)):
            if(s3[i] == s1[fIndex]):
                fIndex +=1
            elif(s3[i] == s2[sIndex]):
                sIndex +=1
            else:
                return False
            i +=1
        return True