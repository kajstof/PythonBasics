import string
import sys

x = 1
if x == 1:
    # indented four spaces
    print("x is 1.")
    print("aaa")
else:
    print("ggg")
print("end")

for i in range(3, 10, 2):
    print(i)

for ch, n in zip(string.ascii_lowercase, range(20)):
    print("%s %d" % (ch, n))

x, y = 100, 120

print("%d, %d" % (x, y))

"%d, %d" % (x, y)

# print(f"{x}+{y}")


l = ["apples", "oranges", "pears"]

d = dict(zip(string.ascii_lowercase, l))

print("choose:")
for ch in sorted(d.keys()):
    print("%s] %s" % (ch, d[ch]))
    # print(f"{ch}] {d[ch]}")
    # print(f"{ch}] {d[ch]}")

# choice = input()[0]

# if choice in "qQ":
#     print("quit")
#     sys.exit(1)

# print(choice)

s = set([4, 3, 5, 4])

t = set([3,6])

print(s)
print(s.union(t))

print(s.symmetric_difference(t))

def f(x):
    return x ** 2

f = lambda x: x ** 2

print(list(map(lambda x: x ** 2, range(10))))