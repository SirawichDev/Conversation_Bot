# -*- coding: utf-8 -*-

import numpy as np
import tensorflow as tf 
import re
import time





#เตรียมข้อมูล

#import Data

lines = open('movie_lines.txt', encoding = 'utf-8', errors= 'ignore').read().split('\n')
conver = open('movie_conversations.txt', encoding='utf-8', errors='ignore').read().split('\n')

#map id กับ line

map_text_id = {}
for line in lines:
    _line = line.split(' +++$+++ ')#_lineใช้เฉพาะใน loop
    if len(_line) == 5:
        map_text_id[_line[0]] = _line[4] #map id กับ text
        
