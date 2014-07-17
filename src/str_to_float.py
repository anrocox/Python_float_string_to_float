#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Jul 16, 2014

@author: anroco

How to convert a string to float in Python?

¿Cómo convertir un string a float en Python?
'''

#create a integer number
s = '273.92'
print(type(s))
print(s)

#convert using the float() function built-in python
f = float(s)
print(type(f))
print(f)

#create a string with a negative number
s = '-765.989'
print(s)

#convert to negative float the string 's'
f = float(s)
print(f)

#create a string with a number in exponential notation
s = '2.6323e-9'
print(s)

#convert to float the string 's'
f = float(s)
print(f)
