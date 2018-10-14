import unittest

from ShakerBattle.ShakerBattle.template import *


class TestTemplate(unittest.TestCase):
    def test_analyse_template(self):
        input = "template\n"
        res = "template\n"
        assert (analyse_template(input) == res)
