class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        pro=0
        low=prices[0]
        for i in range(1,len(prices)):
            temp=prices[i]-low
            pro=max(pro,temp)
            low=min(low,prices[i])
        return pro    


        