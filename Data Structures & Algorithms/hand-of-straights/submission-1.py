class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        hand = sorted(hand)
        while len(hand):
            start = hand.pop(0)
            for i in range(1, groupSize):
                if start + i not in hand:
                    return False
                hand.remove(start + i)
        return True