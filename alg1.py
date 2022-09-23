# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 20:11:17 2022

@author: lidon
"""
import numpy as np
import time

# Algorithm Implementation from Practical Guide to Quant Review

# swap 2 values without additional storage
def swap(i,j):
    i=i+j
    j=i-j
    i=i-j
    return i,j

# x is a sorted list
# find unique elements in x
def unique_elements(x):
    elements=[x[0]]
    for i in range(1,len(x)):
        if x[i]!=x[i-1]:
            elements.append(x[i])
    
    return elements

# Horner algorithm to calculate a0 +a1x+...+an x^n
# a=[a0,a1,...,an], x variable
def Horner(a,x):
    deg=len(a)-1
    output=a[deg]*x+a[deg-1]
    for i in range(1,deg):
        output=output*x+a[deg-1-i]
    return output

# sort x from small to big
# bubble sort
def bubble_sort(x):
    for i in range(0,len(x)):
        for j in range(0,len(x)-i-1):
            if x[j]>x[j+1]:
                x[j],x[j+1]=swap(x[j],x[j+1])
    return x

# quick sort
def quick_sort(x):
    if len(x)==1:
        return x
    a=x[0]
    x1=[]
    x2=[]
    for i in range(0,len(x)):
        if x[i]<=a:
            x1.append(x[i])
        else:
            x2.append(x[i])
    return quick_sort(x1)+quick_sort(x2)

# merge 2 sorted lists
def merge(a,b):
    if a==[] or b==[]:
        return a+b
    else:
        if a[0]<b[0]:
            return [a[0]]+merge(a[1:],b[0:])
        elif a[0]>=b[0]:
            return [b[0]]+merge(a[0:],b[1:])


# merge sort
def merge_sort(x):
    if len(x)==1:
        return x
    if len(x)==2:
        return [min(x),max(x)]
    else:
        low=0
        high=len(x)
        mid=int((low+high)/2)
        return merge(merge_sort(x[low:mid]),merge_sort(x[mid:high]))
    
# Knuth Shuffle
# x is a list, generate a random shuffle of x in O(n)
def Knuth_shuffle(x):
    for i in range(0,len(x)):
        index=np.random.randint(i,len(x),1)[0]
        x[i],x[index]=swap(x[i],x[index])
    return x


# calculate n-th element in Fibonnaci using recursion
# the most inefficient way
def Fibonnaci1(n):
    if n==1:
        return 1
    if n==2:
        return 1
    else:
        return Fibonnaci1(n-1)+Fibonnaci1(n-2)

# calculate n-th element in Fibonnaci by direct computing
# has time complexity O(n)
def Fibonnaci2(n):
    if n==1:
        return 1
    if n==2:
        return 1
    else:
        series=[1,1]
        for i in range(2,n):
            series.append(series[i-1]+series[i-2])
        return series[len(series)-1]
            
# find the maximum of summation of any contiguity array
def max_subarray(x):
    T=x[0]
    V_max=T
    T_min=min(0,T)
    for i in range(1,len(x)):
        T=T+x[i]
        if V_max<=T-T_min:
            V_max=T-T_min
        if T<T_min:
            T_min=T
    return V_max

# find square root of n with acc e
def square_root(n,e):
    # initial point
    x=n
    new_x=x-(x**2-n)/(2*x)
    
    while abs(new_x-x)>e:
        x=new_x
        new_x=x-(x**2-n)/(2*x)
    return new_x
            
    