#coding:utf-8

from math import isnan
import numpy as np
# f=open('data2.txt', 'r')
# f2=open('data3.txt', 'w')
# for line in f.readlines()[:10]:
#      f2.write(line)
# f2.close()
# f.close()

import pandas as pd
data=pd.read_csv('cluster_10')
# print(data)
# print(data.columns[1])
with open('10.txt','w', encoding='utf-8') as f:
    f.write(data.columns[1].replace('\n','').replace('\u3000','')+'\n')
    for i in data[data.columns[1]]:
        f.write(i.replace('\n','').replace('\u3000','')+'\n')



data=pd.read_csv('cluster_0')
# print(data)
# print(data.columns[1])
with open('0.txt','w', encoding='utf-8') as f:
    f.write(data.columns[1].replace('\n','').replace('\u3000','')+'\n')
    for i in data[data.columns[1]]:
        f.write(i.replace('\n','').replace('\u3000','')+'\n')


data=pd.read_csv('cluster_1')
# print(data)
# print(data.columns[1])
with open('1.txt','w', encoding='utf-8') as f:
    f.write(data.columns[1].replace('\n','').replace('\u3000','')+'\n')
    for i in data[data.columns[1]]:
        if type(i)==type(''):
            f.write(i.replace('\n','').replace('\u3000','')+'\n')


data=pd.read_csv('cluster_2')
# print(data)
# print(data.columns[1])
with open('2.txt','w', encoding='utf-8') as f:
    f.write(data.columns[1].replace('\n','').replace('\u3000','')+'\n')
    for i in data[data.columns[1]]:
        if type(i) == type(''):
            f.write(i.replace('\n','').replace('\u3000','')+'\n')


data=pd.read_csv('cluster_3')
# print(data)
# print(data.columns[1])
with open('3.txt','w', encoding='utf-8') as f:
    f.write(data.columns[1].replace('\n','').replace('\u3000','')+'\n')
    for i in data[data.columns[1]]:
        if type(i) == type(''):
            f.write(i.replace('\n','').replace('\u3000','')+'\n')


data=pd.read_csv('cluster_4')
# print(data)
# print(data.columns[1])
with open('4.txt','w', encoding='utf-8') as f:
    f.write(data.columns[1].replace('\n','').replace('\u3000','')+'\n')
    for i in data[data.columns[1]]:
        # print(i)
        if type(i) == type(''):
            f.write(i.replace('\n','').replace('\u3000','')+'\n')


data=pd.read_csv('cluster_5')
# print(data)
# print(data.columns[1])
with open('5.txt','w', encoding='utf-8') as f:
    f.write(data.columns[1].replace('\n','').replace('\u3000','')+'\n')
    for i in data[data.columns[1]]:
        if type(i) == type(''):
            f.write(i.replace('\n','').replace('\u3000','')+'\n')


data=pd.read_csv('cluster_6')
# print(data)
# print(data.columns[1])
with open('6.txt','w', encoding='utf-8') as f:
    f.write(data.columns[1].replace('\n','').replace('\u3000','')+'\n')
    for i in data[data.columns[1]]:
        if type(i) == type(''):
            f.write(i.replace('\n','').replace('\u3000','')+'\n')


data=pd.read_csv('cluster_7')
# print(data)
# print(data.columns[1])
with open('7.txt','w', encoding='utf-8') as f:
    f.write(data.columns[1].replace('\n','').replace('\u3000','')+'\n')
    for i in data[data.columns[1]]:
        if type(i) == type(''):
            f.write(i.replace('\n','').replace('\u3000','')+'\n')


data=pd.read_csv('cluster_8')
# print(data)
# print(data.columns[1])
with open('8.txt','w', encoding='utf-8') as f:
    f.write(data.columns[1].replace('\n','').replace('\u3000','')+'\n')
    for i in data[data.columns[1]]:
        if type(i) == type(''):
            f.write(i.replace('\n','').replace('\u3000','')+'\n')


data=pd.read_csv('cluster_9')
# print(data)
# print(data.columns[1])
with open('9.txt','w', encoding='utf-8') as f:
    f.write(data.columns[1].replace('\n','').replace('\u3000','')+'\n')
    for i in data[data.columns[1]]:
        if type(i) == type(''):
            f.write(i.replace('\n','').replace('\u3000','')+'\n')

