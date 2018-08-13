from collections import deque

d = deque()
d.append(1)
print(d)

d.appendleft(2)
print (d)

d.clear()
print (d)

d.extend('1')
print(d)

d.extendleft('234')
print(d)

d.count('1')

d.pop()

print(d)

d.popleft()
print(d)

d.extend('6789')
print(d)

d.remove('2')
print(d)

d.reverse()
print(d)

d.rotate(3)
print(d)

for _ in range(int(input())):
    command, *args = input().split()
    getattr(d, command)(*map(int, args))
print(*d)
