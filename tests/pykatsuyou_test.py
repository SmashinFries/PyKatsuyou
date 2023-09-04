# -*- coding: utf-8 -*-

import unittest
from unittest import result 
from src.pykatsuyou.pykatsuyou import getInflections

class TestMain(unittest.TestCase):
    def test_Main_Godan(self):
        result = getInflections('行く')
        self.assertListEqual(result['list'], ["行く", "行きます","行った","行きました","行って","行け","行けば","行こう", "行かない", "行きません","行かなかった","行きませんでした","行かなくて","行くな","行かなければ"])

    def test_Main_Ichi(self):
        result = getInflections('生きる')
        self.assertListEqual(result['list'], ["生きる", "生きます","生きた","生きました","生きて","生きろ","生きれば","生きよう", "生きない", "生きません","生きなかった","生きませんでした","生きなくて","生きるな"])

    def test_Main_Irreg(self):
        result = getInflections('する')
        self.assertListEqual(result['list'], ["する", "します","した","しました","して","しろ","すれば","しよう", "しない", "しません","しなかった","しませんでした","しなくて","するな","しなければ"])

    def test_Main_Adj(self):
        result = getInflections('高い')
        self.assertListEqual(result['list'], ["高い", "高かった", "高くない", "高くなかった"])
    
    def test_Main_Exception(self):
        result = getInflections('帰る')
        self.assertListEqual(result['list'], ["帰る", "帰ります", "帰った", "帰りました", "帰って", "帰れ", "帰れば", "帰ろう", "帰らない", "帰りません","帰らなかった","帰りませんでした","帰らなくて","帰るな","帰らなければ"])

    def test_Main_NotVA(self):
        result = getInflections('物')
        self.assertListEqual(result['list'], [])