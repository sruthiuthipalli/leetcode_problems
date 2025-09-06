class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n=sorted(set(nums))
        nums[:]=n
        return len(nums)

        