# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 15:27:10 2018

@author: yuukitamura
"""

points = {"国語" : 70, "算数" : 35, "英語" : 52}
sum = 0
for key in points:
    sum += points[key]
print(int(sum))