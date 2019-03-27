# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 19:13:28 2019

@author: panji
"""

class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        odd=[]
        even=[]
        for i in range(len(A)):
            if A[i]%2==0:
                even.append(A[i])
            else:
                odd.append(A[i])
        return even+odd

A=[1,3,2,4]
f=Solution()
print(f.sortArrayByParity(A))