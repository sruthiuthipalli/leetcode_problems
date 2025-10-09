class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        a=[]
        for i in nums:
            c=0
            for j in nums:
                if i>j:
                    c+=1
            a.append(c)
        return a       
        