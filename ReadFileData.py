from math import floor

from numpy import long

massValues = open("mass.txt","r").readlines()

sumOfFuels = 0
for line in massValues:
    fuel = floor((long(line)/3)-2)
    sumOfFuels += fuel
    print(fuel)

print(sumOfFuels)
