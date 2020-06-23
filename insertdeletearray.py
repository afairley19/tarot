# duplicate zeros: given a fixed length array of integers, 
# duplicate each occurance of zero, shifting the remaining elements to the right

# Input: [1,0,2,3,0,4,5,0]
# Output: null
# Explanation: After calling your function, 
# the input array is modified to: [1,0,0,2,3,0,0,4]

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        # variable is 0 if the count of the item in the array = 0
        zeroes = arr.count(0)
        # n is the length of the array
        n = len(arr)
        # this loop starts at the end of the array
        for i in range(n - 1, -1, -1):
            # if item is located in the array we can append the value, otherwise ignore 
            # items that fall off in the shift
            if i + zeroes < n:
                arr[i + zeroes] = arr[i]
            if arr[i] == 0:
                zeroes -= 1
                if i + zeroes < n:
                    arr[i + zeroes] = 0

# merge sorted array: Given two sorted integer arrays nums1 and nums2,
# merge nums2 into nums1 as one sorted array.
# Input:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3
# Output: [1,2,2,3,5,6]

# The number of elements initialized in nums1 and nums2 are m and n respectively.
# You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # I have no idea
        while n > 0:
            if m <= 0 or nums2[n - 1] >= nums1[m - 1]:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1
            else:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1

# remove elememt
# Given an array nums and a value val, 
# remove all instances of that value in-place and return the new length.

class Solution:
    def removeElement(self, nums, val):
        # "nums" is the array, "val" is the value to be removed
        # while val is present in nums array = nums.remove(val)
        while val in nums:
            nums.remove(val)
        return len(nums)

# remove duplicates from sorted array
# Given a sorted array nums, remove the duplicates 
# in-place such that each element appear only once and return the new length.

class Solution:
    def removeDuplicates(self, nums):
        i = 0
        j = 1

        while j < len(nums):
            if nums[i] == nums[j]:
                j += 1
            else:
                i += 1
                nums[i] = nums[j]
        return (i + 1)

