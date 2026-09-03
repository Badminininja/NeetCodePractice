"""
LC 238 - Product of Array Except Self

Given an integer array nums, return an array answer where answer[i] is the
product of all elements of nums except nums[i]. Must run in O(n) time
without using division.

Approach:
    answer[i] = (product of everything left of i) * (product of everything
    right of i). Both the left-running-product and right-running-product
    can be built in a single accumulating pass each (reusing the previous
    step's result), rather than recomputing "everything except i" from
    scratch for every i. Two passes, O(n) time, O(n) space for output
    (excluding the output array itself, O(1) extra space is achievable).
"""


def productExceptSelf(nums: list[int]) -> list[int]:
    n = len(nums)
    left = [1] * n
    right = [1] * n

    for i in range(1, n):
        left[i] = left[i - 1] * nums[i - 1]

    for i in range(n - 2, -1, -1):
        right[i] = right[i + 1] * nums[i + 1]

    return [left[i] * right[i] for i in range(n)]


# Space-optimized version: build left products directly into the result,
# then fold in the right-running-product using a single extra variable
# instead of a second full array.
def productExceptSelf_optimized(nums: list[int]) -> list[int]:
    n = len(nums)
    result = [1] * n

    for i in range(1, n):
        result[i] = result[i - 1] * nums[i - 1]

    right_running = 1
    for i in range(n - 1, -1, -1):
        result[i] *= right_running
        right_running *= nums[i]

    return result


if __name__ == "__main__":
    assert productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]
    assert productExceptSelf([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]

    assert productExceptSelf_optimized([1, 2, 3, 4]) == [24, 12, 8, 6]
    assert productExceptSelf_optimized([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]

    print("All tests passed.")
