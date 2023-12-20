import re

f = open("pieni.txt", "r")
f = open("input.txt", "r")



f = f.readlines()
card_count = [1]*len(f)

def handle_row(row_i):
  row = f[row_i]
  winning = row.split('|')[0].split(':')[1]
  played = row.split('|')[1]
  #print(f"w {winning} p {played}")
  winning = re.findall(r'\d+', winning)
  played = re.findall(r'\d+', played)
  count = 0
  for play in played:
    if play in winning:
      count +=1
  for i in range(1,count+1):
    card_count[row_i + i] += card_count[row_i]

for row_i in range(len(f)):
  #print(handle_row(row))
  print(card_count)
  handle_row(row_i)
print(sum(card_count))