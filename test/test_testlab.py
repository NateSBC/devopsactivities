import pytest
from pytest_files.testlab import count

def test_empty_sequence():
  assert count([], 1) == 0

def test_item_in_sequence():
  assert count([1, 2, 3, 4], 1) == 1

def test_multiple_in_sequence():
  assert count([1, 2, 3, 1, 4], 1) == 2
  
