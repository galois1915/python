#!/usr/bin/env python
# coding: utf-8

# <p style="font-family: Arial; font-size:3.75em;color:purple; font-style:bold"><br>
# Introduction to numpy:
# </p><br>
# 
# <p style="font-family: Arial; font-size:1.25em;color:#2462C0; font-style:bold"><br>
# Package for scientific computing with Python
# </p><br>
# 
# Numerical Python, or "Numpy" for short, is a foundational package on which many of the most common data science packages are built.  Numpy provides us with high performance multi-dimensional arrays which we can use as vectors or matrices.  
# 
# The key features of numpy are:
# 
# - ndarrays: n-dimensional arrays of the same data type which are fast and space-efficient.  There are a number of built-in methods for ndarrays which allow for rapid processing of data without using loops (e.g., compute the mean).
# - Broadcasting: a useful tool which defines implicit behavior between multi-dimensional arrays of different sizes.
# - Vectorization: enables numeric operations on ndarrays.
# - Input/Output: simplifies reading and writing of data from/to file.
# 
# <b>Additional Recommended Resources:</b><br>
# <a href="https://docs.scipy.org/doc/numpy/reference/">Numpy Documentation</a><br>
# <i>Python for Data Analysis</i> by Wes McKinney<br>
# <i>Python Data science Handbook</i> by Jake VanderPlas
# 
# 

# <p style="font-family: Arial; font-size:2.75em;color:purple; font-style:bold"><br>
# 
# Getting started with ndarray<br><br></p>
# 
# **ndarrays** are time and space-efficient multidimensional arrays at the core of numpy.  Like the data structures in Week 2, let's get started by creating ndarrays using the numpy package.

# <p style="font-family: Arial; font-size:1.75em;color:#2462C0; font-style:bold"><br>
# 
# How to create Rank 1 numpy arrays:
# </p>

# In[1]:


import numpy as np

an_array = np.array([3, 33, 333])  # Create a rank 1 array

print(type(an_array))              # The type of an ndarray is: "<class 'numpy.ndarray'>"


# In[2]:


# test the shape of the array we just created, it should have just one dimension (Rank 1)
print(an_array.shape)


# In[3]:


# because this is a 1-rank array, we need only one index to accesss each element
print(an_array[0], an_array[1], an_array[2]) 


# In[4]:


an_array[0] =888            # ndarrays are mutable, here we change an element of the array

print(an_array)


# <p style="font-family: Arial; font-size:1.75em;color:#2462C0; font-style:bold"><br>
# 
# How to create a Rank 2 numpy array:</p>
# 
# A rank 2 **ndarray** is one with two dimensions.  Notice the format below of [ [row] , [row] ].  2 dimensional arrays are great for representing matrices which are often useful in data science.

# In[5]:


another = np.array([[11,12,13],[21,22,23]])   # Create a rank 2 array

print(another)  # print the array

print("The shape is 2 rows, 3 columns: ", another.shape)  # rows x columns                   

print("Accessing elements [0,0], [0,1], and [1,0] of the ndarray: ", another[0, 0], ", ",another[0, 1],", ", another[1, 0])


# <p style="font-family: Arial; font-size:1.75em;color:#2462C0; font-style:bold"><br>
# 
# There are many way to create numpy arrays:
# </p>
# 
# Here we create a number of different size arrays with different shapes and different pre-filled values.  numpy has a number of built in methods which help us quickly and easily create multidimensional arrays.

# In[6]:


import numpy as np

# create a 2x2 array of zeros
ex1 = np.zeros((2,2))      
print(ex1)                              


# In[7]:


# create a 2x2 array filled with 9.0
ex2 = np.full((2,2), 9.0)  
print(ex2)   


# In[8]:


# create a 2x2 matrix with the diagonal 1s and the others 0
ex3 = np.eye(2,2)
print(ex3)  


# In[9]:


# create an array of ones
ex4 = np.ones((1,2))
print(ex4)    


# In[10]:


# notice that the above ndarray (ex4) is actually rank 2, it is a 2x1 array
print(ex4.shape)

# which means we need to use two indexes to access an element
print()
print(ex4[0,1])


# In[11]:


# create an array of random floats between 0 and 1
ex5 = np.random.random((2,2))
print(ex5)    


# <p style="font-family: Arial; font-size:2.75em;color:purple; font-style:bold"><br>
# 
# Array Indexing
# <br><br></p>

# <p style="font-family: Arial; font-size:1.75em;color:#2462C0; font-style:bold"><br>
# Slice indexing:
# </p>
# 
# Similar to the use of slice indexing with lists and strings, we can use slice indexing to pull out sub-regions of ndarrays.

# In[12]:


import numpy as np

# Rank 2 array of shape (3, 4)
an_array = np.array([[11,12,13,14], [21,22,23,24], [31,32,33,34]])
print(an_array)


# Use array slicing to get a subarray consisting of the first 2 rows x 2 columns.

# In[13]:


a_slice = an_array[:2, 1:3]
print(a_slice)


# When you modify a slice, you actually modify the underlying array.

# In[14]:


print("Before:", an_array[0, 1])   #inspect the element at 0, 1  
a_slice[0, 0] = 1000    # a_slice[0, 0] is the same piece of data as an_array[0, 1]
print("After:", an_array[0, 1])    


# <p style="font-family: Arial; font-size:1.75em;color:#2462C0; font-style:bold"><br>
# 
# Use both integer indexing & slice indexing
# </p>
# 
# We can use combinations of integer indexing and slice indexing to create different shaped matrices.

# In[15]:


# Create a Rank 2 array of shape (3, 4)
an_array = np.array([[11,12,13,14], [21,22,23,24], [31,32,33,34]])
print(an_array)


# In[16]:


# Using both integer indexing & slicing generates an array of lower rank
row_rank1 = an_array[1, :]    # Rank 1 view 

print(row_rank1, row_rank1.shape)  # notice only a single []


# In[17]:


# Slicing alone: generates an array of the same rank as the an_array
row_rank2 = an_array[1:2, :]  # Rank 2 view 

print(row_rank2, row_rank2.shape)   # Notice the [[ ]]


# In[18]:


#We can do the same thing for columns of an array:

print()
col_rank1 = an_array[:, 1]
col_rank2 = an_array[:, 1:2]

print(col_rank1, col_rank1.shape)  # Rank 1
print()
print(col_rank2, col_rank2.shape)  # Rank 2


# <p style="font-family: Arial; font-size:1.75em;color:#2462C0; font-style:bold"><br>
# 
# Array Indexing for changing elements:
# </p>

# Sometimes it's useful to use an array of indexes to access or change elements.

# In[19]:


# Create a new array
an_array = np.array([[11,12,13], [21,22,23], [31,32,33], [41,42,43]])

print('Original Array:')
print(an_array)


# In[20]:


# Create an array of indices
col_indices = np.array([0, 1, 2, 0])
print('\nCol indices picked : ', col_indices)

row_indices = np.arange(4)
print('\nRows indices picked : ', row_indices)


# In[21]:


# Examine the pairings of row_indices and col_indices.  These are the elements we'll change next.
for row,col in zip(row_indices,col_indices):
    print(row, ", ",col)


# In[22]:


# Select one element from each row
print('Values in the array at those indices: ',an_array[row_indices, col_indices])


# In[23]:


# Change one element from each row using the indices selected
an_array[row_indices, col_indices] += 100000

print('\nChanged Array:')
print(an_array)


# <p style="font-family: Arial; font-size:2.75em;color:purple; font-style:bold"><br>
# Boolean Indexing
# 
# <br><br></p>
# <p style="font-family: Arial; font-size:1.75em;color:#2462C0; font-style:bold"><br>
# 
# Array Indexing for changing elements:
# </p>

# In[24]:


# create a 3x2 array
an_array = np.array([[11,12], [21, 22], [31, 32]])
print(an_array)


# In[25]:


# create a filter which will be boolean values for whether each element meets this condition
filter = (an_array > 15)
filter


# Notice that the filter is a same size ndarray as an_array which is filled with True for each element whose corresponding element in an_array which is greater than 15 and False for those elements whose value is less than 15.

# In[26]:


# we can now select just those elements which meet that criteria
print(an_array[filter])


# In[27]:


# For short, we could have just used the approach below without the need for the separate filter array.

an_array[an_array > 15]


# What is particularly useful is that we can actually change elements in the array applying a similar logical filter.  Let's add 100 to all the even values.

# In[28]:


an_array[an_array % 2 == 0] +=100
print(an_array)


# <p style="font-family: Arial; font-size:2.75em;color:purple; font-style:bold"><br>
# 
# Datatypes and Array Operations
# <br><br></p>

# <p style="font-family: Arial; font-size:1.75em;color:#2462C0; font-style:bold"><br>
# 
# Datatypes:
# </p>

# In[29]:


ex1 = np.array([11, 12]) # Python assigns the  data type
print(ex1.dtype)


# In[30]:


ex2 = np.array([11.0, 12.0]) # Python assigns the  data type
print(ex2.dtype)


# In[31]:


ex3 = np.array([11, 21], dtype=np.int64) #You can also tell Python the  data type
print(ex3.dtype)


# In[32]:


# you can use this to force floats into integers (using floor function)
ex4 = np.array([11.1,12.7], dtype=np.int64)
print(ex4.dtype)
print()
print(ex4)


# In[33]:


# you can use this to force integers into floats if you anticipate
# the values may change to floats later
ex5 = np.array([11, 21], dtype=np.float64)
print(ex5.dtype)
print()
print(ex5)


# <p style="font-family: Arial; font-size:1.75em;color:#2462C0; font-style:bold"><br>
# 
# Arithmetic Array Operations:
# 
# </p>

# In[34]:


x = np.array([[111,112],[121,122]], dtype=np.int)
y = np.array([[211.1,212.1],[221.1,222.1]], dtype=np.float64)

print(x)
print()
print(y)


# In[35]:


# add
print(x + y)         # The plus sign works
print()
print(np.add(x, y))  # so does the numpy function "add"


# In[36]:


# subtract
print(x - y)
print()
print(np.subtract(x, y))


# In[37]:


# multiply
print(x * y)
print()
print(np.multiply(x, y))


# In[38]:


# divide
print(x / y)
print()
print(np.divide(x, y))


# In[39]:


# square root
print(np.sqrt(x))


# In[40]:


# exponent (e ** x)
print(np.exp(x))


# <p style="font-family: Arial; font-size:2.75em;color:purple; font-style:bold"><br>
# 
# Statistical Methods, Sorting, and <br> <br> Set Operations:
# <br><br>
# </p>

# <p style="font-family: Arial; font-size:1.75em;color:#2462C0; font-style:bold"><br>
# 
# Basic Statistical Operations:
# </p>

# In[41]:


# setup a random 2 x 4 matrix
arr = 10 * np.random.randn(2,5)
print(arr)


# In[42]:


# compute the mean for all elements
print(arr.mean())


# In[43]:


# compute the means by row
print(arr.mean(axis = 1))


# In[44]:


# compute the means by column
print(arr.mean(axis = 0))


# In[45]:


# sum all the elements
print(arr.sum())


# In[46]:


# compute the medians
print(np.median(arr, axis = 1))


# <p style="font-family: Arial; font-size:1.75em;color:#2462C0; font-style:bold"><br>
# 
# Sorting:
# </p>
# 

# In[47]:


# create a 10 element array of randoms
unsorted = np.random.randn(10)

print(unsorted)


# In[48]:


# create copy and sort
sorted = np.array(unsorted)
sorted.sort()

print(sorted)
print()
print(unsorted)


# In[49]:


# inplace sorting
unsorted.sort() 

print(unsorted)


# <p style="font-family: Arial; font-size:1.75em;color:#2462C0; font-style:bold"><br>
# 
# Finding Unique elements:
# </p>

# In[50]:


array = np.array([1,2,1,4,2,1,4,2])

print(np.unique(array))


# <p style="font-family: Arial; font-size:1.75em;color:#2462C0; font-style:bold"><br>
# 
# Set Operations with np.array data type:
# </p>

# In[51]:


s1 = np.array(['desk','chair','bulb'])
s2 = np.array(['lamp','bulb','chair'])
print(s1, s2)


# In[52]:


print( np.intersect1d(s1, s2) ) 


# In[53]:


print( np.union1d(s1, s2) )


# In[54]:


print( np.setdiff1d(s1, s2) )# elements in s1 that are not in s2


# In[55]:


print( np.in1d(s1, s2) )#which element of s1 is also in s2


# <p style="font-family: Arial; font-size:2.75em;color:purple; font-style:bold"><br>
# 
# Broadcasting:
# <br><br>
# </p>

# Introduction to broadcasting. <br>
# For more details, please see: <br>
# https://docs.scipy.org/doc/numpy-1.10.1/user/basics.broadcasting.html

# In[56]:


import numpy as np

start = np.zeros((4,3))
print(start)


# In[57]:


# create a rank 1 ndarray with 3 values
add_rows = np.array([1, 0, 2])
print(add_rows)


# In[58]:


y = start + add_rows  # add to each row of 'start' using broadcasting
print(y)


# In[59]:


# create an ndarray which is 4 x 1 to broadcast across columns
add_cols = np.array([[0,1,2,3]])
add_cols = add_cols.T

print(add_cols)


# In[60]:


# add to each column of 'start' using broadcasting
y = start + add_cols 
print(y)


# In[61]:


# this will just broadcast in both dimensions
add_scalar = np.array([1])  
print(start+add_scalar)


# Example from the slides:

# In[62]:


# create our 3x4 matrix
arrA = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(arrA)


# In[63]:


# create our 4x1 array
arrB = [0,1,0,2]
print(arrB)


# In[64]:


# add the two together using broadcasting
print(arrA + arrB)


# <p style="font-family: Arial; font-size:2.75em;color:purple; font-style:bold"><br>
# 
# Speedtest: ndarrays vs lists
# <br><br>
# </p>

# First setup paramaters for the speed test. We'll be testing time to sum elements in an ndarray versus a list.

# In[65]:


from numpy import arange
from timeit import Timer

size    = 1000000
timeits = 1000


# In[66]:


# create the ndarray with values 0,1,2...,size-1
nd_array = arange(size)
print( type(nd_array) )


# In[67]:


# timer expects the operation as a parameter, 
# here we pass nd_array.sum()
timer_numpy = Timer("nd_array.sum()", "from __main__ import nd_array")

print("Time taken by numpy ndarray: %f seconds" % 
      (timer_numpy.timeit(timeits)/timeits))


# In[68]:


# create the list with values 0,1,2...,size-1
a_list = list(range(size))
print (type(a_list) )


# In[69]:


# timer expects the operation as a parameter, here we pass sum(a_list)
timer_list = Timer("sum(a_list)", "from __main__ import a_list")

print("Time taken by list:  %f seconds" % 
      (timer_list.timeit(timeits)/timeits))


# <p style="font-family: Arial; font-size:2.75em;color:purple; font-style:bold"><br>
# 
# Read or Write to Disk:
# <br><br>
# </p>

# <p style="font-family: Arial; font-size:1.3em;color:#2462C0; font-style:bold"><br>
# 
# Binary Format:</p>

# In[70]:


x = np.array([ 23.23, 24.24] )


# In[71]:


np.save('an_array', x)


# In[72]:


np.load('an_array.npy')


# <p style="font-family: Arial; font-size:1.3em;color:#2462C0; font-style:bold"><br>
# 
# Text Format:</p>

# In[73]:


np.savetxt('array.txt', X=x, delimiter=',')


# In[74]:


get_ipython().system('cat array.txt')


# In[75]:


np.loadtxt('array.txt', delimiter=',')


# <p style="font-family: Arial; font-size:2.75em;color:purple; font-style:bold"><br>
# 
# Additional Common ndarray Operations
# <br><br></p>

# <p style="font-family: Arial; font-size:1.75em;color:#2462C0; font-style:bold"><br>
# 
# Dot Product on Matrices and Inner Product on Vectors:
# 
# </p>

# In[76]:


# determine the dot product of two matrices
x2d = np.array([[1,1],[1,1]])
y2d = np.array([[2,2],[2,2]])

print(x2d.dot(y2d))
print()
print(np.dot(x2d, y2d))


# In[77]:


# determine the inner product of two vectors
a1d = np.array([9 , 9 ])
b1d = np.array([10, 10])

print(a1d.dot(b1d))
print()
print(np.dot(a1d, b1d))


# In[78]:


# dot produce on an array and vector
print(x2d.dot(a1d))
print()
print(np.dot(x2d, a1d))


# <p style="font-family: Arial; font-size:1.75em;color:#2462C0; font-style:bold"><br>
# 
# Sum:
# </p>

# In[79]:


# sum elements in the array
ex1 = np.array([[11,12],[21,22]])

print(np.sum(ex1))          # add all members


# In[80]:


print(np.sum(ex1, axis=0))  # columnwise sum


# In[81]:


print(np.sum(ex1, axis=1))  # rowwise sum


# <p style="font-family: Arial; font-size:1.75em;color:#2462C0; font-style:bold"><br>
# 
# Element-wise Functions: </p>
# 
# For example, let's compare two arrays values to get the maximum of each.

# In[82]:


# random array
x = np.random.randn(8)
x


# In[83]:


# another random array
y = np.random.randn(8)
y


# In[84]:


# returns element wise maximum between two arrays

np.maximum(x, y)


# <p style="font-family: Arial; font-size:1.75em;color:#2462C0; font-style:bold"><br>
# 
# Reshaping array:
# </p>

# In[85]:


# grab values from 0 through 19 in an array
arr = np.arange(20)
print(arr)


# In[86]:


# reshape to be a 4 x 5 matrix
arr.reshape(4,5)


# <p style="font-family: Arial; font-size:1.75em;color:#2462C0; font-style:bold"><br>
# 
# Transpose:
# 
# </p>

# In[87]:


# transpose
ex1 = np.array([[11,12],[21,22]])

ex1.T


# <p style="font-family: Arial; font-size:1.75em;color:#2462C0; font-style:bold"><br>
# 
# Indexing using where():</p>

# In[88]:


x_1 = np.array([1,2,3,4,5])

y_1 = np.array([11,22,33,44,55])

filter = np.array([True, False, True, False, True])


# In[89]:


out = np.where(filter, x_1, y_1)
print(out)


# In[90]:


mat = np.random.rand(5,5)
mat


# In[91]:


np.where( mat > 0.5, 1000, -1)


# <p style="font-family: Arial; font-size:1.75em;color:#2462C0; font-style:bold"><br>
# 
# "any" or "all" conditionals:</p>

# In[92]:


arr_bools = np.array([ True, False, True, True, False ])


# In[93]:


arr_bools.any()


# In[94]:


arr_bools.all()


# <p style="font-family: Arial; font-size:1.75em;color:#2462C0; font-style:bold"><br>
# 
# Random Number Generation:
# </p>

# In[95]:


Y = np.random.normal(size = (1,5))[0]
print(Y)


# In[96]:


Z = np.random.randint(low=2,high=50,size=4)
print(Z)


# In[97]:


np.random.permutation(Z) #return a new ordering of elements in Z


# In[98]:


np.random.uniform(size=4) #uniform distribution


# In[99]:


np.random.normal(size=4) #normal distribution


# <p style="font-family: Arial; font-size:1.75em;color:#2462C0; font-style:bold"><br>
# 
# Merging data sets:
# </p>

# In[100]:


K = np.random.randint(low=2,high=50,size=(2,2))
print(K)

print()
M = np.random.randint(low=2,high=50,size=(2,2))
print(M)


# In[101]:


np.vstack((K,M))


# In[102]:


np.hstack((K,M))


# In[103]:


np.concatenate([K, M], axis = 0)


# In[104]:


np.concatenate([K, M.T], axis = 1)

