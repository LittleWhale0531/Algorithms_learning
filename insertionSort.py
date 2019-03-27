# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 18:14:14 2019

@author: panji
"""

#插入排序
def insertionSort(A):
    for j in range(1,len(A)):
        key=A[j]
        i=j-1
        while i>=0 and A[i]>key:
            A[i+1]=A[i]
            i=i-1
        if A[i+1]>key:
            A[i+1]=key
    
    return A

D=[0,1,2,3,4,5,6]
B=[9,7,8,6,5,4,3]

insertionSort(B)
print(B)

    