"""
The hello.py tests
"""
import unittest
import w1.plus_minus



class PlusMinusTest(unittest.TestCase):

    tcs = [
        "tc/1_0.txt",
        "tc/1_1.txt",
        "tc/1_2.txt",
    ]

    def test_plus_minus(self):
        print("hello")
    
