// # 1. You are given two integer arrays nums1 and nums2, sorted in non - decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

// # Merge nums1 and nums2 into a single array sorted in non - decreasing order.

// # The final sorted array should not be returned by the function, but instead be stored inside the array nums1.To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored.nums2 has a length of n.

// function merge(nums1, m, nums2, n) {
//     let p1 = m - 1;
//     let p2 = n - 1;
//     let p = m + n - 1;

//     while (p1 >= 0 && p2 >= 0) {
//         if (nums1[p1] > nums2[p2]) {
//             nums1[p] = nums1[p1];
//             p1--;            
//         } else {
//             nums1[p] = nums2[p2];
//             p2--;
//         }
//         p--;
//     }

//     while (p2 >= 0) {
//         nums1[p] = nums2[p2];
//         p2--;
//         p--;
//     }
// }

// re-write 2025/Feb/22
// function merge(nums1, m, nums2, n) {
//     let p1 = m - 1, p2 = n - 1, p = m + n - 1;

//     while (p1 >= 0 && p2 >= 0) {
//         if (nums1[p1] > nums2[p2]) {
//             nums1[p] = nums1[p1];
//             p1--;
//         } else {
//             nums1[p] = nums2[p2];
//             p2--;
//         }
//         p--;
//     }

//     while (p2 >= 0) {
//         nums1[p] = nums2[p2]
//         p2--;
//         p--;
//     }
// }

// re-write 2025/Feb/23
// function merge(nums1, m, nums2, n) {
//     let p1 = m - 1, p2 = n -1, p = m + n - 1;

//     while (p1 >= 0 && p2 >= 0) {
//         if (nums1[p1] > nums2[p2]) {
//             nums1[p] = nums1[p1];
//             p1--;
//         } else {
//             nums1[p] = nums2[p2];
//             p2--;
//         }
//         p--;
//     }

//     while (p2 >= 0) {
//         nums1[p] = nums2[p2];
//         p2--;
//         p--;
//     }
// }

// re-write 2025/Feb/25
// function merge(nums1, m, nums2, n) {
//     let p1 = m - 1, p2 = n - 1, p = m + n -1;

//     while (p1 >= 0 && p2 >= 0) {
//         if (nums1[p1] > nums2[p2]) {
//             nums1[p] = nums1[p1];
//             p1--;
//         } else {
//             nums1[p] = nums2[p2];
//             p2--;
//         }
//         p--;
//     }

//     while (p2 >= 0) {
//         nums1[p] = nums2[p2];
//         p2--;
//         p--;
//     }
// }

// re-write 2025/Feb/27
// function merge(nums1, m, nums2, n) {
//     let p1 = m - 1;
//     let p2 = n - 1;
//     let p = m + n - 1;

//     while (p1 >= 0 && p2 >= 0) {
//         if (nums1[p1] > nums2[p2]) {
//             nums1[p] = nums1[p1];
//             p1--;
//         } else {
//             nums1[p] = nums2[p2];
//             p2--;
//         }
//         p--;
//     }

//     while (p2 >= 0) {
//         nums1[p] = nums2[p2];
//         p2--;
//         p--;
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

// function removeElement(nums, val) {
//     let k = 0;
//     for (let i = 0; i < nums.length; i++) {
//         if (nums[i] != val) {
//             nums[k] = nums[i];
//             k++;
//         }
//     }
//     return k;
// }

// re-write 2025/Feb/24
// function removeElement(nums, val) {
//     let k = 0;
//     for (let i = 0; i < nums.length; i++) {
//         if (nums[i] !== val) {
//             nums[k] = nums[i];
//             k++;
//         }
//     }
//     return k;
// }

// re-write 2025/Feb/25
// function removeElement(nums, val) {
//     let k = 0;
//     for (let i = 0; i < nums.length; i++) {
//         if (nums[i] != val) {
//             nums[k] = nums[i];
//             k++;
//         }
//     }
//     return k;
// }

// re-write 2025/Feb/27
// function removeElement(nums, val) {
//     let k = 0;
//     for (let i = 0; i < nums.length; i++) {
//         if (nums[i] !== val) {
//             nums[k] = nums[i];
//             k++;
//         }
//     }
//     return k;
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

// function removeDuplicates(nums) {
//     let k = 0;
//     for (let i = 1; i < nums.length; i++) {
//         if (nums[i] != nums[k]) {
//             k++;
//             nums[k] = nums[i];
//         }
//     }
//     return k + 1;
// }

// re-write 2025/Feb/24
// function removeDuplicates(nums) {
//     if (nums.length === 0) return 0; // for null array

//     let k = 0;
//     for (let i = 1; i < nums.length; i++) {
//         if (nums[k] !== nums[i]) {
//             k++;
//             nums[k] = nums[i];
//         }
//     }
//     return k + 1;
// }

// re-write 2025/Feb/25
// function removeDuplicates(nums) {
//     if (nums.length === 0) return 0;
//     let k = 0;
//     for (let i = 1; i < nums.length; i++) {
//         if (nums[k] != nums[i]) {
//             k++;
//             nums[k] = nums[i];
//         }
//     }
//     return k + 1;
// }

// re-write 2025/Feb/27
// function removeDuplicates(nums) {
//     let k = 0;
//     for (let i = 1; i < nums.length; i++) {
//         if (nums[k] !== nums[i]) {
//             k++;
//             nums[k] = nums[i];
//         }
//     }
//     return k + 1;
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

// function removeDuplicates(nums) {
//     let k = 2;
//     for (let i = 2; i < nums.length; i++) {
//         if (nums[i] != nums[k - 2]) {
//             nums[k] = nums[i];
//             k++;
//         }
//     }
//     return k;
// }

// re-write 2025/Feb/24
// function removeDuplicates(nums) {
//     if (nums.length < 2) return nums.length; // Avoid out-of-bounds access for nums[k-2].
    
//     let k = 2;
//     for (let i = 2; i < nums.length; i++) {
//         if (nums[i] !== nums[k - 2]) {
//             nums[k] = nums[i];
//             k++;
//         }
//     }
//     return k;
// }

// re-write 2025/Feb/25
// function removeDuplicates(nums) {
//     if (nums.length < 2) return nums.length;
//     let k = 2;
//     for (let i = 2; i < nums.length; i++) {
//         if (nums[i] != nums[k - 2]) {
//             nums[k] = nums[i];
//             k++;
//         }
//     }
//     return k;
// }

// re-write 2025/Feb/27
// function removeDuplicates(nums) {
//     let k = 2;
//     for (let i = 2; i < nums.length; i++) {
//         if (nums[i] !== nums[k - 2]) {
//             nums[k] = nums[i];
//             k++;
//         }
//     }
//     return k;
// }

// # ------------------------------------------------------------

// # 169. Majority Element
// # Easy
// # Topics
// # Companies
// # Given an array nums of size n, return the majority element.

// # The majority element is the element that appears more than n / 2 times. You may assume that the majority element always exists in the array.

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

// function majorityElement(nums) {
//     nums.sort((a, b) => a - b);
//     return nums[Math.floor(nums.length / 2)];
// }

// re-write 2025/Feb/26
// function majorityElement(nums) {
//     nums.sort((a, b) => a - b);
//     return nums[Math.floor(nums.length / 2)];
// }

// re-write 2025/Feb/27 - 1
// function majorityElement(nums) {
//     nums.sort((a, b) => a - b);
//     return nums[Math.floor(nums.length / 2)];
// }

// re-write 2025/Feb/27 - 2
// function majorityElement(nums) {
//     nums.sort((a, b) => a - b);
//     return nums[Math.floor(nums.length / 2)];
// }

// re-write 2025/Feb/27 - 3
// function majorityElement(nums) {
//     nums.sort((a, b) => a - b);
//     return nums[Math.floor(nums.length / 2)];
// }

// re-write 2025/Feb/27 - 4
// function majorityElement(nums) {
//     nums.sort((a, b) => a - b);
//     return nums[Math.floor(nums.length / 2)];
// }

// re-write 2025/Feb/27 - 5
// function majorityElement(nums) {
//     nums.sort((a, b) => a - b);
//     return nums[Math.floor(nums.length / 2)];
// }

// re-write 2025/Feb/27 - 6
// function majorityElement(nums) {
//     nums.sort((a, b) => a - b);
//     return nums[Math.floor(nums.length / 2)];
// }

// re-write 2025/Feb/27 - 7
// function majorityElement(nums) {
//     nums.sort((a, b) => a - b);
//     return nums[Math.floor(nums.length / 2)];
// }

// re-write 2025/Feb/27 - 8
// function majorityElement(nums) {
//     nums.sort((a, b) => a - b);
//     return nums[Math.floor(nums.length / 2)];
// }

// re-write 2025/Feb/27 - 9
// function majorityElement(nums) {
//     nums.sort((a, b) => a - b)
//     return nums[Math.floor(nums.length / 2)];
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

// var rotate = function(nums, k) {
//     let n = nums.length;
//     k %= n;

//     const reverse = (arr, start, end) => {
//         while (start < end) {
//             let temp = arr[start];
//             arr[start] = arr[end];
//             arr[end] = temp;
//             start++;
//             end--;
//         }
//     };

//     reverse(nums, 0, n - 1);
//     reverse(nums, 0, k - 1);
//     reverse(nums, k, n - 1);
// };

// re-write 2025/Feb/28 - 1
// var rotate = function(nums, k) {
//     let n = nums.length;
//     k %= n;

//     const reverse = (nums, start, end) => {
//         while (start < end) {
//             let temp = nums[start];
//             nums[start] = nums[end];
//             nums[end] = temp;
//             start++;
//             end--;
//         }
//     };

//     reverse(nums, 0, n - 1);
//     reverse(nums, 0, k - 1);
//     reverse(nums, k, n - 1);
// };

// re-write 2025/Feb/28 - 2
// var rotate = function(nums, k) {
//     let n = nums.length;
//     k %= n;
//     if (k == 0) return;

//     const reverse = (nums, start, end) => {
//         while (start < end) {
//             let temp = nums[start];
//             nums[start] = nums[end];
//             nums[end] = temp;
//             start++;
//             end--;
//         }
//     };

//     reverse(nums, 0, n - 1);
//     reverse(nums, 0, k - 1);
//     reverse(nums, k, n - 1);
// };

// re-write 2025/Feb/28 - 3
// var rotate = function(nums, k) {
//     let n = nums.length;
//     k %= n;
//     if (k == 0) return;

//     const reverse = (nums, start, end) => {
//         while (start < end) {
//             let temp = nums[start];
//             nums[start] = nums[end];
//             nums[end] = temp;
//             start++;
//             end--;
//         }
//     };

//     reverse(nums, 0, n - 1);
//     reverse(nums, 0, k - 1);
//     reverse(nums, k, n - 1);
// };

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

var maxProfit = function(prices) {
    let minPrice = Infinity;
    let maxProfit = 0;

    for (let price of prices) {
        minPrice = Math.min(minPrice, price);
        maxProfit = Math.max(maxProfit, price - minPrice);
    }

    return maxProfit;
};