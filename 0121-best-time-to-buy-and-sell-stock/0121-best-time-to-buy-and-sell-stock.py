class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_element=0
        min_element=prices[0]
        n=len(prices)
        for i in range(1,n):
            max_element=max(max_element,prices[i]-min_element)
            min_element=min(min_element,prices[i])
        return max_element