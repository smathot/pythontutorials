"""
![](https://upload.wikimedia.org/wikipedia/commons/thumb/d/d2/Pythagorean.svg/390px-Pythagorean.svg.png)

Imagine a right triangle like the one above and:

- Read a number from the standard input and assign it to `a`
- Read another number from the standard input and assign it to `b`
- Use Pythagoras theorem to determine the value of the long side `c`
- Use string formatting to print out the length of the long side
- If `c` is larger than `PI` (a constant), also print out: *And this is longer than PI*
"""

PI = 3.14

a = input('Length of a? ')
b = input('Length of b? ')
a = float(a)
b = float(b)
c = (a ** 2 + b ** 2) ** .5
print('C has length {0}'.format(c))
if c > PI:
  print('And this is longer than PI')
