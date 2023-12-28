from pprint import pprint
import re

f = open("pieni.txt", "r")
f = open("input.txt", "r")


f = f.readlines()

time = re.findall(r'\d+', f[0])
time = [int(x) for x in time]

distance = re.findall(r'\d+', f[1])
distance = [int(x) for x in distance]

def number_of_ways(time, distance):
  count = 0
  for speed in range(time):
    if speed * (time-speed) > distance:
      count += 1
  return count  
  
mul_sum = 1

for i in range(len(distance)):
  print(number_of_ways(time[i], distance[i]))
  mul_sum *= number_of_ways(time[i], distance[i])

print(mul_sum)