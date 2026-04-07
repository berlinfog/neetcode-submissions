class Solution:
    # 0 1 2 3 lens//2-1 lens//2
    # 0 1 2 len//2 len//2
    def isPalindrome(self, s: str) -> bool:

        s = s.lower()
        sn = ""
        for i in s:
            oi = ord(i)
            if oi >= ord('a') and oi <= ord('z'):
                sn += i
            elif oi >= ord('0') and oi <= ord('9'):
                sn += i

        lens = len(sn)
        isodd = False if lens % 2 == 0 else True
        startl = lens//2 if isodd else lens//2-1
        startr = lens//2
    
        print(str(startl)+" "+str(startr))
        while startl >= 0 and startr <= lens - 1:
            if sn[startl]!=sn[startr]:
                return False
            else:
                startl -= 1
                startr += 1
        return True

