#!/usr/bin/env python3
import sys
import re
import pytest

def isnumeric(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


def test_isnumeric_num():
    assert isnumeric(1.3) == True

def test_isnumeric_str():
    assert isnumeric('1.3') == True

def test_isnumeric_exp():
    assert isnumeric('1e-6') == True

def test_isnumeric_dec():
    assert isnumeric(-0.0001) == True

def test_isnumeric_notnum():
    try:
        isnumeric('not-a-number')
    except False: #not a number is caught
        return #and we return, passing the test


