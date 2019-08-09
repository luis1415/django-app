#!/usr/bin/env python
# -*- coding: utf-8 -*-

def column(num, res = ''):
   return column((num - 1) // 26, u'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'[(num - 1) % 27] + res) if num > 0 else res


print(column(69))