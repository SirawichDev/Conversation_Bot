# -*- coding: utf-8 -*-

import numpy as np
import tensorflow as tf 
import re
import time





#เตรียมข้อมูล

#import Data

lines = open('movie_lines.txt', encoding = 'utf-8', errors= 'ignore').read().split('\n')
conver = open('movie_conversations.txt', encoding='utf-8', errors='ignore').read().split('\n')