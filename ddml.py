import sys
sys.setrecursionlimit(5000)


def ddml(turn_number):
  turn_number = int(turn_number)
  output = 0
  if turn_number == 0:
    output = turn_number
  elif turn_number == 1:
    output = (turn_number * 5)
  else:
    output = (turn_number * 5) + ddml(turn_number - 1)
  return int(output)

print(f"On turn {sys.argv[1]}, Doug Doug will pay: {ddml(sys.argv[1])}")
