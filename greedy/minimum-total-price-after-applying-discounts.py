class Solution:
    def minPrice(self, prices: list[int], discounts: list[int]) -> float:
        prices.sort(reverse=True)
        discounts.sort(reverse=True)
        actual_price=[]
            
        for i in range(min(len(prices),len(discounts))):
            actual_price.append(prices[i] * (100 - discounts[i]) / 100)

        if len(prices)>len(discounts):
            actual_price+=prices[len(discounts):]
        return round(sum(actual_price),5)
        