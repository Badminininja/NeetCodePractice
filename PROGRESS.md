# Progress Log

Tracking problems worked through, organized by NeetCode's roadmap categories. Each entry notes the actual approach taken, bugs caught along the way, and where the code lives in this repo.

## Arrays & Hashing
_(none yet)_

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
  - Code + self-tests: `solutions/stack/01-valid-parentheses.py`

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
