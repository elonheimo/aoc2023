import re

f = open("pieni.txt", "r")
f = open("input.txt", "r")

sum = 0

def handle_game(row):
  throws = row.split(";")
  throws[0] = throws[0].split(':')[1]
  biggest = {
    "red":1,
    "green":1,
    "blue":1
  }
  for throw in throws:
    for color, limit in [
      ("red",12),
      ("green",13),
      ("blue",14)
    ]:
      finds = re.findall(f"\d*(?= {color})", throw)
      if len(finds) == 0:
        continue
      if biggest[color] < int(finds[0]):
        biggest[color] = int(finds[0])
  return biggest['red'] * biggest['green'] * biggest['blue']
      

games = {}
sum += 0
for row in f:
  game_id = row.split(":")[0].split(" ")[1]
  #if handle_game(row):
  #  print(row)
  #  sum += int(game_id)
  sum+=handle_game(row)
print(sum)