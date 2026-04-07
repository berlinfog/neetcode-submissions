from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        lens1 = len(s1)
        lens2 = len(s2)
        # 3 7
        # 
        for i in range(0,lens2 - lens1+1):
            if Counter(s1) == Counter(s2[i:i+lens1]):
                return True
        return False

            