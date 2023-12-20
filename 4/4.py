import re

f = open("pieni.txt", "r")
f = open("input.txt", "r")

def handle_row(row):
  winning = row.split('|')[0].split(':')[1]
  played = row.split('|')[1]
  #print(f"w {winning} p {played}")
  winning = re.findall(r'\d+', winning)
  played = re.findall(r'\d+', played)
  points = 0
  for play in played:
    if play in winning:
      if points == 0:
        points+=1
      else:
        points*=2
  return points

sum = 0
for row in f:
  #print(handle_row(row))
  sum += handle_row(row)
print(sum)