# -*- coding: utf-8 -*-
"""leap_year.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1alePV3-fIRrAVuT0zt3hA9mssC78Myhf
"""

def is_leap(year):
    leap = False
    
    # Write your logic here
    if (year%4==0):
        leap= True
    if (year%100==0):
        leap= False
    if(year%400==0):
        leap= True
    
    return leap

year = int(raw_input())
print is_leap(year)