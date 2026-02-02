#!/usr/bin/python3

import unittest
from calc_mul import calc
import sys

# Run with testrunner so needs to be in file test_

fmin = sys.float_info.min
fmax = sys.float_info.max

class TestCalc (unittest.TestCase):
        
        def test_eq_part1 (self):
                self.assertEqual(20, calc(1, 20))
        def test_eq_part2 (self):
                self.assertEqual(20, calc(4, 5))
        def test_eq_part3 (self):
                self.assertEqual(20, calc(20, 1))
        
        def test_edge1 (self):
                self.assertEqual(999, calc(1,999))
        def test_edge2 (self):
                self.assertEqual(-1, calc(0, 999))
        def test_edge3 (self):
                self.assertEqual(-1, calc(1,1000))
        def test_edge4 (self):
                self.assertEqual(-1, calc(0, 1000))

        def test_force_err1 (self):
                self.assertEqual(-1, calc(0.1, 200))
        def test_force_err2 (self):
                self.assertEqual(-1, calc(10, 200.5))
        def test_force_err3 (self):
                self.assertEqual(-1, calc(10, "hoge"))
        def test_force_err4 (self):
                self.assertEqual(-1, calc("hoge", 10))
        
        def test_repeat_yourself1 (self):
                for _ in range(10):
                        self.assertEqual(200, calc(10, 20))
        
        def test_of_uf1 (self):
                self.assertEqual(-1, calc(fmin, fmin))
        def test_of_uf2 (self):
                self.assertEqual(-1, calc(fmax, fmax))

        def test_zero (self):
                self.assertEqual(-1, calc(0, 0))

