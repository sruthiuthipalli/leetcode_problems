class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        a=max(candies)
        r=[]
        for i in candies:
            s=i+extraCandies
            if s>=a:
                r.append(True)
            else:
                r.append(False)
        return r   

        