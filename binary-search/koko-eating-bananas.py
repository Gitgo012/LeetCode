import math
class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        left=1
        right=max(piles)
        while left<=right:
            mid=left+(right-left+1)//2
            hours=0
            for pile in piles:
                hours+=math.ceil(pile/mid)
            if hours<=h:
                right=mid-1
            elif hours>h:
                left=mid+1
        return left