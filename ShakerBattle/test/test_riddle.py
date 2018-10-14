import unittest

from ShakerBattle.riddle import *

slow_riddle_list = [50, 57, 58, 59, 67, 75, 76, 85]
slow_riddle_list1 = [10512223142516, 51222314251617, 51222314251618, 51222314251619, 51222314251617, 51222314251617,
                     51222314251617, 51222314251618]


class TestRiddle(unittest.TestCase):

    def test_analyse_riddle(self):
        input1 = "47\n"
        input2 = "10000000\n"
        for i in range(0, 100):
            for j in range(0, 10000000):
                analyse_riddle(str(i) + "\n", input2 + "\n")
                #print(i)

    def test_analyse_riddle_example_1(self):
        input1 = "59\n"
        input2 = "6\n"
        assert (analyse_riddle(input1, input2) == "611213142519\n")

    def test_analyse_riddle_example_2(self):
        input1 = "87\n"
        input2 = "47\n"
        assert (analyse_riddle(input1, input2) == "6122132425161718\n")

    def test_analyse_riddle_50(self):
        input1 = str(slow_riddle_list[0]) + "\n"
        input2 = "10000000\n"
        print("We obtain " + analyse_riddle(input1, input2) + "\n")
        print("We need   " + str(slow_riddle_list1[0]) + "\n")
        assert(analyse_riddle(input1, input2) == str(slow_riddle_list1[0]) + "\n")

    def test_analyse_riddle_57(self):
        input1 = str(slow_riddle_list[1]) + "\n"
        input2 = "10000000\n"
        print("We obtain " + analyse_riddle(input1, input2) + "\n")
        print("We need   " + str(slow_riddle_list1[1]) + "\n")
        assert(analyse_riddle(input1, input2) == str(slow_riddle_list1[1]) + "\n")

    def test_analyse_riddle_97(self):
        input1 = "97\n"
        input2 = "1000000\n"
        assert (analyse_riddle(input1, input2) == "712213241526171819\n")

    def test_analyse_riddle_98(self):
        input1 = "98\n"
        input2 = "1000000\n"
        assert (analyse_riddle(input1, input2) == "712213241526171819\n")

    def test_analyse_riddle_max_less_1(self):
        input1 = "99\n"
        input2 = "1000000\n"
        assert (analyse_riddle(input1, input2) == "31123319\n")

    def test_analyse_riddle_max(self):
        input1 = "100\n"
        input2 = "1000000\n"
        assert (analyse_riddle(input1, input2) == "10311233\n")
