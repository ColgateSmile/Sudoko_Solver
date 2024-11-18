import unittest
from loaders import CsvLoader


class LoaderTest(unittest.TestCase):
    @staticmethod
    def test_csv_loader():
        CsvLoader().load()
