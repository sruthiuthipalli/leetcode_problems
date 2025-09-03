class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
       a=len(set(nums))
       b=len(nums)
       return b!=a
        