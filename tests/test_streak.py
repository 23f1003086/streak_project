import pytest
from streak import longest_positive_streak

def test_empty_list():
    """Tests that an empty list returns a streak of 0."""
    assert longest_positive_streak([]) == 0

def test_multiple_streaks():
    """Tests that the function correctly identifies the longest streak among multiple."""
    assert longest_positive_streak([1, 2, -1, 4, 5, 6, 0, 1]) == 3

def test_zeros_and_negatives():
    """Tests that zeros and negative numbers correctly break the streak."""
    assert longest_positive_streak([1, 2, 0, 3, 4, -5, 6, 7, 8]) == 3

def test_all_positive():
    """Tests a list containing only positive numbers."""
    assert longest_positive_streak([1, 2, 3, 4, 5]) == 5

def test_all_non_positive():
    """Tests a list with no positive numbers."""
    assert longest_positive_streak([-1, -2, 0, -5]) == 0

def test_single_element_list():
    """Tests lists with a single element."""
    assert longest_positive_streak([5]) == 1
    assert longest_positive_streak([-5]) == 0

def test_streak_at_end():
    """Tests when the longest streak is at the end of the list."""
    assert longest_positive_streak([-1, 0, 1, 2, 3, 4]) == 4