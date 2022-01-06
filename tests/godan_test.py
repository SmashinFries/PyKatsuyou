# -*- coding: utf-8 -*-

from src.pykatsuyou.godan import Godan
import unittest

class TestGodan(unittest.TestCase):
    def test_checkVerb(self):
        godan = Godan('いく')
        self.assertAlmostEqual(godan.checkVerbType('行く'), 1)
    
    def test_nonU_MU(self):
        godan = Godan('のむ')
        affirmative, negative = godan.nonU('飲む', 10)
        self.assertListEqual(affirmative, ['飲む', '飲みます', '飲んだ', '飲みました', '飲んで', '飲め', '飲めば', '飲もう'])
        self.assertListEqual(negative, ['飲まない', '飲みません', '飲まなかった', '飲みませんでした', '飲まなくて', '飲むな', '飲まなければ', 'ｘ'])

    def test_nonU_KU(self):
        godan = Godan('きく')
        affirmative, negative = godan.nonU('聞く', 1)
        self.assertListEqual(affirmative, ['聞く', '聞きます', '聞いた', '聞きました', '聞いて', '聞け', '聞けば', '聞こう'])
        self.assertListEqual(negative, ['聞かない', '聞きません', '聞かなかった', '聞きませんでした', '聞かなくて', '聞くな', '聞かなければ', 'ｘ'])

    def test_nonU_GU(self):
        godan = Godan('およぐ')
        affirmative, negative = godan.nonU('泳ぐ', 2)
        self.assertListEqual(affirmative, ['泳ぐ', '泳ぎます', '泳いだ', '泳ぎました', '泳いで', '泳げ', '泳げば', '泳ごう'])
        self.assertListEqual(negative, ['泳がない', '泳ぎません', '泳がなかった', '泳ぎませんでした', '泳がなくて', '泳ぐな', '泳がなければ', 'ｘ'])

    def test_nonU_TSU(self):
        godan = Godan('まつ')
        affirmative, negative = godan.nonU('待つ', 5)
        self.assertListEqual(affirmative, ['待つ', '待ちます', '待った', '待ちました', '待って', '待て', '待てば', '待とう'])
        self.assertListEqual(negative, ['待たない', '待ちません', '待たなかった', '待ちませんでした', '待たなくて', '待つな', '待たなければ', 'ｘ'])
    
    def test_nonU_EXCEPTION(self):
        godan = Godan('かえる')
        affirmative, negative = godan.nonU('帰る', 12)
        self.assertListEqual(affirmative, ['帰る', '帰ります', '帰った', '帰りました', '帰って', '帰れ', '帰れば', '帰ろう'])
        self.assertListEqual(negative, ['帰らない', '帰りません', '帰らなかった', '帰りませんでした', '帰らなくて', '帰るな', '帰らなければ', 'ｘ'])