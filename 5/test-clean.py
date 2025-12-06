import pytest
import clean

def test_works():
    assert clean.TestWorks() == True

def test_ranges1():
    ranges = ['2-5', '11-15', '6-12', '17-19']
    res = clean.CombineRanges(ranges)
    assert res == ['2-15', '17-19']

def test_ranges2():
    ranges = ['4-5','1-2','1-6']
    res = clean.CombineRanges(ranges)
    assert res == ['1-6']