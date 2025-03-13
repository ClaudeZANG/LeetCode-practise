# 1. You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

# Merge nums1 and nums2 into a single array sorted in non-decreasing order.

# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

# class Solution:
#     def merge(self, nums1, m, nums2, n):
#         p1 = m - 1
#         p2 = n - 1 
#         p = m + n - 1 

#         while p1 >= 0 and p2 >= 0:
#             if nums1[p1] > nums2[p2]:
#                 nums1[p] = nums1[p1]
#                 p1 -= 1
#             else:
#                 nums1[p] = nums2[p2]
#                 p2 -= 1
#             p -= 1

#         while p2 >= 0:
#             nums1[p] = nums2[p2]
#             p2 -= 1
#             p -= 1

# re-write 2025/Feb/22
# class Solution:
#     def merge(self, nums1, m, nums2, n):
#         p1, p2, p = m - 1, n - 1, m + n - 1

#         while p1 >= 0 and p2 >= 0:
#             if nums1[p1] > nums2[p2]:
#                 nums1[p] = nums1[p1]
#                 p1 -= 1
#             else:
#                 nums1[p] = nums2[p2]
#                 p2 -= 1
#             p -= 1

#         while p2 >= 0:
#             nums1[p] = nums2[p2]
#             p2 -= 1
#             p -= 1

# # re-write 2025/Feb/23
# class Solution:
#     def merge(self, nums1, m, nums2, n):
#         p1, p2, p = m - 1, n - 1, m + n - 1

#         while p1 >=0 and p2 >= 0:
#             if nums1[p1] > nums2[p2]:
#                 nums1[p] = nums1[p1]
#                 p1 -= 1
#             else:
#                 nums1[p] = nums2[p2]
#                 p2 -= 1
#             p -= 1

#         while p2 >= 0:
#             nums1[p] = nums2[p2]
#             p2 -= 1
#             p -= 1

# re-write 2025/Feb/25
# class Solution:
#     def merge(self, nums1, m, nums2, n):
#         p1, p2, p = m - 1, n - 1, m + n - 1
        
#         while p1 >= 0 and p2 >= 0:
#             if nums1[p1] > nums2[p2]:
#                 nums1[p] = nums1[p1]
#                 p1 -= 1
#             else:
#                 nums1[p] = nums2[p2]
#                 p2 -= 1
#             p -= 1
        
#         while p2 >= 0:
#             nums1[p] = nums2[p2]
#             p2 -= 1
#             p -= 1

# re-write 2025/Feb/27
# class Solution:
#     def merge(self, nums1, m, nums2, n):
#         p1, p2, p = m - 1, n - 1, m + n - 1

#         while p1 >= 0 and p2 >= 0:
#             if nums1[p1] > nums2[p2]:
#                 nums1[p] = nums1[p1]
#                 p1 -= 1
#             else:
#                 nums1[p] = nums2[p2]
#                 p2 -= 1
#             p -= 1
        
#         while p2 >= 0:
#             nums1[p] = nums2[p2]
#             p2 -= 1
#             p -= 1

# ------------------------------------------------------------

# 27. Remove Element
# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

# Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

# Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
# Return k.
# Custom Judge:

# The judge will test your solution with the following code:

# int[] nums = [...]; // Input array
# int val = ...; // Value to remove
# int[] expectedNums = [...]; // The expected answer with correct length.
#                             // It is sorted with no values equaling val.

# int k = removeElement(nums, val); // Calls your implementation

# assert k == expectedNums.length;
# sort(nums, 0, k); // Sort the first k elements of nums
# for (int i = 0; i < actualLength; i++) {
#     assert nums[i] == expectedNums[i];
# }
# If all assertions pass, then your solution will be accepted.

# Example 1:

# Input: nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2,_,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 2.
# It does not matter what you leave beyond the returned k (hence they are underscores).
# Example 2:

# Input: nums = [0,1,2,2,3,0,4,2], val = 2
# Output: 5, nums = [0,1,4,0,3,_,_,_]
# Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
# Note that the five elements can be returned in any order.
# It does not matter what you leave beyond the returned k (hence they are underscores).

# Constraints:

# 0 <= nums.length <= 100
# 0 <= nums[i] <= 50
# 0 <= val <= 100

# class Solution(object):
#     def removeElement(self, nums, val):
#         k = 0
#         for i in range(len(nums)):
#             if nums[i] != val:
#                 nums[k] = nums[i]
#                 k += 1
#         return k

# re-write 2025/Feb/24
# class Solution:
#     def removeElement(self, nums, val):
#         k = 0
#         for i in range(len(nums)):
#             if nums[i] != val:
#                 nums[k] = nums[i]
#                 k += 1
#         return k

# re-write 2025/Feb/25
# class Solution:
#     def removeElement(self, nums, val):
#         k = 0
#         for i in range(len(nums)):
#             if nums[i] != val:
#                 nums[k] = nums[i]
#                 k += 1
#         return k

# re-write 2025/Feb/25
# class Solution:
#     def removeElement(self, nums, val):
#         k = 0
#         for i in range(len(nums)):
#             if nums[i] != val:
#                 nums[k] = nums[i]
#                 k += 1
#         return k

# -------------------------------------------

# 26. Remove Duplicates from Sorted Array
# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

# Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

# Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
# Return k.
# Custom Judge:

# The judge will test your solution with the following code:

# int[] nums = [...]; // Input array
# int[] expectedNums = [...]; // The expected answer with correct length

# int k = removeDuplicates(nums); // Calls your implementation

# assert k == expectedNums.length;
# for (int i = 0; i < k; i++) {
#     assert nums[i] == expectedNums[i];
# }

# int val = ...; // Value to remove
# int[] expectedNums = [...]; // The expected answer with correct length.
#                             // It is sorted with no values equaling val.

# int k = removeElement(nums, val); // Calls your implementation

# assert k == expectedNums.length;
# sort(nums, 0, k); // Sort the first k elements of nums
# for (int i = 0; i < actualLength; i++) {
#     assert nums[i] == expectedNums[i];
# }
# If all assertions pass, then your solution will be accepted.

# Example 1:

# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).

# It does not matter what you leave beyond the returned k (hence they are underscores).
# Example 2:

# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
# Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).

# Note that the five elements can be returned in any order.
# It does not matter what you leave beyond the returned k (hence they are underscores).

# Constraints:

# 1 <= nums.length <= 3 * 104
# -100 <= nums[i] <= 100
# nums is sorted in non-decreasing order.

# class Solution(object):
#     def removeDuplicates(self, nums):
#         k = 0
#         for i in range(1, len(nums)):
#             if nums[i] != nums[k]:
#                 k += 1
#                 nums[k] = nums[i]                   

#         return k + 1

# re-write 2025/Feb/24
# class Solution:
#     def removeDuplicates(self, nums):
#         k = 0
#         for i in range(1, len(nums)):
#             if nums[i] != nums[k]:
#                 k += 1
#                 nums[k] = nums[i]
#         return k + 1

# re-write 2025/Feb/25
# class Solution:
#     def removeDuplicates(self, nums):
#         k = 0
#         for i in range(1, len(nums)):
#             if nums[k] != nums[i]:
#                 k += 1
#                 nums[k] = nums[i]
#         return k + 1 

# re-write 2025/Feb/27
# class Solution:
#     def removeDuplicates(self, nums):
#         k = 0
#         for i in range(1, len(nums)):
#             if nums[k] != nums[i]:
#                 k += 1
#                 nums[k] = nums[i]
#         return k + 1

# -----------------------------------------------

# 80. Remove Duplicates from Sorted Array II
# Medium

# Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same.

# Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

# Return k after placing the final result in the first k slots of nums.

# Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

# Custom Judge:

# int[] nums = [...]; // Input array
# int[] expectedNums = [...]; // The expected answer with correct length

# int k = removeDuplicates(nums); // Calls your implementation

# assert k == expectedNums.length;
# for (int i = 0; i < k; i++) {
#     assert nums[i] == expectedNums[i];
# }
# If all assertions pass, then your solution will be accepted. 

# Example 1:

# Input: nums = [1,1,1,2,2,3]
# Output: 5, nums = [1,1,2,2,3,_]
# Explanation: Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).
# Example 2:

# Input: nums = [0,0,1,1,1,1,2,3,3]
# Output: 7, nums = [0,0,1,1,2,3,3,_,_]
# Explanation: Your function should return k = 7, with the first seven elements of nums being 0, 0, 1, 1, 2, 3 and 3 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).
 
# Constraints:

# 1 <= nums.length <= 3 * 104
# -104 <= nums[i] <= 104
# nums is sorted in non-decreasing order.

# class Solution(object):
#     def removeDuplicates(self, nums):
#         k = 2

#         for i in range(2, len(nums)):
#             if nums[i] != nums[k - 2]:
#                 nums[k] = nums[i]
#                 k += 1

#         return k

# re-write 2025/Feb/24      
# class Solution:
#     def removeDuplicates(self, nums):
#         k = 2
#         for i in range(2, len(nums)):
#             if nums[i] != nums[k - 2]:
#                 nums[k] = nums[i] # put to k position
#                 k += 1
#         return k

# re-write 2025/Feb/25
# class Solution:
#     def removeDuplicates(self, nums):
#         k = 2
#         for i in range(2, len(nums)):
#             if nums[i] != nums[k - 2]:
#                 nums[k] = nums[i]
#                 k += 1
#         return k

# re-write 2025/Feb/27
# class Solution:
#     def removeDuplicates(self, nums):
#         k = 2
#         for i in range(2, len(nums)):
#             if nums[i] != nums[k - 2]:
#                 nums[k] = nums[i]
#                 k += 1
#         return k

# ------------------------------------------------------------

# 169. Majority Element
# Easy
# Topics
# Companies
# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than (n / 2) times. You may assume that the majority element always exists in the array.

# Example 1:
# Input: nums = [3,2,3]
# Output: 3

# Example 2:
# Input: nums = [2,2,1,1,1,2,2]
# Output: 2

# Constraints:
# n == nums.length
# 1 <= n <= 5 * 104
# -109 <= nums[i] <= 109

# class Solution:
#     def majorityElement(self, nums):
#         nums.sort()
#         return nums[len(nums) // 2]

# re-write 2025/Feb/25
# class Solution:
#     def majorityElement(self, nums):
#         nums.sort()
#         return nums[len(nums) // 2]

# re-write 2025/Feb/26 - 1
# class Solution:
#     def majorityElement(self, nums):
#         nums.sort()
#         return nums[len(nums) // 2]

# re-write 2025/Feb/26 - 2
# class Solution:
#     def majorityElement(self, nums):
#         nums.sort()
#         return nums[len(nums) // 2]

# re-write 2025/Feb/27 -1
# class Solution:
#     def majorityElement(self, nums):
#         nums.sort()
#         return nums[len(nums) // 2]

# re-write 2025/Feb/27 -2
# class Solution:
#     def majorityElement(self, nums):
#         nums.sort()
#         return nums[len(nums) // 2]

# re-write 2025/Feb/27 -3
# class Solution:
#     def majorityElement(self, nums):
#         nums.sort()
#         return nums[len(nums) // 2]

# re-write 2025/Feb/27 -4
# class Solution:
#     def majorityElement(self, nums):
#         nums.sort()
#         return nums[len(nums) // 2]

# re-write 2025/Feb/27 -5
# class Solution:
#     def majorityElement(self, nums):
#         nums.sort()
#         return nums[len(nums) // 2]

# re-write 2025/Feb/27 -6
# class Solution:
#     def majorityElement(self, nums):
#         nums.sort()
#         return nums[len(nums) // 2]

# re-write 2025/Feb/27 -7
# class Solution:
#     def majorityElement(self, nums):
#         nums.sort()
#         return nums[len(nums) // 2]

# re-write 2025/Feb/27 -8
# class Solution:
#     def majorityElement(self, nums):
#         nums.sort()
#         return nums[len(nums) // 2]

# ------------------------------------------

# 189. Rotate Array
# Medium
# Topics
# Companies
# Hint
# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative. 

# Example 1:

# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]
# Example 2:

# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]
# Explanation: 
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]
 
# Constraints:

# 1 <= nums.length <= 105
# -231 <= nums[i] <= 231 - 1
# 0 <= k <= 105

# class Solution(object):
#     def rotate(self, nums, k):
#         n = len(nums)
#         k %= n
#         nums[:] = nums[-k:] + nums[:-k]

# re-write 2025/Feb/27 - 1
# class Solution(object):
#     def rotate(self, nums, k):
#         n = len(nums)
#         k %= n
#         nums[:] = nums[-k:] + nums[:-k]

# re-write 2025/Feb/27 - 2
# class Solution:
#     def rotate(self, nums, k):
#         n = len(nums)
#         k %= n
#         nums[:] = nums[-k:] + nums[:-k]

# re-write 2025/Feb/28 -1
# class Solution:
#     def rotate(self, nums, k):
#         n = len(nums)
#         k %= n
#         if k == 0:
#             return
#         nums[:] = nums[-k:] + nums[:-k]

# re-write 2025/Feb/28 -2
# class Solution:
#     def rotate(self, nums, k):
#         n = len(nums)
#         k %= n
#         if k == 0:
#             return
        
#         nums[:] = nums[-k:] + nums[:-k]

# ---------------------------

# 121. Best Time to Buy and Sell Stock
# Easy
# Topics
# Companies
# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
# Example 2:

# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.

# Constraints:

# 1 <= prices.length <= 105
# 0 <= prices[i] <= 104

# class Solution:
#     def maxProfit(self, prices):
#         min_price, max_profit = float('inf'), 0
        
#         for price in prices:
#             min_price = min(min_price, price)
#             max_profit = max(max_profit, price - min_price)
        
#         return  max_profit

# re-write 2025/Feb/28 -1
# class Solution:
#     def maxProfit(self, prices):
#         min_price, max_profit = float('inf'), 0

#         for price in prices:
#             min_price = min(min_price, price)
#             max_profit = max(max_profit, price - min_price)
        
#         return max_profit

# re-write 2025/Feb/28 -2
# class Solution:
#     def maxProfit(self, prices):
#         min_price, max_profit = float('inf'), 0

#         for price in prices:
#             min_price = min(min_price, price)
#             max_profit = max(max_profit, price - min_price)

#         return max_profit
    
# re-write 2025/Feb/28 -3
# class Solution:
#     def maxProfit(self, prices):
#         min_price, max_profit = float('inf'), 0

#         for price in prices:
#             min_price = min(min_price, price)
#             max_profit = max(max_profit, price - min_price)
        
#         return max_profit

# -----------------------------------

# 122. Best Time to Buy and Sell Stock II
# Medium # Topics # Companies
# You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
# On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.
# Find and return the maximum profit you can achieve.

# Example 1:
# Input: prices = [7,1,5,3,6,4]
# Output: 7
# Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
# Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
# Total profit is 4 + 3 = 7.

# Example 2:
# Input: prices = [1,2,3,4,5]
# Output: 4
# Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
# Total profit is 4.

# Example 3:
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.
 
# Constraints:
# 1 <= prices.length <= 3 * 104
# 0 <= prices[i] <= 104

# class Solution:
#     def maxProfit(self, prices):
#         return sum(max(prices[i] - prices[i - 1], 0) for i in range (1, len(prices)))

# re-write 2025/Mar/1 -1
# class Solution:
#     def maxProfit(self, prices):
#         return sum(max(prices[i] - prices[i - 1], 0) for i in range (1, len(prices)))

# re-write 2025/Mar/1 -2
# class Solution:
#     def maxProfit(self, prices):
#         return sum(max(prices[i] - prices[i - 1], 0) for i in range (1, len(prices)))

# -----------------------------------

# 55. Jump Game
# Medium # Topics # Companies
# You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.
# Return true if you can reach the last index, or false otherwise.

# Example 1:
# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

# Example 2:
# Input: nums = [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

# Constraints:
# 1 <= nums.length <= 104
# 0 <= nums[i] <= 105

# class Solution:
#     def canJump(self, nums):
#         max_reach = 0
#         for i in range(len(nums)):
#             if i > max_reach:
#                 return False
#             max_reach = max(max_reach, i + nums[i])
#             if max_reach >= len(nums) - 1:
#                 return True
#         return True

# re-write 2025/Mar/5 - 1
# class Solution:
#     def canJump(self, nums):
#         max_reach = 0
#         for i in range (len(nums)):
#             if i > max_reach:
#                 return False
#             max_reach = max(max_reach, i + nums[i])
#             if max_reach >= len(nums) - 1:
#                 return True

# re-write 2025/Mar/5 - 2
# class Solution:
#     def canJump(self, nums):
#         max_reach = 0
#         for i in range (len(nums)):
#             if i > max_reach:
#                 return False
#             max_reach = max(max_reach, i + nums[i])
#             if max_reach >= len(nums) - 1:
#                 return True
            

# re-write 2025/Mar/5 - 3
# class Solution:
#     def canJump(self, nums):
#         max_reach = 0
#         for i in range (len(nums)):
#             if i > max_reach:
#                 return False
#             max_reach = max(max_reach, i + nums[i])
#             if max_reach >= len(nums) - 1:
#                 return True

# -----------------------------------

# 45. Jump Game II
# Medium # Topics # Companies
# You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].
# Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:

# 0 <= j <= nums[i] and
# i + j < n
# Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].

# Example 1:
# Input: nums = [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.

# Example 2:
# Input: nums = [2,3,0,1,4]
# Output: 2

# Constraints:
# 1 <= nums.length <= 104
# 0 <= nums[i] <= 1000
# It's guaranteed that you can reach nums[n - 1].

# class Solution:
#     def jump(self, nums: list[int]) -> int:
#         jumps = 0
#         maxReach = 0
#         end = 0

#         for i in range(len(nums) - 1):
#             maxReach = max(maxReach, i + nums[i])
#             if i == end:
#                 jumps += 1
#                 end = maxReach
#                 if end >= len(nums) - 1:
#                     break
#         return jumps

# class Solution:
#     def jump(self, nums: list[int]) -> int:
#         jumps = 0
#         maxReach = 0
#         end = 0

#         for i in range (len(nums)):
#             maxReach = max(maxReach, i + nums[i])
#             if i == end:
#                 jumps += 1
#                 end = maxReach
#                 if end >= len(nums) - 1:
#                     break
#         return jumps

# re-write 2025/Mar/6 - 1
# class Solution:
#     def jump(self, nums): # leetcode python2
#         jumps = 0
#         maxReach = 0
#         end = 0

#         for i in range (len(nums) - 1):
#             maxReach = max(maxReach, i + nums[i])
#             if end == i:
#                 jumps += 1
#                 end = maxReach
#                 if end >= len(nums) - 1:
#                     break
#         return jumps

# re-write 2025/Mar/6 - 2
# class Solution:
#     def jump(self, nums):
#         maxReach = 0
#         jumps = 0
#         end = 0

#         for i in range (len(nums) - 1):
#             maxReach = max(maxReach, i + nums[i])
#             if i == end:
#                 jumps += 1
#                 end = maxReach
#                 if end >= len(nums) - 1:
#                     break
#         return jumps

# re-write 2025/Mar/6 - 3
# class Solution:
#     def jump(self, nums):
#         maxReach = 0
#         end = 0
#         jumps = 0

#         for i in range (len(nums) - 1):
#             maxReach = max(maxReach, i + nums[i])
#             if i == end:
#                 jumps += 1
#                 end = maxReach
#                 if end >= len(nums) - 1:
#                     break
#         return jumps

# -----------------------------------

# 274. H-Index
# Medium # Topics # Companies 
# Hint
# Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, return the researcher's h-index.
# According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of h such that the given researcher has published at least h papers that have each been cited at least h times.

# Example 1:
# Input: citations = [3,0,6,1,5]
# Output: 3
# Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively.
# Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, their h-index is 3.

# Example 2:
# Input: citations = [1,3,1]
# Output: 1

# Constraints:
# n == citations.length
# 1 <= n <= 5000
# 0 <= citations[i] <= 1000

# class Solution:
#     def hIndex(self, citations):
#         citations.sort(reverse=True)
#         h = 0

#         for i, citation in enumerate(citations):
#             if citation >= i + 1:
#                 h = i + 1
#             else:
#                 break
        
#         return h

# re-write 2025/Mar/6 - 1
# class Solution:
#     def hIndex(self, citations):
#         citations.sort(reverse = True)
#         h = 0

#         for i, citation in enumerate(citations):
#             if citation >= i + 1:
#                 h = i + 1
#             else:
#                 break
#         return h

# re-write 2025/Mar/6 - 2
# class Solution:
#     def hIndex(self, citations):
#         citations.sort(reverse = True)
#         h = 0

#         for i, citation in enumerate(citations):
#             if citation >= i + 1:
#                 h = i + 1
#             else:
#                 break
#         return h

# re-write 2025/Mar/6 - 3
# class Solution:
#     def hIndex(self, citations):
#         citations.sort(reverse = True)
#         h = 0

#         for i, citation in enumerate(citations):
#             if citation >= i + 1:
#                 h = i + 1
#             else:
#                 break
#         return h

# re-write 2025/Mar/8 - 1
# class Solution:
#     def hIndex(self, citations):
#         citations.sort(reverse = True)
#         h = 0

#         for i, citation in enumerate(citations):
#             if citation >= i + 1:
#                 h = i + 1
#             else:
#                 break
#         return h
    
# re-write 2025/Mar/8 - 2
# class Solution:
#     def hIndex(self, citations):
#         citations.sort()
#         h = 0
#         n = len(citations)

#         for i, citation in enumerate(citations):
#             if citation >= n - i:
#                 h =  n - i
#                 break
#         return h

# re-write 2025/Mar/8 - 3
# class Solution:
#     def hIndex(self, citations):
#         citations.sort(reverse = True)
#         h = 0

#         for i, citation in enumerate(citations):
#             if citation >= i + 1:
#                 h = i + 1
#             else:
#                 break
#         return h


# re-write 2025/Mar/8 - 4
# class Solution:
#     def hIndex(self, citations):
#         citations.sort()
#         h = 0
#         n = len(citations)

#         for i, citation in enumerate(citations):
#             if citation >= n - i:
#                 h = n - i
#                 break
#         return h

# re-write 2025/Mar/8 - 5
# class Solution:
#     def hIndex(self, citations):
#         citations.sort(reverse = True)
#         h = 0

#         for i, citation in enumerate(citations):
#             if citation >= i + 1:
#                 h = i + 1
#             else:
#                 break
#         return h

# re-write 2025/Mar/8 - 6
# class Solution:
#     def hIndex(self, citations):
#         citations.sort()
#         h = 0
#         n = len(citations)

#         for i, citation in enumerate(citations):
#             if citation >= n - i:
#                 h = n - i
#                 break
#         return h

# re-write 2025/Mar/8 - 7
# class Solution:
#     def hIndex(self, citations):
#         citations.sort(reverse = True)
#         h = 0

#         for i, citation in enumerate(citations):
#             if citation >= i + 1:
#                 h = i + 1
#             else:
#                 break
#         return h

# re-write 2025/Mar/8 - 8
# class Solution:
#     def hIndex(self, citations):
#         citations.sort()
#         n = len(citations)
#         h = 0

#         for i, citation in enumerate(citations):
#             if citation >= n - i:
#                 h = n - i
#                 break
#         return h

# -----------------------------------

# 380. Insert Delete GetRandom O(1)
# Medium # Topics # Companies

# Implement the RandomizedSet class:
# RandomizedSet() Initializes the RandomizedSet object.
# bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
# bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
# int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
# You must implement the functions of the class such that each function works in average O(1) time complexity.

# Example 1:
# Input
# ["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
# [[], [1], [2], [2], [], [1], [2], []]
# Output
# [null, true, false, true, 2, true, false, 2]

# Explanation
# RandomizedSet randomizedSet = new RandomizedSet();
# randomizedSet.insert(1); // Inserts 1 to the set. Returns true as 1 was inserted successfully.
# randomizedSet.remove(2); // Returns false as 2 does not exist in the set.
# randomizedSet.insert(2); // Inserts 2 to the set, returns true. Set now contains [1,2].
# randomizedSet.getRandom(); // getRandom() should return either 1 or 2 randomly.
# randomizedSet.remove(1); // Removes 1 from the set, returns true. Set now contains [2].
# randomizedSet.insert(2); // 2 was already in the set, so return false.
# randomizedSet.getRandom(); // Since 2 is the only number in the set, getRandom() will always return 2.

# Constraints:
# -231 <= val <= 231 - 1
# At most 2 * 105 calls will be made to insert, remove, and getRandom.
# There will be at least one element in the data structure when getRandom is called.

# import random

# class RandomizedSet:
#     def __init__(self):
#         self.list = []  # Stores all elements
#         self.map = {}   # Maps value to its index in the list

#     def insert(self, val: int) -> bool:
#         """Insert an element into the set. Returns True if inserted, False if it already exists. O(1) complexity."""
#         if val in self.map:
#             return False
#         self.map[val] = len(self.list)
#         self.list.append(val)
#         return True

#     def remove(self, val: int) -> bool:
#         """Remove an element from the set. Returns True if removed, False if not present. O(1) complexity."""
#         if val not in self.map:
#             return False
        
#         index = self.map[val]  # Get the index of the element to remove
#         last_element = self.list[-1]  # Get the last element of the list

#         # Swap the element to be removed with the last element
#         self.list[index] = last_element
#         self.map[last_element] = index  # Update the index of the last element in the map

#         # Remove the last element from the list to maintain compactness
#         self.list.pop()
#         del self.map[val]

#         return True

#     def getRandom(self) -> int:
#         """Return a random element from the set. O(1) complexity."""
#         return random.choice(self.list)

# re-write 2025/Mar/8 - 1
# import random

# class RandomizedSet:
#     def __init__(self):
#         self.list = []
#         self.map = {}

#     def insert(self, val):
#         if val in self.map:
#             return False
#         self.map[val] = len(self.list)
#         self.list.append(val)
#         return True

#     def remove(self, val):
#         if val not in self.map:
#             return False
#         index = self.map[val]
#         last_element = self.list[-1]

#         self.list[index] = last_element
#         self.list.pop()

#         self.map[last_element] = index
#         del self.map[val]

#         return True
    
#     def getRandom(self):
#         return random.choice(self.list)

# re-write 2025/Mar/9 - 1
# import random

# class Solution:
#     def __init__(self):
#         self.list = []
#         self.map = {}

#     def insert(self, val):
#         if val in self.map:
#             return False
#         self.map[val] = len(self.list)
#         self.list.append(val)
#         return True

#     def remove(self, val):
#         if val not in self.map:
#             return False
#         index = self.map[val]
#         last_element = self.list[-1]

#         self.list[index] = last_element
#         self.map[last_element] = index

#         self.list.pop()
#         del self.map[val]

#         return True
    
#     def getRandom(self):
#         return random.choice(self.list)
    
# re-write 2025/Mar/9 - 2
# import random
# class Solution:  # class RandomizedSet()
#     def __init__(self):
#         self.list = []
#         self.map = {}

#     def insert(self, val):
#         if val in self.map:
#             return False
        
#         self.map[val] = len(self.list)
#         self.list.append(val)
        
#         return True
    
#     def remove(self, val):
#         if val not in self.map:
#             return False
        
#         '''
#         [0: 0, 10: 1, 20: 2, 30: 3]
#         remove val == 10

#         1 = self.map[10]
#         30 = self.list[-1]

#         [0: 0, 30: 1, 20: 2, 30: 3]
#         [0: 0, 10: 1, 20: 2, 30: 1]

#         [0: 0, 30: 1, 20: 2]
#         [0: 0, 20: 2, 30: 1]

#         '''
#         index = self.map[val]
#         last_element = self.list[-1]

#         self.list[index] = last_element
#         self.map[last_element] = index

#         self.list.pop()
#         del self.map[val]

#         return True
    
#     def getRandom(self):
#         return random.choice(self.list)
    
# re-write 2025/Mar/9 - 3
# import random
# class Solution:
#     def __init__(self):
#         self.list = []
#         self.map = {}
    
#     def insert(self, val):
#         if val in self.map:
#             return False
        
#         self.map[val] = len(self.list)
#         self.list.append(val)
#         return True
    
#     def remove(self, val):
#         if val not in self.map:
#             return False
        
#         index = self.map[val]
#         last_element = self.list[-1]

#         self.list[index] = last_element
#         self.map[last_element] = index

#         self.list.pop()
#         del self.map[val]

#         return True
    
#     def getRandom(self):
#         return random.choice(self.list)

# re-write 2025/Mar/11 - 1
# import random

# class RandomizedSet():
#     def __init__(self):
#         self.list = []
#         self.map = {}
        
#     def insert(self, val):
#         if val in self.map:
#             return False
#         self.map[val] = len(self.list)
#         self.list.append(val)

#         return True
    
#     def remove(self, val):
#         if val not in self.map:
#             return False
#         index = self.map[val]
#         last_element = self.list[-1]

#         self.list[index] = last_element
#         self.map[last_element] = index

#         self.list.pop()
#         del self.map[val]

#         return True
    
#     def getRandom(self):
#         return random.choice(self.list)

# re-write 2025/Mar/11 - 2
# import random

# class RandomizedSet():
#     def __init__(self):
#         self.list = []
#         self.map = {}

#     def insert(self, val):
#         if val in self.map:
#             return False
        
#         self.map[val] = len(self.list)
#         self.list.append(val)

#         return True
    
#     def remove(self, val):
#         if val not in self.map:
#             return False
        
#         index = self.map[val]
#         last_element = self.list[-1]

#         self.list[index] = last_element
#         self.map[last_element] = index

#         self.list.pop()
#         del self.map[val]

#         return True
    
#     def getRandom(self):
#         return random.choice(self.list)

# re-write 2025/Mar/12 - 1
# import random
# class RandomizedSet():
#     def __init__(self):
#         self.list = []
#         self.map = {}

#     def insert(self, val):
#         if val in self.map:
#             return False
#         self.map[val] = len(self.list)
#         self.list.append(val)
#         return True
    
#     def remove(self, val):
#         if val not in self.map:
#             return False
#         index = self.map[val]
#         last_element = self.list[-1]

#         self.list[index] = last_element
#         self.map[last_element] = index

#         self.list.pop()
#         del self.map[val]

#         return True
    
#     def getRandom(self):
#         return random.choice(self.list)

# re-write 2025/Mar/12 - 2
# import random

# class RandomizedSet:
#     def __init__(self):
#         self.list = []
#         self.map = {}

#     def insert(self, val):
#         if val in self.map:
#             return False
        
#         self.map[val] = len(self.list)
#         self.list.append(val)

#         return True
    
#     def remove(self, val):
#         if val not in self.map:
#             return False
        
#         index = self.map[val]
#         last_element = self.list[-1]

#         self.list[index] = last_element
#         self.map[last_element] = index

#         self.list.pop()
#         del self.map[val]

#         return True
    
#     def getRandom(self):
#         return random.choice(self.list)

# re-write 2025/Mar/12 - 3
# import random
# class RandomizedSet:
#     def __init__(self):
#         self.list = []
#         self.map = {}

#     def insert(self, val):
#         if val in self.map:
#             return False
        
#         self.map[val] = len(self.list)
#         self.list.append(val)
#         return True
    
#     def remove(self, val):
#         if val not in self.map:
#             return False
        
#         index = self.map[val]
#         last_element = self.list[-1]

#         self.list[index] = last_element
#         self.map[last_element] = index

#         self.list.pop()
#         del self.map[val]
#         return True

#     def getRandom(self):
#         return random.choice(self.list)

# -----------------------------------

# 238. Product of Array Except Self
# Medium # Topics # Companies

# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.

# Example 1:
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]

# Example 2:
# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]

# Constraints:
# 2 <= nums.length <= 105
# -30 <= nums[i] <= 30
# The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.
 
# Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)

from typing import List

def productExceptSelf(nums: List[int]) -> List[int]:
    n = len(nums)
    answer = [1] * n  # Initialize the answer array with 1s

    # Step 1: Compute prefix product for each element (left to right)
    prefix = 1
    for i in range(n):
        answer[i] = prefix
        prefix *= nums[i]  # Update prefix product

    # Step 2: Compute suffix product and multiply with prefix (right to left)
    suffix = 1
    for i in range(n - 1, -1, -1):
        answer[i] *= suffix  # Multiply suffix with current answer
        suffix *= nums[i]  # Update suffix product

    return answer
