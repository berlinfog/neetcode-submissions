from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # 1，2，2，3，3，4，4，5
        # then gp = len(hand) / groupsize
        # put like hand[0:gp] to a array
        # and then iterate to find which group to add and update the array?
        # but iterate ...  groupsize * n like this time complex and on space complex
        lh = len(hand)
        if lh % groupSize != 0:
            return False
        count = Counter(hand)
        sorted_keys = sorted(count.keys())
        for key in sorted_keys:
            if count[key] > 0: 
                start_count = count[key] # must above this value

                for i in range(key, key+groupSize):
                    if count[i] < start_count:
                        return False
                    count[i] -= start_count
        return True