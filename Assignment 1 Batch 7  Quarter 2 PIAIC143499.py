#!/usr/bin/env python
# coding: utf-8

# # Name: Ruhan Rafiq Bhaleshah
# # Roll Number: PIAIC143499
# # Batch: 7

# In[1]:


#method 1
import numpy as ruhan
ruhan.array([1,2,3,4,5])


# In[2]:


#method 2
ruhan.add(2,5)


# In[3]:


#method 3
ruhan.subtract(3,4)


# In[4]:


#method 4
ruhan.multiply(4,2)


# In[5]:


#method 5
ruhan.ones(10)


# In[6]:


#method 6
ruhan.zeros((2,4),dtype=float)


# In[7]:


#method 7
ruhan.full((3,2),77)


# In[8]:


#method 8
ruhan.arange(1,10,6)


# In[9]:


#method 9
ruhan.linspace(2,10,5)


# In[10]:


#method 10
ruhan.random.random((1,2))


# In[11]:


r=ruhan.eye(10)


# In[14]:


#method 11
ruhan.shape(r)


# In[15]:


#method 12
ruhan.empty(5)


# In[16]:


#method 13
r=ruhan.random.randint(1,10,(5,5))
r


# In[18]:


#method 14
ruhan.size(r)


# In[19]:


#method 15
r.dtype


# In[20]:


#method 16
r.data


# In[21]:


#method 17
r.itemsize


# In[22]:


#method 18
r.ndim


# In[23]:


#method 19
s=ruhan.random.default_rng(10)
s


# In[24]:


#method 20
t=ruhan.random.randint(0,10,(3,3))
t


# In[25]:


#method 21
t.min()


# In[26]:


#method 22
t.max()


# In[27]:


#method 23
t.mean()


# In[28]:


#method 24
t.sum()


# In[29]:


#method 26
ruhan.exp(t)


# In[30]:


#method 27
ruhan.random.seed(1)
ruhan.random.random((5,5))


# In[31]:


#method 28
t.ravel()


# In[32]:


#method 29
ruhan.abs(t)


# In[33]:


#method 30
ruhan.pi


# In[34]:


#method 31
ruhan.sin(t)


# In[35]:


#method 32
ruhan.cos(t)


# In[36]:


#method 33
ruhan.tan(t)


# In[51]:


#method 34
ruhan.arcsin(0.10)


# In[52]:


#method 35
ruhan.arccos(0.10)


# In[53]:


#method 36
ruhan.arctan(0.10)


# In[54]:


#method 37
ruhan.log(t)


# In[55]:


#method 38
ruhan.log2(t)


# In[56]:


#method 39
ruhan.log10(t)


# In[57]:


#method 40
ruhan.add.reduce(t)


# In[58]:


#method 41
ruhan.multiply.reduce(t)


# In[59]:


#method 42
ruhan.add.accumulate(t)


# In[60]:


#method 43
ruhan.multiply.accumulate(t)


# In[61]:


#method 44
ruhan.power(1,2)


# In[63]:


#method 45
ruhan.hsplit(t,3)


# In[64]:


#method 46
ruhan.vsplit(t,3)


# In[65]:


#method 47
ruhan.absolute(t)


# In[66]:


#method 48
ruhan.prod(t)


# In[67]:


#method 49
ruhan.std(t)


# In[68]:


#method 50
ruhan.var(t)


# In[ ]:




