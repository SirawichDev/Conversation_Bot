# -*- coding: utf-8 -*-

import numpy as np
import tensorflow as tf 
import re
import time





#เตรียมข้อมูล

#import Data

lines = open('movie_lines.txt', encoding = 'utf-8', errors= 'ignore').read().split('\n')
conver = open('movie_conversations.txt', encoding='utf-8', errors='ignore').read().split('\n')

#map id กับ conversation

map_text_id = {}
for line in lines:
    _line = line.split(' +++$+++ ')#_lineใช้เฉพาะใน loop
    if len(_line) == 5:
        map_text_id[_line[0]] = _line[4]#map id กับ text
      #  print(_line[4])
      # print(map_text_id[_line[0]])
      # break
        
conver_id_split= []
for convers in conver[:-1]:
    _convers = convers.split(' +++$+++ ')[-1][1:-1].replace("'","").replace(" ","")#เลือกindexสุดดท้ายแล้วตัด[]ออก
    #print(_convers)
    #break
    conver_id_split.append(_convers.split(','))
    #print(conver_split[0])
    #break

#Qe & A
answer = []
questions = []
for conversation in conver_id_split:
    for i in range(len(conversation)-1):
        questions.append(map_text_id[conversation[i]])
        answer.append(map_text_id[conversation[i+1]])
        #print(questions[0]+'\n')
        #print(answer[0])
        #break
    #break
#endofPredata

def clean_process(text):
    text = text.lower()
    #replace word
    text = re.sub(r"i'm","i am",text)
    text = re.sub(r"he's","he is",text)
    text = re.sub(r"she's","she is",text)
    text = re.sub(r"that's","that is",text)
    text = re.sub(r"what's","what is",text)
    text = re.sub(r"where's","where is",text)
    text = re.sub(r"\'ll"," will", text)
    text = re.sub(r"\'ve"," have", text)
    text = re.sub(r"\'d"," would", text)
    text = re.sub(r"\'re"," are", text)
    text = re.sub(r"won't","will not", text)
    text = re.sub(r"can't","cannot", text)
    text = re.sub(r"won't","will not", text)
    #text unnessecary symbol
    text = re.sub(r"[-()\"#/@;:<>{}+-=|.?,]", "", text)
    return text
    
#clean question
clean_question = []
for question in questions:
    clean_question.append(clean_process(question))


#clean answer
clean_answer = []
for answers in answer:
    clean_answer.append(clean_process(answers))

    
#สร้าง dictionary เพื่อให้ wordที่เหมือนกันนั้นเป็นตัวเลขขึ้นมา
word_count ={}
for question in clean_question:
    for word in question.split():
        if word not in word_count:
            word_count[word] = 1
        else:
            word_count[word] += 1
            
for answer in clean_answer:
    for word in answer.split():
        if word not in word_count:
            word_count[word] = 1
        else:
            word_count[word] += 1

#สร้าง 2 dictionary  ที่ map กันระหว่าง question กบั  answer
#นับความถี่
threshold = 20
question_to_int = {}
count_word = 0

for word, count in word_count.items():
    if count >= threshold:
        question_to_int[word] = count_word
        count_word +=1
        
answer_to_int = {}
count_word = 0

for word, count in word_count.items():
    if count >= threshold:
        answer_to_int[word] = count_word
        count_word +=1
        
        
#เพิ่มtoken ด้านหลัง dictonary
tokens = ['<PAD>','<EOS>','<OUT>','<SOS>']
for token in tokens:
    question_to_int[token] = len(question_to_int) + 1
for token in tokens:
    answer_to_int[token] = len(question_to_int) + 1

#ส้ราง dic แบบ invert ใน anser dic
#answer_to_int.items()
#สลับให้ word มาอยู่ด้านหลัง integer
answer_to_word = {w_i: w for w, w_i in answer_to_int.items()}       
        
            

            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
    
    
    
    
    
    
    
    
    
    
    