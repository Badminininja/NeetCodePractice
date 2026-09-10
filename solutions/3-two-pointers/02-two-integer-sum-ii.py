"""
LeetCode 167. Two Sum II - Input Array Is Sorted (NeetCode: Two Integer Sum II)

Given a 1-indexed array of integers numbers that is already sorted in
non-decreasing order, find two numbers that add up to a specific target
number. Return the indices of the two numbers (1-indexed) as an integer
array of size 2. There is exactly one valid answer, and the same element
can't be used twice.

Approach: two pointers, left and right, starting at opposite ends. Since
the array is sorted, moving the left pointer up can only increase the sum
and moving the right pointer down can only decrease it, so comparing the
current sum to target tells you unambiguously which pointer to move - no
need for a hashmap like the unsorted Two Sum.

Time:  O(n)
Space: O(1)
"""


class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        index1 = 0
        index2 = len(numbers) - 1

        while True:
            if numbers[index1] + numbers[index2] < target:
                index1 += 1
            if numbers[index1] + numbers[index2] > target:
                index2 -= 1
            if numbers[index1] + numbers[index2] == target:
                return [index1 + 1, index2 + 1]


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([2, 7, 11, 15], 9, [1, 2]),
        ([2, 3, 4], 6, [1, 3]),
        ([-1, 0], -1, [1, 2]),
        ([1, 2, 3, 4, 4, 9, 56, 90], 8, [4, 5]),
        ([0, 0, 3, 4], 0, [1, 2]),
    ]
    for nums, target, expected in tests:
        result = sol.twoSum(nums, target)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: twoSum({nums}, {target}) = {result} (expected {expected})")
