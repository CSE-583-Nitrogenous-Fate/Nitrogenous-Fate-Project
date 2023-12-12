"""
This module contains the unit test functions for the nitrogenous fate (nfex)
project

Classes:
- TestKFEX(unittest.TestCase)
"""

import unittest
from nitrogenousfate import process_csv

class TestNFEX(unittest.TestCase):
    """
    TestNFEX(unittest.TestCase): tests the code for data cleaning and wranging for NFEX. 
    """

    def test_smoke_pass(self):
        """
        test_smoke_pass(self): Smoke test (1) verifying function should run without 
        crashing or throwing errors if given an appropriate CSV file.
        """
        csv_file = './data_tests/NFEX_test_diss_OK.csv'
        process_csv(csv_file)

    def test_invalid_csv(self):
        """
        test_invalid_csv(self): Test verifying function should throw exception 
        if we do not give it a valid address to a CSV file.
        """
        csv_file = 1
        with self.assertRaises(ValueError):
            process_csv(csv_file)

    def test_empty_csv(self):
        """
        test_empty_csv(self): Test verifying function should throw exception 
        if we give it an empty CSV file.
        """
        csv_file = './data_tests/NFEX_test_nodata.csv'
        with self.assertRaises(ValueError):
            process_csv(csv_file)

    def test_incorrect_dtype(self):
        """
        test_incorrect_dtype(self): Test verifying function should throw exception 
        if we give it a CSV file with incorrect data types (e.g. string instead of double)
        """
        csv_file = './data_tests/NFEX_test_wrongdatatype.csv'
        with self.assertRaises(ValueError):
            process_csv(csv_file)

unittest.main()
