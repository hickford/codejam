#!python3
import pytest
from codejamhelpers import trials

def test_trials():
    assert trials([]) == [1]
    assert trials([0.6]) == [0.4, 0.6]
    assert trials([0.6,0.5]) == [0.2, 0.5, 0.3]
    assert trials([0.8,0.6,0.25]) == pytest.approx([0.06, 0.35, 0.47, 0.12])
