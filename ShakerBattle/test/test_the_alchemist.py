import unittest

from ShakerBattle.the_alchemist import *


class TestThe_Alchemist(unittest.TestCase):

    def test_analyse_the_alchemist(self):
        input1 = "47\n"

    def test_analyse_the_alchemist_example_1(self):
        input = "91 5 967\n"
        assert (analyse_the_alchemist(input) == "0\n")

    def test_analyse_the_alchemist_example_2(self):
        input = "69 83 2224\n"
        assert (analyse_the_alchemist(input) == "1\n")

    def test_analyse_the_alchemist_example_3(self):
        input = "38 100 973\n"
        assert (analyse_the_alchemist(input) == "3\n")
