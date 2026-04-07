from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # lens1 = len(s1)
        # lens2 = len(s2)
        # # 3 7
        # # 
        # for i in range(0,lens2 - lens1+1):
        #     if Counter(s1) == Counter(s2[i:i+lens1]):
        #         return True
        # return False
        dict1 = {}
        dict2 = {}
        l1 = len(s1)
        l2 = len(s2)
        for i in s1:
            dict1[i] = dict1.get(i,0) + 1
        for i in s2[:l1]:
            dict2[i] = dict2.get(i,0) + 1
        for k in range(l1,l2):
            if dict1 == dict2:
                return True

            if dict2[s2[k-l1]] == 1:
                del dict2[s2[k-l1]]
            else:
                dict2[s2[k-l1]] -= 1
            
            dict2[s2[k]] = dict2.get(s2[k],0) + 1
        return dict1 == dict2

            