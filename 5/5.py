from pprint import pprint
import re

f = open("pieni.txt", "r")
f = open("input.txt", "r")

def range_list(rows):
  i = 0
  res = [[]]
  while i < len(rows):
    nums = re.findall(r'\d+', rows[i])
    nums = [int(num) for num in nums]

    if len(nums) < 3:
      i+=2
      res.append([])
      continue
    res[len(res) -1].append(nums)
    i+=1
  return res


f = f.readlines()
seeds = re.findall(r'\d+', f[0])
seeds = [int(seed) for seed in seeds]
ranges = range_list(f[3:])
pprint(ranges)
def final_seed_value(seed):
  seed_value = seed
  for count, range_set in enumerate(ranges):
    for _range in range_set:
      dest, source, length = _range
      if source <= seed_value < source + length:
        print("old", seed_value, '_'*count)
        seed_value = dest + (seed_value - source)
        print("new", seed_value," "* 10,f'source {source}, dest {dest}, len {length}')
        break
  return seed_value

computed_seeds = []
for seed in seeds:
  
  computed_seeds.append(
    final_seed_value(seed)
  )
  print('----------')

pprint(computed_seeds)
print( min(computed_seeds))

