#!/usr/bin/env python3
import sys
import re
import pytest

def dna_rc(dna):
    seq = dna.upper()
    valid = {'A', 'C', 'G', 'T', 'N'}
    if not set(seq).issubset(valid):
        raise ValueError("Invalid characters in sequence")
    clean_dna = re.sub(r"\s+", "", dna) 
    #replace all non-characters with nothing
    seq = clean_dna.upper()
    seq = seq.replace('A', 't')
    seq = seq.replace('T', 'a')
    seq = seq.replace('G', 'c')
    seq = seq.replace('C', 'g')
    seq = seq[::-1]
    return seq.upper()

def test_dna_rc_lower():
    assert dna_rc('aattgg') == 'CCAATT'

def test_dna_rc_upper():
    assert dna_rc('AATTGG') == 'CCAATT'

def test_dna_rc_mix():
    assert dna_rc('aAtTgg') == 'CCAATT'

def test_dna_rc_non():
    try: 
        dna_rc('-ATCGN')
    except ValueError: #ValueError is caught
        return #and we return, passing the test
    assert False, 'expected ValueError exception'


