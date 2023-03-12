#!/usr/bin/env python
# coding: utf-8

# In[1]:

n = int(input())
x = 0
y = 1
for i in range(n):
	if i == 0:
		continue
	print(x, end=" ")
	for j in range(i):
		temp = x
		x = y
		y = temp + y
		print(x, end=" ")
	print()
	x = 0
	y = 1

# In[2]:

# In[ ]:
