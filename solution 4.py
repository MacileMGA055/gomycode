#!/usr/bin/env python
# coding: utf-8

# In[1]:


def remove_char(str, n):
      first_part = str[:n] 
      last_part = str[n+1:]
      return first_part + last_part
print(remove_char('Kitten', 1))
print(remove_char('Kitten', 0))
print(remove_char('Kitten', 4))


# In[ ]:




