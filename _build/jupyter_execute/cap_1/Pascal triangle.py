#!/usr/bin/env python
# coding: utf-8

# # El Triángulo de Pascal

# In[1]:


def pascal_triangle(n):
   trow = [1]
   y = [0]
   for x in range(max(n,0)):
      print(trow)
      trow=[l+r for l,r in zip(trow+y, y+trow)]
   return n>=1
pascal_triangle(10) 


# In[39]:


t=[1,2,1]
# t = [i+j for i,j in zip(t,t)]


# In[40]:


print(t)


# In[46]:


x=zip(t+[0],[0]+t)


# In[47]:


list(x)


# In[10]:


Guess


# In[17]:


radius = float(input("Radio (m): "))
print("El área es", 3.141592 * radius ** 2, "m2")
print("El diámetro", 3.141592 * radius * 2, "m")


# In[18]:


print("The cursor will stay on this line, at the end", end = "")


# In[1]:


import Guess


# In[1]:


get_ipython().run_line_magic('run', "-i 'Guess.py'")


# In[ ]:


"""
Author: Ken Lambert
Demonstrates a function that traps number format errors during input.
"""
def safeIntegerInput(prompt):
    """Prompts the user for an integer and returns the
    integer if it is well-formed. Otherwise, prints an
    error message and repeats this process."""
    inputString = input(prompt)
    try:
        number = int(inputString)
        return number
    except ValueError:
         print("Error in number format:", inputString)
    return safeIntegerInput(prompt)
if __name__ == "__main__":
    age = safeIntegerInput("Enter your age: ")
    print("Your age is", age)


# In[2]:


get_ipython().system('pip install --user keras')


# In[ ]:




