import pytest
import aoc2

def test_works():
    assert aoc2.TestWorks() == True

def test_test_input():
    input_file = "test.txt"
    total = aoc2.run_with_file(input_file)
    assert total == 1227775554

def test_test_range1():
    s = aoc2.do_range(3,23)
    assert s == 33

def test_test_range2():
    s = aoc2.do_range(11,22)
    assert s == 33

def test_test_range3():
    s = aoc2.do_range(998,1012)
    assert s == 1010

def test_test_range4():
    s = aoc2.do_range(95,115)
    assert s == 99
