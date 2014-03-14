#!/usr/bin/env python

def function(x=0,y=0,z=0):
  print "x = " + str(x) + ",y = " + str(y) + ", z= " + str(z)

print "Enter a the name of a file containing a,b,n numbers: ",
filename = raw_input()

array = []
with open(filename, "r") as f:
  for line in f:
    array.append(line)
    numbers_str = line.split()
    #convert numbers to floats
    numbers_int = [int(x) for x in numbers_str]
    function(numbers_int[0],numbers_int[1],numbers_int[2])
