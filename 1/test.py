
import pytest
#from aoc1 import TestWorks,run_with_file
import aoc1


def test_works():
    assert aoc1.TestWorks() == True

def test_test_input():
    input_file = "test.txt"
    start = 50

    totals = aoc1.run_with_file(input_file,start)
    assert totals == (3, 6)

def test_part1_lock_move_left_to_zero():
    lock = aoc1.Lock(50)
    lock.Move("L",50)
    assert lock.loc == 0

def test_part1_lock_move_left():
    lock = aoc1.Lock(50)
    lock.Move("L",101)
    assert lock.loc == 49

def test_part1_lock_move_right():
    lock = aoc1.Lock(50)
    lock.Move("R",50)
    assert lock.loc == 0

def test_part2_lock_move_left_a_little():
    lock = aoc1.Lock(50)
    passed = lock.Move("L",30)
    assert passed == 0

def test_part2_lock_move_right_a_little():
    lock = aoc1.Lock(50)
    passed = lock.Move("R",30)
    assert passed == 0

def test_part2_lock_move_left_to_zero():
    lock = aoc1.Lock(50)
    passed = lock.Move("L",50)
    assert passed == 1

def test_part2_lock_move_right_to_zero():
    lock = aoc1.Lock(50)
    passed = lock.Move("R",50)
    assert passed == 1

def test_part2_lock_move_left_past_zero():
    lock = aoc1.Lock(50)
    passed = lock.Move("L",60)
    assert passed == 1

def test_part2_lock_move_right_past_zero():
    lock = aoc1.Lock(50)
    passed = lock.Move("R",60)
    assert passed == 1

def test_part2_lock_move_left_big_past_zero():
    lock = aoc1.Lock(50)
    passed = lock.Move("L",160)
    assert passed == 2

def test_part2_lock_move_right_big_past_zero():
    lock = aoc1.Lock(50)
    passed = lock.Move("R",160)
    assert passed == 2

def test_part2_lock_move_left_big_to_zero():
    lock = aoc1.Lock(50)
    passed = lock.Move("L",150)
    assert passed == 2

def test_part2_lock_move_right_big_to_zero():
    lock = aoc1.Lock(50)
    passed = lock.Move("R",150)
    assert passed == 2

def test_part2_lock_move_left_none():
    lock = aoc1.Lock(0)
    passed = lock.Move("L",0)
    assert passed == 0

def test_part2_lock_move_right_none():
    lock = aoc1.Lock(0)
    passed = lock.Move("R",0)
    assert passed == 0

def test_wtf():
    lock = aoc1.Lock(1)
    passed = lock.Move("L",101)
    assert passed == 2

def test_part2_lock_move_left_less_than_fifty_to_zero():
    lock = aoc1.Lock(1)
    passed = lock.Move("L",1)
    assert passed == 1