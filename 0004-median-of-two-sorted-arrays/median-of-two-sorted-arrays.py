from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        new_list = []

        for m in range(len(nums1)):
            new_list.append(nums1[m])

        for n in range(len(nums2)):
            new_list.append(nums2[n])

        new_list = sorted(new_list)

        median = 0.0
        if len(new_list) % 2 == 0:
            median = (new_list[int((len(new_list)/2)-1)] +
                      new_list[int((len(new_list)/2))])/2
        else:
            median = new_list[int(len(new_list)//2)]
        return median
