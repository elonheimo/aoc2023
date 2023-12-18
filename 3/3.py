import re

f = open("pieni.txt", "r")
f = open("input.txt", "r")

def part_num_sum(prev, curr, next):
  part_numbers = [0]
  start = 0
  while True:
    if start >= len(curr): break
    res = re.search(r'\d+', curr[start:])
    if res == None: break
    span = (res.span()[0]+start,res.span()[1]+start)
    start = span[1]
    if span[0] == 0: 
      span = (1,span[1])
    if span[1] == len(curr): 
      span = (span[0],span[1]-1)
    if len(
      re.findall(r"[=&%*#$@/+-]",
                 f"{prev[span[0]-1:span[1]+1]}{curr[span[0]-1:span[1]+1]}{next[span[0]-1:span[1]+1]}")
                 ) > 0:
      part_numbers.append(int(res.group()))
  print(part_numbers)
  return sum(part_numbers)

res_sum = 0
f = f.readlines()
for row_i in range(len(f)):
  
  if row_i == 0:
    res_sum += part_num_sum(
      "",
      f[row_i],
      f[row_i+1] 
      )
  elif row_i == len(f)-1:
    res_sum += part_num_sum(
      f[row_i-1],
      f[row_i],
      "" 
      )
  else:
    res_sum += part_num_sum(
      f[row_i-1],
      f[row_i],
      f[row_i+1],
      )
print(res_sum)