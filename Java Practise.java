//  # 1. You are given two integer arrays nums1 and nums2, sorted in non - decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

// # Merge nums1 and nums2 into a single array sorted in non - decreasing order.

// # The final sorted array should not be returned by the function, but instead be stored inside the array nums1.To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored.nums2 has a length of n.

// import java.util.Arrays;

// public class Solution {
//     public void merge(int[] nums1, int m, int[] nums2, int n) {
//         int p1 = m - 1;
//         int p2 = n - 1;
//         int p = m + n - 1;

//         while (p1 >=0 && p2 >= 0) {
//             if (nums1[p1] > nums2[p2]) {
//                 nums1[p] = nums1[p1];
//                 p1--;
//             } else {
//                 nums1[p] = nums2[p2];
//                 p2--;
//             }
//             p--;
//         }

//         while (p2 >= 0) {
//             nums1[p] = nums2[p2];
//             p2--;
//             p--;
//         }
//     }
// }

// re-write 2025/Feb/22
// public class Solution {
//     public void merge(int[] nums1, int m, int[] nums2, int n) {
//         int p1 = m - 1;
//         int p2 = n - 1;
//         int p = m + n - 1;

//         while (p1 >= 0 && p2 >= 0) {
//             if (nums1[p1] > nums2[p2]) {
//                 nums1[p] = nums1[p1];
//                 p1--;
//             } else {
//                 nums1[p] = nums2[p2];
//                 p2--;
//             }
//             p--;
//         }

//         while (p2 >= 0) {
//             nums1[p] = nums2[p2];
//             p2--;
//             p--;
//         }
//     }
// }

// re-write 2025/Feb/23
// public class Solution {
//     public void merge(int[] nums1, int m, int[] nums2, int n) {
//         int p1 = m - 1;
//         int p2 = n - 1;
//         int p = m + n - 1;

//         while (p1 >= 0 && p2 >= 0) {
//             if (nums1[p1] > nums2[p2]) {
//                 nums1[p] = nums1[p1];
//                 p1--;                
//             } else {
//                 nums1[p] = nums2[p2];
//                 p2--;
//             }
//             p--;
//         }

//         while (p2 >= 0) {
//             nums1[p] = nums2[p2];
//             p2--;
//             p--;
//         }
//     }
// }

// re-write 2025/Feb/25
// public class Solution {
//     public void merge(int[] nums1, int m, int[] nums2, int n) {
//         int p1 = m - 1;
//         int p2 =  n - 1;
//         int p =  m + n - 1;

//         while (p1 >= 0 && p2 >= 0) {
//             if (nums1[p1] > nums2[p2]) {
//                 nums1[p] = nums1[p1];
//                 p1--;
//             } else {
//                 nums1[p] = nums2[p2];
//                 p2--;
//             }
//             p--;
//         }

//         while (p2 >= 0) {
//             nums1[p] = nums2[p2];
//             p2--;
//             p--;
//         }
//     }
// }

// re-write 2025/Feb/27
// public class Solution {
//     public void merge(int[] nums1, int m, int[] nums2, int n) {
//         int p1 = m - 1;
//         int p2 = n - 1;
//         int p = m + n - 1;

//         while (p1 >= 0 && p2 >= 0) {
//             if (nums1[p1] > nums2[p2]) {
//                 nums1[p] = nums1[p1];
//                 p1--;
//             } else {
//                 nums1[p] = nums2[p2];
//                 p2--;
//             }
//             p--;
//         }

//         while (p2 >= 0) {
//             nums1[p] = nums2[p2];
//             p2--;
//             p--;
//         }
//     }
// }

// ------------------------------------------------------------

// Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

// Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

// Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
// Return k.
// Custom Judge:

// The judge will test your solution with the following code:

// int[] nums = [...]; // Input array
// int val = ...; // Value to remove
// int[] expectedNums = [...]; // The expected answer with correct length.
//                             // It is sorted with no values equaling val.

// int k = removeElement(nums, val); // Calls your implementation

// assert k == expectedNums.length;
// sort(nums, 0, k); // Sort the first k elements of nums
// for (int i = 0; i < actualLength; i++) {
//     assert nums[i] == expectedNums[i];
// }
// If all assertions pass, then your solution will be accepted.

// Example 1:

// Input: nums = [3,2,2,3], val = 3
// Output: 2, nums = [2,2,_,_]
// Explanation: Your function should return k = 2, with the first two elements of nums being 2.
// It does not matter what you leave beyond the returned k (hence they are underscores).
// Example 2:

// Input: nums = [0,1,2,2,3,0,4,2], val = 2
// Output: 5, nums = [0,1,4,0,3,_,_,_]
// Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
// Note that the five elements can be returned in any order.
// It does not matter what you leave beyond the returned k (hence they are underscores).
 
// Constraints:

// 0 <= nums.length <= 100
// 0 <= nums[i] <= 50
// 0 <= val <= 100

// public class Solution {
//     public int removeElement(int[] nums, int val) {
//         int k = 0;
//         for (int i = 0; i < nums.length; i++) {
//             if (nums[i] != val) {
//                 nums[k] = nums[i];
//                 k++;
//             }    
//         }
//         return k;
//     }
// }

// re-write 2025/Feb/24
// public class Solution {
//     public int removeElement(int[] nums, int val) {
//         int k = 0;
//         for (int i = 0; i < nums.length; i++) {
//             if (nums[i] != val) {
//                 nums[k] = nums[i];
//                 k++;
//             }
//         }
//         return k;
//     }
// }

// re-write 2025/Feb/25
// public class Solution {
//     public int removeElement(int[] nums, int val) {
//         int k = 0;
//         for (int i = 0; i < nums.length; i++) {
//             if (nums[i] != val) {
//                 nums[k] = nums[i];
//                 k++;
//             }
//         }
//         return k;
//     }
// }

// re-write 2025/Feb/27
// public class Solution {
//     public int removeElement(int[] nums, int val) {
//         int k = 0;
//         for (int i = 0; i < nums.length; i++) {
//             if (nums[i] != val) {
//                 nums[k] = nums[i];
//                 k++;
//             }
//         }
//         return k;
//     }
// }


// # -------------------------------------------

// 26. Remove Duplicates from Sorted Array
// # Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

// # Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

// # Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
// # Return k.
// # Custom Judge:

// # The judge will test your solution with the following code:

// # int[] nums = [...]; // Input array
// # int[] expectedNums = [...]; // The expected answer with correct length

// # int k = removeDuplicates(nums); // Calls your implementation

// # assert k == expectedNums.length;
// # for (int i = 0; i < k; i++) {
// #     assert nums[i] == expectedNums[i];
// # }

// # int val = ...; // Value to remove
// # int[] expectedNums = [...]; // The expected answer with correct length.
// #                             // It is sorted with no values equaling val.

// # int k = removeElement(nums, val); // Calls your implementation

// # assert k == expectedNums.length;
// # sort(nums, 0, k); // Sort the first k elements of nums
// # for (int i = 0; i < actualLength; i++) {
// #     assert nums[i] == expectedNums[i];
// # }
// # If all assertions pass, then your solution will be accepted.

// # Example 1:

// # Input: nums = [1,1,2]
// # Output: 2, nums = [1,2,_]
// # Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
// # It does not matter what you leave beyond the returned k (hence they are underscores).

// # It does not matter what you leave beyond the returned k (hence they are underscores).
// # Example 2:

// # Input: nums = [0,0,1,1,1,2,2,3,3,4]
// # Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
// # Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
// # It does not matter what you leave beyond the returned k (hence they are underscores).

// # Note that the five elements can be returned in any order.
// # It does not matter what you leave beyond the returned k (hence they are underscores).
 
// # Constraints:

// # 1 <= nums.length <= 3 * 104
// # -100 <= nums[i] <= 100
// # nums is sorted in non-decreasing order.

// public class Solution {
//     public int removeDuplicates(int[] nums) {
//         int k = 0;
//         for (int i = 1; i < nums.length; i++) {
//             if (nums[i] != nums[k]) {
//                 k++;
//                 nums[k] = nums[i]; 
//             }
//         }
//         return k + 1;
//     }
// }

// re-write 2025/Feb/24
// public class Solution {
//     public int removeDuplicates(int[] nums) {
//         int k = 0;
//         for (int i = 1; i < nums.length; i++) {
//             if (nums[i] != nums[k]) {
//                 k++;
//                 nums[k] = nums[i];
//             }
//         }
//         return k + 1;
//     }
// }

// re-write 2025/Feb/25
// public class Solution {
//     public int removeDuplicates(int[] nums) {
//         int k = 0;
//         for (int i = 1; i < nums.length; i++) {
//             if (nums[k] != nums[i]) {
//                 k++;
//                 nums[k] = nums[i];
//             }
//         }
//         return k + 1;
//     }
// }

// re-write 2025/Feb/27
// public class Solution {
//     public int removeDuplicates(int[] nums) {
//         int k = 0;
//         for (int i = 1; i < nums.length; i++) {
//             if (nums[k] != nums[i]) {
//                 k++;
//                 nums[k] = nums[i];
//             }
//         }
//         return k + 1;
//     }
// }

// # -----------------------------------------------

// # 80. Remove Duplicates from Sorted Array II
// # Medium
// # Topics
// # Companies
// # Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same.

// # Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

// # Return k after placing the final result in the first k slots of nums.

// # Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

// # Custom Judge:

// # The judge will test your solution with the following code:

// # int[] nums = [...]; // Input array
// # int[] expectedNums = [...]; // The expected answer with correct length

// # int k = removeDuplicates(nums); // Calls your implementation

// # assert k == expectedNums.length;
// # for (int i = 0; i < k; i++) {
// #     assert nums[i] == expectedNums[i];
// # }
// # If all assertions pass, then your solution will be accepted.

// # Example 1:

// # Input: nums = [1,1,1,2,2,3]
// # Output: 5, nums = [1,1,2,2,3,_]
// # Explanation: Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
// # It does not matter what you leave beyond the returned k (hence they are underscores).
// # Example 2:

// # Input: nums = [0,0,1,1,1,1,2,3,3]
// # Output: 7, nums = [0,0,1,1,2,3,3,_,_]
// # Explanation: Your function should return k = 7, with the first seven elements of nums being 0, 0, 1, 1, 2, 3 and 3 respectively.
// # It does not matter what you leave beyond the returned k (hence they are underscores).
 
// # Constraints:

// # 1 <= nums.length <= 3 * 104
// # -104 <= nums[i] <= 104
// # nums is sorted in non-decreasing order.

// public class Solution {
//     public int removeDuplicates(int[] nums) {
//         int k = 2;
//         for (int i = 2; i < nums.length; i++) {
//             if (nums[i] != nums[k - 2]) {
//                 nums[k] = nums[i];
//                 k++;
//             }
//         }
//         return k;
//     }
// }

// re-write 2025/Feb/24
// public class Solution{
//     public int removeDuplicates(int[] nums) {
//         int k = 2;
//         for (int i = 2; i < nums.length; i++) {
//             if (nums[i] != nums[k - 2]) {
//                 nums[k] = nums[i];
//                 k++;
//             }
//         }
//         return k;
//     }
// }

// re-write 2025/Feb/25
// public class Solution {
//     public int removeDuplicates(int[] nums) {
//         int k = 2;
//         for (int i = 2; i < nums.length; i++) {
//             if (nums[i] != nums[k - 2]) {
//                 nums[k] = nums[i];
//                 k++;
//             }
//         }
//         return k;
//     }
// }

// re-write 2025/Feb/27
// public class Solution {
//     public int removeDuplicates(int[] nums) {
//         int k = 2;
//         for (int i = 2; i < nums.length; i++) {
//             if (nums[i] != nums[k - 2]) {
//                 nums[k] = nums[i];
//                 k++;
//             }
//         }
//         return k;
//     }
// }

// # ------------------------------------------------------------

// # 169. Majority Element
// # Easy
// # Topics
// # Companies
// # Given an array nums of size n, return the majority element.

// # The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

// # Example 1:

// # Input: nums = [3,2,3]
// # Output: 3
// # Example 2:

// # Input: nums = [2,2,1,1,1,2,2]
// # Output: 2

// # Constraints:

// # n == nums.length
// # 1 <= n <= 5 * 104
// # -109 <= nums[i] <= 109

// import java.util.Arrays;
// public class Solution {
//     public int majorityElement(int[] nums) {
//         Arrays.sort(nums);  // array nums
//         return nums[nums.length / 2];  // return middle element
//     }
// }

// re-write 2025/Feb/25
// import java.util.Arrays;
// public class Solution {
//     public int majorityElement(int[] nums) {
//         Arrays.sort(nums);
//         return nums[nums.length / 2];
//     }
// }

// re-write 2025/Feb/26 - 1
// import java.util.Arrays;
// public class Solution {
//     public int majorityElement(int[] nums) {
//         Arrays.sort(nums);
//         return nums[nums.length / 2];
//     }
// }

// re-write 2025/Feb/26 - 2
// import java.util.Arrays;
// public class Solution {
//     public int majorityElement(int[] nums) {
//         Arrays.sort(nums);
//         return nums[nums.length /2];
//     }
// }

// re-write 2025/Feb/27 - 1
// import java.utyil.Arrays;
// public class Solution {
//     public int majorityElement(int nums[]) {
//         Arrays.sort(nums);
//         return nums[nums.length / 2];
//     }}

// re-write 2025/Feb/27 - 2
// import java.util.Arrays;
// public class Solution {
//     public int majorityElement(int[] nums) {
//         Arrays.sort(nums);
//         return nums[nums.length / 2];
//     }
// }

// re-write 2025/Feb/27 - 3
// import java.util.Arrays;
// public class Solution {
//     public int majorityElement(int[] nums) {
//         Arrays.sort(nums);
//         return nums[nums.length / 2];
//     }
// }

// re-write 2025/Feb/27 - 4
// import java.util.Arrays;
// public class Solution {
//     public int majorityElement(int[] nums) {
//         Arrays.sort(nums);
//         return nums[nums.length / 2];
//     }
// }

// re-write 2025/Feb/27 - 5
// import java.util.Arrays;
// public class Solution {
//     public int majorityElement(int[] nums) {
//         Arrays.sort(nums);
//         return nums[nums.length / 2];
//     }
// }

// re-write 2025/Feb/27 - 6
// import java.util.Arrays;
// public class Solution {
//     public int majorityElement(int[] nums) {
//         Arrays.sort(nums);
//         return nums[nums.length / 2];
//     }
// }

// re-write 2025/Feb/27 - 7
// import java.util.Arrays;
// public class Solution {
//     public int majorityElement(int[] nums) {
//         Arrays.sort(nums);
//         return nums[nums.length / 2];
//     }
// }

// # ------------------------------------------

// # 189. Rotate Array
// # Medium
// # Topics
// # Companies
// # Hint
// # Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

// # Example 1:

// # Input: nums = [1,2,3,4,5,6,7], k = 3
// # Output: [5,6,7,1,2,3,4]
// # Explanation:
// # rotate 1 steps to the right: [7,1,2,3,4,5,6]
// # rotate 2 steps to the right: [6,7,1,2,3,4,5]
// # rotate 3 steps to the right: [5,6,7,1,2,3,4]
// # Example 2:

// # Input: nums = [-1,-100,3,99], k = 2
// # Output: [3,99,-1,-100]
// # Explanation: 
// # rotate 1 steps to the right: [99,-1,-100,3]
// # rotate 2 steps to the right: [3,99,-1,-100]

// # Constraints:

// # 1 <= nums.length <= 105
// # -231 <= nums[i] <= 231 - 1
// # 0 <= k <= 105

// public class Solution {
//     public void rotate(int[] nums, int k) {
//         int n = nums.length;
//         k %= n; // valid rotate steps
//         if (k == 0) return;

//         // Step 1: rotate all nums
//         reverse(nums, 0, n - 1);
//         // Step 2: rotate the first k elements
//         reverse(nums, 0, k - 1);
//         // Step 3: rotate the n-k elements
//         reverse(nums, k, n - 1);
//     }

//     // def reverse method, to rotate start to end
//     private void reverse(int[] nums, int start, int end) {
//         while (start < end) {
//             int temp = nums[start];
//             nums[start] = nums[end];
//             nums[end] = temp;
//             start++;
//             end--;
//         }
//     }
// }

// re-write 2025/Feb/27 - 1
// public class Solution {
//     public void rotate(int[] nums, int k) {
//         int n = nums.length;
//         k %= n;
//         if (k == 0) return;

//         reverse(nums, 0, n - 1);
//         reverse(nums, 0, k - 1);
//         reverse(nums, k, n - 1);
//     }

//     private void reverse(int[] nums, int start, int end) {
//         while (start < end) {
//             int temp = nums[start];
//             nums[start] = nums[end];
//             nums[end] = temp;
//             start++;
//             end--;
//         }
//     }
// }

// re-write 2025/Feb/27 - 2
// public class Solution {
//     public void rotate(int[] nums, int k) {
//         int n = nums.length;
//         k %= n;
//         if (k == 0) return;

//         reverse(nums, 0, n - 1);
//         reverse(nums, 0, k - 1);
//         reverse(nums, k, n - 1);
//     }

//     private void reverse(int[] nums, int start, int end) {
//         while (start < end) {
//             int temp = nums[start];
//             nums[start] = nums[end];
//             nums[end] = temp;
//             start++;
//             end--;
//         }
//     }
// }

// re-write 2025/Feb/28 - 1
// public class Solution {
//     public void rotate(int[] nums, int k) {
//         int n = nums.length;
//         k %= n;
//         if (k == 0) return;

//         reverse(nums, 0, n - 1);
//         reverse(nums, 0, k - 1);
//         reverse(nums, k, n - 1);
//     }

//     private void reverse(int[] nums, int start, int end) {
//         while (start < end) {
//             int temp = nums[start];
//             nums[start] = nums[end];
//             nums[end] = temp;
//             start++;
//             end--;
//         }
//     }
// }

// re-write 2025/Feb/28 - 2
// public class Solution {
//     public void rotate(int[] nums, int k) {
//         int n = nums.length;
//         k %= n;
//         if (k == 0) return;

//         reverse(nums, 0, n - 1);
//         reverse(nums, 0, k - 1);
//         reverse(nums, k, n - 1);
//     }

//     private void reverse(int[] nums, int start, int end) {
//         while (start < end) {
//             int temp = nums[start];
//             nums[start] = nums[end];
//             nums[end] = temp;
//             start++;
//             end--;
//         }
//     }
// }

// re-write 2025/Feb/28 - 3
// public class Solution {
//     public void rotate(int[] nums, int k) {
//         int n = nums.length;
//         k %= n;
//         if (k == 0) return;

//         reverse(nums, 0, n - 1);
//         reverse(nums, 0, k - 1);
//         reverse(nums, k, n - 1);
//     }

//     private void reverse(int[] nums, int start, int end) {
//         while (start < end) {
//             int temp = nums[start];
//             nums[start] = nums[end];
//             nums[end] = temp;
//             start++;
//             end--;
//         }
//     }
// }

// # ------------------------------------------

// # 121. Best Time to Buy and Sell Stock
// # Easy
// # Topics
// # Companies
// # You are given an array prices where prices[i] is the price of a given stock on the ith day.

// # You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

// # Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

// # Example 1:

// # Input: prices = [7,1,5,3,6,4]
// # Output: 5
// # Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
// # Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
// # Example 2:

// # Input: prices = [7,6,4,3,1]
// # Output: 0
// # Explanation: In this case, no transactions are done and the max profit = 0.
 

// # Constraints:

// # 1 <= prices.length <= 105
// # 0 <= prices[i] <= 104

// class Solution {
//     public int maxProfit(int[] prices) {
//         int minPrice = Integer.MAX_VALUE;
//         int maxProfit = 0;

//         for (int i = 0; i < prices.length; i++) {
//             if (prices[i] < minPrice) {
//                 minPrice = prices[i];
//             }
//             else if (maxProfit < prices[i] - minPrice) {
//                 maxProfit = prices[i] - minPrice;
//             }
//         }
//         return maxProfit;
//     }
// }

// re-write 2025/Mar/1 - 1
// class Solution {
//     public int maxProfit(int[] prices) {
//         int minPrice = Integer.MAX_VALUE;
//         int maxProfit = 0;

//         for (int price : prices) {
//             minPrice = Math.min(minPrice, price);
//             maxProfit = Math.max(maxProfit, price - minPrice);
//         }

//         return maxProfit;
//     }
// }

// re-write 2025/Mar/1 - 2
// class Solution {
//     public int maxProfit(int[] prices) {
//         int minPrice = Integer.MAX_VALUE;
//         int maxProfit = 0;

//         for (int price : prices) {
//             minPrice = Math.min(minPrice, price);
//             maxProfit = Math.max(maxProfit, price - minPrice);
//         }
//         return maxProfit;
//     }
// }

// re-write 2025/Mar/1 - 3
// class Solution {
//     public int maxProfit(int[] prices) {
//         int minPrice = Integer.MAX_VALUE;
//         int maxProfit = 0;

//         for (int price : prices) {
//             minPrice = Math.min(minPrice, price);
//             maxProfit = Math.max(maxProfit, price - minPrice);
//         }
//         return maxProfit;
//     }
// }

// re-write 2025/Mar/1 - 4
// class Solution {
//     public int maxProfit(int[] prices) {
//         int minPrice = Integer.MAX_VALUE;
//         int maxProfit = 0;

//         for (int price : prices) {
//             minPrice = Math.min(minPrice, price);
//             maxProfit = Math.max(maxProfit, price - minPrice);
//         }
//         return maxProfit;
//     }
// }

// # -----------------------------------

// # 122. Best Time to Buy and Sell Stock II
// # Medium # Topics # Companies
// # You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
// # On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.
// # Find and return the maximum profit you can achieve.

// # Example 1:
// # Input: prices = [7,1,5,3,6,4]
// # Output: 7
// # Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
// # Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
// # Total profit is 4 + 3 = 7.

// # Example 2:
// # Input: prices = [1,2,3,4,5]
// # Output: 4
// # Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
// # Total profit is 4.

// # Example 3:
// # Input: prices = [7,6,4,3,1]
// # Output: 0
// # Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.
 
// # Constraints:
// # 1 <= prices.length <= 3 * 104
// # 0 <= prices[i] <= 104

// class Solution {
//     public int maxProfit(int[] prices) {
//         int maxProfit = 0;
//         for (int i = 1; i < prices.length; i++) {
//             maxProfit += Math.max(prices[i] - prices[i - 1], 0);
//         }
//         return maxProfit;
//     }
// }

// # re-write 2025/Mar/1 -1
// class Solution {
//     public int maxProfit(int[] prices) {
//         int maxProfit = 0;
//         for (int i = 1; i < prices.length; i++) {
//             maxProfit += Math.max(prices[i] - prices[i - 1], 0);
//         }
//         return maxProfit;
//     }
// }

// # re-write 2025/Mar/1 -2
// class Solution {
//     public int maxProfit(int[] prices) {
//         int maxProfit = 0;
//         for (int i = 1; i < prices.length; i++) {
//             maxProfit += Math.max(prices[i] - prices[i - 1], 0);
//         }
//         return maxProfit;
//     }
// }

// # -----------------------------------

// # 55. Jump Game
// # Medium # Topics # Companies
// # You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.
// # Return true if you can reach the last index, or false otherwise.

// # Example 1:
// # Input: nums = [2,3,1,1,4]
// # Output: true
// # Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

// # Example 2:
// # Input: nums = [3,2,1,0,4]
// # Output: false
// # Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

// # Constraints:
// # 1 <= nums.length <= 104
// # 0 <= nums[i] <= 105

// class Solution {
//     public boolean canJump(int[] nums) {
//         int maxReach = 0;
//         for (int i = 0; i < nums.length; i++) {
//             if (i > maxReach) {
//                 return false;
//             }
//             maxReach = Math.max(maxReach, i + nums[i]);
//             if (maxReach >= nums.length - 1) {
//                 return true;
//             }
//         }
//         return false;
//     }
// }

// # re-write 2025/Mar/5 - 1
// class Solution {
//     public boolean canJump(int[] nums) {
//         int maxReach = 0;
//         for (int i = 0; i < nums.length; i++) {
//             if (i > maxReach) {
//                 return false;
//             }
//             maxReach = Math.max(maxReach, i + nums[i]);
//             if (maxReach >= nums.length - 1) {
//                 return true;
//             }
//         }
//         return false;
//     }
// }

// # re-write 2025/Mar/5 - 2
// class Solution {
//     public boolean canJump(int[] nums) {
//         int maxReach = 0;
//         for (int i = 0; i < nums.length; i++) {
//             if (i > maxReach) {
//                 return false;
//             }
//             maxReach = Math.max(maxReach, i + nums[i]);
//             if (maxReach >= nums.length - 1) {
//                 return true;
//             }
//         }
//         return false;
//     }
// }

// # re-write 2025/Mar/5 - 3
// class Solution {
//     public boolean canJump(int[] nums) {
//         int maxReach = 0;
//         for (int i = 0; i < nums.length; i++) {
//             if (i > maxReach) {
//                 return false;
//             }
//             maxReach = Math.max(maxReach, i + nums[i]);
//             if (maxReach >= nums.length - 1) {
//                 return true;
//             }
//         }
//         return false;
//     }
// }

// # -----------------------------------

// # 45. Jump Game II
// # Medium # Topics # Companies
// # You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].
// # Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:

// # 0 <= j <= nums[i] and
// # i + j < n
// # Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].

// # Example 1:
// # Input: nums = [2,3,1,1,4]
// # Output: 2
// # Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.

// # Example 2:
// # Input: nums = [2,3,0,1,4]
// # Output: 2

// # Constraints:
// # 1 <= nums.length <= 104
// # 0 <= nums[i] <= 1000
// # It's guaranteed that you can reach nums[n - 1].

// class Solution {
//     public int jump(int[] nums) {
//         int jumps = 0;
//         int maxReach = 0;
//         int end = 0;

//         for (int i = 0; i < nums.length - 1; i++) {
//             maxReach = Math.max(maxReach, i + nums[i]);
//             if (i == end) {
//                 jumps++;
//                 end = maxReach;
//                 if (end >= nums.length - 1) {
//                     break;
//                 }
//             }
//         }
//         return jumps;
//     }
// }

// # re-write 2025/Mar/6 - 1
// class Solution {
//     public int jump(int[] nums) {
//         int jumps = 0;
//         int maxReach = 0;
//         int end = 0;

//         for (int i = 0; i < nums.length - 1; i++) {
//             maxReach = Math.max(maxReach, i + nums[i]);
//             if (end == i) {
//                 jumps++;
//                 end = maxReach;
//                 if (end >= nums.length - 1) {
//                     break;
//                 }
//             }
//         }
//         return jumps;
//     }
// }

// # -----------------------------------

// # 274. H-Index
// # Medium # Topics # Companies 
// # Hint
// # Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, return the researcher's h-index.
// # According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of h such that the given researcher has published at least h papers that have each been cited at least h times.

// # Example 1:
// # Input: citations = [3,0,6,1,5]
// # Output: 3
// # Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively.
// # Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, their h-index is 3.

// # Example 2:
// # Input: citations = [1,3,1]
// # Output: 1

// # Constraints:
// # n == citations.length
// # 1 <= n <= 5000
// # 0 <= citations[i] <= 1000