textNum = {
  'one':1,
  'two':2,
  'three':3,
  'four':4,
  'five':5,
  'six':6,
  'seven':7,
  'eight':8,
  'nine':9
}

def getNumbers(line):


  line = (line.replace("one", "one1one")
    .replace("two", "two2two")
    .replace("three", "three3three")
    .replace("four", "four4four")
    .replace("five", "five5five")
    .replace("six", "six6six")
    .replace("seven", "seven7seven")
    .replace("eight", "eight8eight")
    .replace("nine", "nine9nine"))
  first = 0
  last = 0
  for letter in line:
    if letter not in "0123456789":
      continue
    first = letter
    break
  
  for letter in reversed(line):
    if letter not in "0123456789":
      continue
    last = letter
    break


  return int(first+last)


f = open("pieni.txt", "r")
f = open("input.txt", "r")

sum = 0

for x in f:
  sum += getNumbers(x)
print(sum)