import sys
sys.path.append('../')
from metafix.components.StringReplacers import StringReplacers
import unittest

replacer = StringReplacers()

class TestStringMethods(unittest.TestCase):

    def test_forwardSlashToSemiColon(self):
        initalString = 'test_/'
        expectedString = 'test_;'
        updatedString = replacer.forwardSlashToSemiColon(initalString)
        self.assertEqual(updatedString, expectedString)


if __name__ == '__main__':
    unittest.main()
