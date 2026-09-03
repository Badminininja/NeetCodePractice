# Progress Log

Tracking problems worked through, organized by NeetCode's roadmap categories. Each entry notes the actual approach taken, bugs caught along the way, and where the code lives in this repo.

## Arrays & Hashing

_Worked through in a separate chat and imported here. Full per-problem write-ups live in `solutions/1-arrays-and-hashing/arrays_hashing_tips.md` — this is the condensed version._

- [x] **Contains Duplicate** (LC 217) — existence check, so reach for a `set` not a counting `dict`. Naive nested-loop comparison is O(n²); a single pass tracking "have I seen this" is O(n).
- [x] **Valid Anagram** (LC 242) — build a frequency `dict` from one string, then "spend down" counts while walking the other; any missing/zeroed key fails it. Not the same as a palindrome check.
- [x] **Two Sum** (LC 1) — reframe as "what complement do I still need," not "what do these sum to." Dict maps value → index; check for the complement before inserting the current value, which naturally prevents reusing an element.
- [x] **Group Anagrams** (LC 49) — sorting a word's letters gives a canonical signature shared by every anagram of it; a dict keyed by signature groups everything in one pass instead of pairwise comparisons.
- [x] **Top K Frequent Elements** (LC 347) — frequency is bounded by `len(nums)`, so use frequency itself as an array index (bucket sort) instead of sorting by count. The nested loop over buckets is still O(n) total since every element is visited exactly once.
- [x] **Encode and Decode Strings** (LC 271) — a format-design problem, not an algorithm one. Length-prefixing each string (`"{len}#{string}"`) avoids ambiguity when a string contains whatever delimiter you'd otherwise pick.
- [x] **Product of Array Except Self** (LC 238) — `answer[i]` = (product left of i) × (product right of i), each built with a single accumulating pass — no division needed, works fine with zeros in the array.
- [x] **Valid Sudoku** (LC 36) — rows, columns, and 3×3 boxes are three independent "no duplicates" zones, each needing its own tracking set; a single global seen-set would be wrong. `(r // 3, c // 3)` keys the box.
- [x] **Longest Consecutive Sequence** (LC 128) — walking forward from every number is O(n²) from redundant re-walks of the same run. Only start a walk from a true sequence start (`num - 1 not in set`) to make it O(n).

## Two Pointers
_(none yet)_

## Sliding Window
_(none yet)_

## Stack

- [x] **Valid Parentheses** (LC 20) — 2026-09-03
  - Initial instinct was a counter per bracket type (up on open, down on close, fail on negative or non-zero at the end). Worked out that this fails on interleaved-but-invalid strings like `([)]`, because counting throws away ordering information — it only tracks totals, not which bracket is currently "open."
  - Rebuilt with a stack: push each opening bracket; on a closing bracket, check the top of the stack against a dict of matching pairs (`{')': '(', ']': '[', '}': '{'}`) — pop on a match, return `False` on a mismatch or an empty stack. String is valid only if the stack is empty once the loop ends.
  - Caught a real bug mid-build: an early version's mismatch branch had no `else: return False`, so a genuinely invalid closer (the `]` in `"(])"`) was silently skipped instead of failing the whole string — it came back `True` when it should've been `False`.
  - Also benchmarked the dict-lookup version against a chained triple-OR condition with `timeit` — dict version came out ~1.4-2x faster in practice, mainly because the OR-chain version was doing two independent, unconditional `if` checks (not `if`/`elif`) per character rather than one dict membership test.
  - Code + self-tests: `solutions/2-stack/01-valid-parentheses.py`

## Binary Search
_(none yet)_

## Linked List
_(none yet)_

## Trees
_(none yet)_

## Tries
_(none yet)_

## Heap / Priority Queue
_(none yet)_

## Backtracking
_(none yet)_

## Graphs
_(none yet)_

## Advanced Graphs
_(none yet)_

## 1-D Dynamic Programming
_(none yet)_

## 2-D Dynamic Programming
_(none yet)_

## Greedy
_(none yet)_

## Intervals
_(none yet)_

## Math & Geometry
_(none yet)_

## Bit Manipulation
_(none yet)_
