#!/usr/bin/env python3


from nose.tools import assert_equal
from typing import List
from ..dutch_national_flag_four_values import dutch_flag_four_values


def test_dutch_flag_four_values():
    A = [0,3,1,2,1,1,2,3,0]
    dutch_flag_four_values(A)
    assert_equal(is_partitioned(A), True)


def test_dutch_flag_four_values2():
    A = [3,3,3,2,2,1,1]
    dutch_flag_four_values(A)
    assert_equal(is_partitioned(A), True)


def test_dutch_flag_four_values3():
    A = [0,0,0,0,2,2,2,2,1,1,1,1,3,3,3,3]
    dutch_flag_four_values(A)
    assert_equal(is_partitioned(A), True)


def test_dutch_flag_four_values4():
    A = [3,2,1,0,3,2,1,0,3,2,1,0]
    dutch_flag_four_values(A)
    assert_equal(is_partitioned(A), True)


def test_dutch_flag_four_values5():
    A = [1,1,1,1,0,1,1,1,1,2,1,1,1,1,3]
    dutch_flag_four_values(A)
    assert_equal(is_partitioned(A), True)


def is_partitioned(A: List[int]) -> bool:
    j = 0
    for _ in range(4):
        if j >= len(A):
            break
        val = A[j] 
        while j < len(A) and A[j] == val:
            j += 1
    
    return j == len(A)