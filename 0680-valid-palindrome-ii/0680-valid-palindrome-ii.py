class Solution(object):
    def validPalindrome(self, s):
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                l1, r1 = l + 1, r
                l2, r2 = l, r - 1
                left_s = s[l1:r1 + 1]
                right_s = s[l2:r2 + 1]
                if left_s == left_s[::-1]:
                    return True
                elif right_s == right_s[::-1]:
                    return True
                else:
                    return False
            l += 1
            r -= 1
        return True
        
            
        