# Task 2
s = int(input('Enter sum of x and y: '))
p = int(input('Enter product of numbers x and y: '))
x = 1
y = s - 1
while x <= s / 2:
    if x + y == s and x * y == p:
        print('x =', x)
        print('y =', y)
        break
    else:
        x += 1
        y -= 1
