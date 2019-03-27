# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 18:32:42 2019

@author: panji
"""

#merge sort
def mergeSort(A):
    n=len(A)
    if n<1 or n==1 :
        return A
    
    k=n//2
    A1=mergeSort(A[:k])
    A2=mergeSort(A[k:])
    p=0
    q=0
    results=[]
    while p<len(A1) and q<len(A2):
        if A1[p]<A2[q]:
            results.append(A1[p])
            p+=1
        else:
            results.append(A2[q])
            q=q+1
    if p==len(A1):
        results=results + A2[q:]
    if q==len(A2):
        results= results + A1[p:]
    return results

B=[0,1,2,3,4,5,6,7,8,9]
C=[9,6,7,3,4,7,9,1,2,0]
z=mergeSort(C)
print(z)
