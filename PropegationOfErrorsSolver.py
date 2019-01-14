# Rhayven Nite
# 9/6/2018
#
# This program works to solve propegation of errors in equations using input
# From the end user as variables.
#
# Currently, it solves Multiplication based Propegation of Errors.
# 
# Formulas Used:
#
# Multiplication: (x*y) + (x*error Y) + (Y * error X)
# 
# Thanks to @JulianaTh for helping with the equations

import math

x = float(input("Please enter the X variable: "))
y = float(input("Please enter the Y variable: "))
errX = float(input("Please enter the X Error Variable: "))
errY = float(input("Please enter the Y Error Variable: "))

product = x*y

multiplication_error = ((x*errY) + (y*errX))

multiplication_total = str(product) + " +- " + str(multiplication_error)

print("Final Result: " + multiplication_total)
