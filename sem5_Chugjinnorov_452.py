#!/usr/bin/env python
# coding: utf-8

# In[4]:


#1
def od():
    n=int(input())
    x=1
    while x<n+1:
        print('*'*x)
        x+=1
od()
        


# In[1]:


#2
def c():
    n=int(input())
    x=1
    while x<n+1:
        print(['*'*x])
        x+=1
c()


# In[14]:


#3
def a(students):
    x= max(students, key=students.get)
    y= min(students, key=students.get)
    return x,y
students = {'Bat': 400,
            'Oyun': 85,
            'Dulam': 999,
            'Suren': 500}
a(students)


# In[11]:


#4
import numpy as np
c=np.arange(1,1000)
k=0
for i in c:
    if i%3==0 or i%7==0:
        k=k+i
print(k)


# In[ ]:





# In[ ]:




