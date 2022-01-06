# -*- coding: utf-8 -*-

from src.pykatsuyou.ichidan import Ichidan
import unittest

class TestGodan(unittest.TestCase):
    def test_Rules(self):
        ichi = Ichidan()
        affirmative, negative = ichi.applyRules('上げる')
        self.assertListEqual(affirmative, ['上げる', '上げます', '上げた', '上げました', '上げて', '上げろ', '上げれば', '上げよう'])
        self.assertListEqual(negative, ['上げない', '上げません', '上げなかった', '上げませんでした', '上げなくて', '上げるな', 'ｘ', 'ｘ'])