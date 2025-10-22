#!/usr/bin/env python3
import sys
import re
import pytest

def gc_content(seq):
    uppseq = seq.upper()
    valid = {'A', 'C', 'G', 'T', 'N'}
    if not set(uppseq).issubset(valid):
        raise ValueError("Invalid characters in sequence")
    if len(uppseq) == 0:
        return 0
    return round((uppseq.count('G') + uppseq.count('C')) / len(uppseq), 2)

def test_gc_gc():
    assert gc_content('GCGC') == 1.00

def test_gc_at():
    assert gc_content('ATAT') == 0.00

def test_gc_acgt():
    assert gc_content('ATGC') == 0.50

def test_gc_empty():
    assert gc_content('') == 0.00

def test_gc_X():
    try:
        gc_content("ATGXB")
    except ValueError: #ValueError is caught
        return #and we return, passing the test
    assert False, 'expected ValueError exception'

def test_gc_N():
    assert gc_content("ATGNNTAGC") == 0.33

def test_gc_lower():
    assert gc_content('gattacaa') == 0.25