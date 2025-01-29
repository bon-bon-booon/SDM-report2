#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):

        def test_sample01 (self):
                self.assertEqual (180000, calc(300,600))

        def test_sample02 (self):
                self.assertEqual (1, calc(1,1))

        def test_sample03 (self):
                self.assertEqual (998001, calc(999,999))

        def test_sample04 (self):
                self.assertEqual (-1, calc(0,0))

        def test_sample05 (self):
                self.assertEqual (4, calc(2,2))

        def test_sample06 (self):
                self.assertEqual (996004, calc(998,998))

        def test_sample07 (self):
                self.assertEqual (-1, calc(1000,1000))

        def test_sample08 (self):
                self.assertEqual (-1, calc(-100,1111))

        def test_sample09 (self):
                self.assertEqual (-1, calc(2.3,965.6))

        def test_sample10 (self):
                self.assertEqual (-1, calc('abc','efg'))

        def test_sample11 (self):
                self.assertEqual (-1, calc('',''))

        def test_sample12 (self):
                self.assertEqual (-1, calc(100,'h3j4'))
        
        def test_sample13 (self):
                self.assertEqual (-1, calc('hello',400))

        def test_sample14 (self):
                self.assertEqual (-1, calc('112.3s','8.4d'))

