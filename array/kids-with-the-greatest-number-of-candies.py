class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        largest=max(candies)
        result=[]
        for i in range(len(candies)):
            if candies[i]+extraCandies>=largest:
                result.append(True)
            else:
                result.append(False)
        return result