
class A:
  def __init__(self, v):
    self.v = v
v = 0
a = A(v)

for i in range(0, 5):
  a.v += 5
  print(a.v)
