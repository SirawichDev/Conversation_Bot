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
        map_text_id[_line[0]] = _line[4]#map id กับ text
      #  print(_line[4])
      # print(map_text_id[_line[0]])
      # break
        
conver_split= []
for convers in conver[:-1]:
    _convers = convers.split(' +++$+++ ')[-1][1:-1].replace("'","").replace(" ","")#เลือกindexสุดดท้ายแล้วตัด[]ออก
    #print(_convers)
    #break
    conver_split.append(_convers.split(','))
    #print(conver_split[0])
    #break