from pprint import pprint
import re
from functools import reduce

f = open("pieni.txt", "r")
f = open("input.txt", "r")


f = f.readlines()

time = re.findall(r'\d+', f[0])
time = reduce(
  (lambda a,b : a+b),
  time
)
time = int(time)

distance = re.findall(r'\d+', f[1])
distance = reduce(
  (lambda a,b : a+b),
  distance
)
distance = int(distance)

def number_of_ways(time, distance):
  count = 0
  for speed in range(time):
    if speed * (time-speed) > distance:
      count += 1
  return count  
  
print(number_of_ways(time, distance))