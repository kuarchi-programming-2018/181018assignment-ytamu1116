# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 15:31:49 2018

@author: yuukitamura
"""

class Gakusei:
    def __init__(self, kokugo, sansu):
        self.kokugo = kokugo
        self.sansu  = sansu

    def sum(self):
        return self.kokugo + self.sansu

yamada = Gakusei(70, 43)
print("合計は" + str(yamada.sum()) + "点です")