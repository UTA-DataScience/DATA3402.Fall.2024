#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
x = random.random()
print("The Value of x is", x)


# In[2]:


#Exercise 1: 
def generate_uniform(N, mymin, mymax):
    out = []
    c = random.randrange(mymin, mymax)*x
    h = mymin + c * random.random() 
    out.append(h)
    return out 


# In[3]:


data=generate_uniform(1000,-10,10)
print ("Data Type:", type(data))
print ("Data Length:", len(data))
if len(data)>0: 
    print ("Type of Data Contents:", type(data[0]))
    print ("Data Minimum:", min(data))
    print ("Data Maximum:", max(data))
    


# In[4]:


#Exercise 2: Write a function that computes the mean of values in a list. 
#Recall the equation for the mean of a random variable X c.
#computed on a data set of n values {xi} = {x1, x2, ..., xn}. 

def mean(Data):
    m=0 
    total = (1/len(Data)*sum(Data))
    m = +total
    return m 


# In[5]:


Data = [10, 990, 3, 5, 28, 90]
print ("Mean of Data",mean(Data))


# In[6]:


#Exercise 2b: Write a function that computes the variance of values in a list.
# Recall the equation for the variance of a random variable X
# on a data set of n values {xi} = {x1, x2, ..., xn} 
# is [x] = 1/n(Sum)(xi - x).

def variance(Data): 
    n=0
    h = []
    c = (1/len(Data)*(sum(Data)-((1/(len(Data))*sum(Data)))))
    h.append(c)   
    return h


# In[7]:


print("Variance of Data",variance(Data))


# In[103]:


#Exercise 3: Write a function that bins 
#the data so that you can create a histogram. 
def histogram(x, n_bins=10, x_min = None, x_max = None):
    if not x:
        raise ValueError("Input list 'x' cannot be empty.")

    # Find the minimum and maximum values
    x_min, x_max = min(x), max(x)

    # Calculate the bin size
    bin_size = (x_max - x_min) / n_bins

    # Initialize the histogram with zeros
    hist = [0] * n_bins

    # Populate the histogram
    for value in x:
        for i, _ in enumerate(hist):
            lower_edge = x_min + i * bin_size
            upper_edge = x_min + (i + 1) * bin_size
            if lower_edge <= value < upper_edge:
                hist[i] += 1

    # Compute the bin edges
    bin_edges = [x_min + i * bin_size for i in range(n_bins + 1)]

    return hist, bin_edges

        


# In[8]:


data = [2, 8, 4, 5.8, 7, 9, 10]


# In[9]:


histogram,bin_edges=histogram(data, 100)


# In[10]:


print("Histogram:",  histogram)
print("Bin Edges:", bin_edges)


# In[127]:


#Exercise4: Write a function that uses the histogram function in the previous exercise
# to create a text-based "graph". Where each line corresponds to a bin and the number 
# of #'s are proportional to the value of the data in the bin.
def draw_histogram(x, n_bins, x_min=None, character="#", max_character_per_line=20):
    # Calculate the histogram
    hist, bin_edges = histogram(x, n_bins, x_min)
    
    # Determine the maximum frequency to normalize the histogram
    max_freq = max(hist)
    if max_freq == 0:
        max_freq = 1  # Avoid division by zero
    
    # Initialize the result string
    result = ""
    
    # Iterate over the bins
    for i in range(len(hist)):
        left_bound = bin_edges[i]
        right_bound = bin_edges[i + 1]
        
        # Calculate the number of characters to represent the bin
        num_chars = int(hist[i] / max_freq * max_character_per_line)
        
        
        # Create the histogram line
        line = f"[{left_bound}, {right_bound}]: {character * num_chars}"
        
        # Add the line to the result string
        result += line + "\n"
    
    return result


# In[133]:


data_1 = [2, 8, 4, 5.8, 7, 9, 10, 99, 89, 56, 23, 10, 67, 43, 88]


# In[134]:


hist,bin_edges=histogram(data_1, 20)


# In[135]:


histogram_text = draw_histogram(data_1, 20)


# In[136]:


print(histogram_text)


# ## Functional Programming

# In[2]:


## Exercise5: Write a function the applies a booling function (that returns true/false) 
## to every element in data, and return a list of indices of elements where the result was true. 
## Use this function to find the indices of entries greater than 0.5.
def where(mylist, myfunc= 0.5):
    out = []
    
    for i, value in enumerate(mylist):
        if value > myfunc:
            out.append(i)
    
            return out 
        


# In[4]:


mylist = [0.9, 0.2, 0.08, 0.013]


# In[38]:


myfunc = 0.5 


# In[39]:


out_list = where(mylist, myfunc)


# In[40]:


out_list
# not sure what is going on here... 


# In[ ]:


## Exercise 6: The inrange(mymin, mymax) function below returns a function that 
## tests if it's input is between the specified values. Write corresponding
## functions that test:
## Even
## Odd
## Greater than
## Less than 
## Equal 
## Divisible by 


# In[7]:


def in_range(mymin, mymax):
    def testrange(x):
        return x<mymax and x>=mymin
    return testrange

F1=in_range(0,8)
F2=in_range(8, 16)

#Test of in_range
print (F1(0), F1(1), F1(8), F1(16))
print (F2(0), F2(1), F2(8), F2(16))

print ("Number of Entries passing F1:", len(where(mylist,F1)))
print ("Number of Entries passing F2:", len(where(mylist,F2)))


# In[6]:


mylist = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]


# ## Monte Carlo

# In[8]:


## Exercise 7:  Write a "generator" function called 
## generate_function(func,x_min,x_max,N), that 
## instead of generating a flat distribution, 
## generates a distribution with functional form coded in func. 
## Note that func will always be > 0.


# In[17]:


## Function 1: 
def generate_function(func, x_min, x_max, N = 100):
    out = list()
    
    test_x = random.range(8)
    x_min, x_max = min(test_x), max(test_x)
    p <= function(test_x)
    
    out.append(test_x)
    
    return out


# In[18]:


# Function 2: 
def test_func(x,a=1,b=1):
    return abs(a*x+b)


# In[19]:


## Testing function 1:
u = generate_function(func, x_min, x_max, N=100)


# In[20]:


# Exercise 8: Use your function to generate 1000 numbers 
# that are normal distributed, using the gaussian function 
# below. Confirm the mean and variance of the data is 
# close to the mean and variance you specify when 
# building the Gaussian. Histogram the data.

import math

def gaussian(mean, sigma):
    def f(x): 
        return math.exp(-((x-mean)**2)/(2*sigma**2))/math.sqrt(math.pi*sigma)
    return f
g1 = gaussian(0,1)
g2 = gaussian(10,3)


# In[21]:


g1


# In[22]:


g2


# In[26]:


# Exercise9: Combine your generate_function, where, and in_range functions
# above to create an integrate function. Use your integrate funciton to 
# show that approximately 68% of Normal distribution is within one variance

def integrate(func, x_min, x_max, n_points = 1000):
    delta_x = (x_max - x_min) / N
    integral_value = 0.5 * (func(x_min) + func(x_max))
    
    for i in range(1, N):
        x_i = x_min + i * delta_x
        integral_value += func(x_i)
    
    integral_value *= delta_x
    return integral_value

def normal_pdf(x):
    return (1 / math.sqrt(2 * math.pi)) * math.exp(-0.5 * x**2)
    
    return integral


# In[28]:


func = [990, 89, 67, 54, 6, 12, 34, 23]


# In[30]:


x_min = 6


# In[31]:


x_max = 990


# In[34]:


N = 1000


# In[36]:


integrate(func, x_min, x_max, n_points = 1000)


# In[ ]:




