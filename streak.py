from typing import List

def longest_positive_streak(nums: List[int]) -> int:
    """
    Returns the length of the longest consecutive run of positive (>0) numbers.

    - An empty list returns 0.
    - Non-positive numbers break the streak.
    - Must be deterministic: no prints, no randomness, no global state.
    """
    max_streak = 0
    current_streak = 0
    for num in nums:
        if num > 0:
            current_streak += 1
        else:
            current_streak = 0
        max_streak = max(max_streak, current_streak)
    return max_streak