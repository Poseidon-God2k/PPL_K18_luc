import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    
    def test_wrong_miss_close(self):
        """Miss variable"""
        input = """Var: a_95;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,201))