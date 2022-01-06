import unittest
from unittest import result
from src.pykatsuyou.cli import main

class TestCLI(unittest.TestCase):
    # Edited cli.py to accept parameters for testing. Not sure how to test sys.argv
    def test_Help(self):
        test_result = main(['', '-h'])
        self.assertEqual(test_result, '\nUsage:\npykatsuyou [verb/adjective] [-h/-j/-l]\n*Must use dictionary form\n\nOptions:\n***A table is printed by default***\n-h (--help) = outputs this text\n-j (--json) = prints json\n-l (--list) = prints a list')

    def test_List(self):
        result = main(['', '行く', '-l'])
        self.assertListEqual(result, ["行く", "行きます","行った","行きました","行って","行け","行けば","行こう", "行かない", "行きません","行かなかった","行きませんでした","行かなくて","行くな","行かなければ"])