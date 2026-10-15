class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        list1=[]
        list2=[]
        for i in set(nums1):
            if i not in nums2:
                list1.append(i)
        for i in set(nums2):
            if i not in nums1:
                list2.append(i)
        return [list1,list2]