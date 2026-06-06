class Solution(object):
    def validateCoupons(self, code, businessLine, isActive):
        """
        :type code: List[str]
        :type businessLine: List[str]
        :type isActive: List[bool]
        :rtype: List[str]
        """
        line_id={
            "electronics": 1,
            "grocery": 2,
            "pharmacy": 3,
            "restaurant": 4,
        }

        def ok_chars(s):
            return all(ch.isalnum() or ch=="_" for ch in s)

        def is_valid(i):
            if not isActive[i]:
                return False
            if not code[i]:
                isActive[i]=False
                return False
            if businessLine[i] not in line_id:
                isActive[i]=False
                return False
            if not ok_chars(code[i]):
                isActive[i]=False
                return False
            return True
        valid=[i for i in range(len(code)) if is_valid(i)]
        valid.sort(key=lambda i: (line_id[businessLine[i]], code[i]))
        return [code[i] for i in valid]