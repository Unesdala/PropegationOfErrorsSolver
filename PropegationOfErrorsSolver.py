# Rhayven Nite
# 9/6/2018
#
# This program works to solve propegation of errors in equations using input
# From the end user as variables.
#
#
# Thanks to @JulianaTh for helping with the equations

import math

x = float(input("Please enter the X variable: "))
y = float(input("Please enter the Y variable: "))
errX = float(input("Please enter the X Error Variable: "))
errY = float(input("Please enter the Y Error Variable: "))

total_error1 = x*y
total_error2 = ((x*errY) + (y*errX))
final_error = str(total_error1) + " +- " + str(total_error2)

print("Final Result:" + " +- " + final_error)
