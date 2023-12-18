import re
from itertools import chain

f = open("pieni.txt", "r")
f = open("input.txt", "r")

def part_num_sum(prev, curr, next, i):
  part_nums = []
  ret_sum = 0
  for i in range(len(curr)):
    if curr[i] != "*":
      continue
    part_nums = []
    allIter = chain(
      re.finditer(r'\d+', prev),
      re.finditer(r'\d+', curr),
      re.finditer(r'\d+', next),
    )
    for match in allIter:
      if match.span()[0]-1 <= i <= match.span()[1]:
        part_nums.append(int(match.group()))

    if len(part_nums) ==2:
      ret_sum += part_nums[0]*part_nums[1]

  return ret_sum

res_sum = 0
f = f.readlines()
for row_i in range(len(f)):
  
  if row_i == 0:
    res_sum += part_num_sum(
      "",
      f[row_i],
      f[row_i+1],
      row_i
      )
  elif row_i == len(f)-1:
    res_sum += part_num_sum(
      f[row_i-1],
      f[row_i],
      "",
      row_i
      )
  else:
    res_sum += part_num_sum(
      f[row_i-1],
      f[row_i],
      f[row_i+1],
      row_i
      )
print(res_sum)