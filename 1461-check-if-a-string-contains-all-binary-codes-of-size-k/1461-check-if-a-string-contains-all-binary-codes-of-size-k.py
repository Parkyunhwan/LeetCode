class Solution(object):
    def hasAllCodes(self, s, k):
        # k=2라면  00 01 10 11 이 있는지 확인 
        # k=3이라면 000 001 010 011 100 101 110 111 
        b_codes = set()
        for i in range(len(s) - k + 1):
            b_codes.add(s[i:i + k])
        return len(b_codes) == 2 ** k
            