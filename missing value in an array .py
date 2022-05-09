#!/usr/bin/env python
# coding: utf-8

# In[21]:


# for number higher than zero 
A = [1,2,3,4,5,6,7,10]
missing_elements = []
for ele in range(A[0], A[-1]+1):
    if ele not in A:
        missing_elements.append(ele)
print(missing_elements)


# In[ ]:


#Set() is a Python unordered mutable datatype that holds only unique values.
arr = [1,2,3,4,5,7,6,9,10]
missing_value = set(range(arr[0], arr[-1]+1)) - set(arr)
print(missing_value)


# In[ ]:




