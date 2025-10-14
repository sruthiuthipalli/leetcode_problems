class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        r=[]
        for n in nums1:
            f=False
            g=-1
            for i in range(len(nums2)):
                if nums2[i]==n:
                    f=True
                if f and nums2[i]>n:
                    g=nums2[i]
                    break
            r.append(g)
        return r          

        