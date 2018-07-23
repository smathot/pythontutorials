title: Basic Syntax: Exercises and Solutions
next_title: Syntax
next_url: %url:syntax%


## Pythagoras

### Exercise

%-- include: exercises/basic/syntax.md --%


### Solution

~~~ .python
PI = 3.14

a = input('Length of a? ')
b = input('Length of b? ')
a = float(a)
b = float(b)
c = (a ** 2 + b ** 2) ** .5
print('C has length {0}'.format(c))
if c > PI:
  print('And this is longer than PI')
~~~

__Output:__

~~~
Length of a? 1
Length of b? 2
C has length 2.23606797749979
~~~
