#!/bin/python
# -*- coding: utf-8 -*-

import unittest
import rmb
import rmb2

class TestRMB(unittest.TestCase) :

    def runTest(self) :
        self.assertEqual(rmb.capitalize(1203.45), u'壹仟贰佰零叁元肆角伍分')
        self.assertEqual(rmb.capitalize(6005430), u'陆佰万伍仟肆佰叁拾元整')
        self.assertEqual(rmb.capitalize(9000000876.50), u'玖拾亿零捌佰柒拾陆元伍角整')
        self.assertEqual(rmb.capitalize(9000003000.05), u'玖拾亿叁仟元零伍分')

        self.assertEqual(rmb2.capitalize(1203.45), u'壹仟贰佰零叁元肆角伍分')
        self.assertEqual(rmb2.capitalize(6005430), u'陆佰万伍仟肆佰叁拾元整')
        self.assertEqual(rmb2.capitalize(9000000876.50), u'玖拾亿零捌佰柒拾陆元伍角整')
        self.assertEqual(rmb2.capitalize(9000003000.05), u'玖拾亿叁仟元零伍分')

if __name__ == '__main__' :
    unittest.main()
