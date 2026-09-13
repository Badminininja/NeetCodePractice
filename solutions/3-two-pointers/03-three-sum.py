"""
LeetCode 15. 3Sum

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
such that i != j, i != k, j != k, and nums[i] + nums[j] + nums[k] == 0. The
solution set must not contain duplicate triplets.

Approach: sort the array, then loop i over it as an anchor for the first
number. For each i, run a Two-Sum-II-style two-pointer search (left, right)
over the remainder of the array for a pair summing to -nums[i]. Collect
results in a set of tuples to dedupe automatically, instead of manually
skip-checking repeated values - since i < left < right always, a matching
triplet's values come out in the same sorted order regardless of which
array positions produced them, so equal-valued triplets collapse into the
same tuple.

The three pointer-move branches must be if/elif/elif, not three separate
ifs: with separate ifs, once one branch moves a pointer past the other in
a given pass, the remaining ifs still re-evaluate nums[left] + nums[right]
using that now-crossed state, which can spuriously satisfy the equality
check using the same array position twice.

Time:  O(n^2)
Space: O(n) for the sort; O(1) extra beyond the output
"""


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        found = set()

        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                if nums[left] + nums[right] < 0 - nums[i]:
                    left += 1
                elif nums[left] + nums[right] > 0 - nums[i]:
                    right -= 1
                elif nums[left] + nums[right] == 0 - nums[i]:
                    found.add(tuple([nums[i], nums[left], nums[right]]))
                    left += 1

        return [[x, y, z] for x, y, z in found]


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
        ([0, 1, 1], []),
        ([0, 0, 0], [[0, 0, 0]]),
        ([0, 0, 0, 0], [[0, 0, 0]]),
        ([-2, 0, 0, 2, 2], [[-2, 0, 2]]),
        ([3, 0, -2, -1, 1, 2], [[-2, -1, 3], [-2, 0, 2], [-1, 0, 1]]),
    ]
    for nums, expected in tests:
        result = sol.threeSum(nums[:])
        got_sorted = sorted(sorted(t) for t in result)
        exp_sorted = sorted(sorted(t) for t in expected)
        status = "PASS" if got_sorted == exp_sorted else "FAIL"
        print(f"{status}: threeSum({nums}) = {result} (expected {expected})")
