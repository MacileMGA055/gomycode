#!/usr/bin/env python
# coding: utf-8

# In[1]:


def factorial(n):
      
    if n == 0:
        return 1
     
    return n * factorial(n-1)
  
# Driver Code
num = 5;
print("Factorial of", num, "is",
factorial(num))


# In[ ]:




