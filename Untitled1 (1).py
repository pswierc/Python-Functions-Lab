#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np

rulenumber = int(input("Enter the number of the rule you will use: "))

#rule 1

if rulenumber == 1:

    dA = float(input("Enter value for dA: "))
    c = float(input("Enter value for c: "))

    def rule1(dA, c):
        dQ = abs(c)*dA
        return dQ
    dQ = rule1(dA, c)
    
    print("dQ =", dQ)
    
#rule 2

if rulenumber == 2:
    
    c = float(input("Enter value for c: "))
    m = float(input("Enter value for m: "))
    A = float(input("Enter value for A: "))
    dA = float(input("Enter value for dA: "))
    
    def rule2(c, m, A, dA):
        dQ = abs(c*m*(A**(m-1)))*dA
        return dQ
    dQ = rule2(c, m, A, dA)
    
    print("dQ =", dQ)
    
#rule 3

if rulenumber == 3:
    
    dA = float(input("Enter value for dA: "))
    dB = float(input("Enter value for dB: "))
    
    def rule3(dA, dB):
        dQ = np.sqrt(dA**2+dB**2)
        return dQ
    dQ = rule3(dA, dB)
    
    print("dQ =", dQ)

#rule 4

if rulenumber == 4:
    
    dA = float(input("Enter value for dA: "))
    dB = float(input("Enter value for dB: "))
    Q = float(input("Enter value for Q: "))
    A = float(input("Enter value for A: "))
    B = float(input("Enter value for B: "))
    m = float(input("Enter value for m: "))
    n = float(input("Enter value for n: "))
    
    def rule4(dA, dB, Q, A, B, m, n):
        dQ = abs(Q)*np.sqrt(((m*(dA/A))**2)+((n*(dB/B))**2))
        return dQ
    dQ = rule4(dA, dB, Q, A, B, m, n)
    
    print("dQ =", dQ)

    
    
    
    
    
    
#activity 2

x = np.array([ 1.1, 1.3, 1.4, 0.9, 0.95, 1.05])

mean = np.average(x)
dx = np.std(x)/np.sqrt(6)

print("mean =", mean)
print("error in the mean =", dx)


#activity 3


# # Practice Heading

# $\delta Q = \sqrt{(\delta A)^2 + (\delta B)^2}$

# 
# $\delta F_{c} = f_{c} * \sqrt{(\delta m_{h} / m_{h})^2 + (\delta m / m)^2}$
# 
# $0.00796 = 0.784 * \sqrt{(0.0001 / 0.2083)^2 + (0.106 / 10.5)^2}$

# In[ ]:




