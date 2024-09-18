import sys
sys.setrecursionlimit(15000)


def ddml(n):
  n = int(n)
  if n > 0:
    n = (n * 5) + ddml(n - 1)
  return n

print(f"On turn {sys.argv[1]}, Doug Doug will pay: {ddml(sys.argv[1])}")
