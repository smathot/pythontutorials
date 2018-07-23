title: Exceptions: Exercises and Solutions
next_title: Exceptions
next_url: %url:exceptions%


## An interactive calculator

### Exercise

%-- include: exercises/basic/exceptions.md --%


### Solution

~~~ .python
class FormulaError(Exception): pass


def parse_input(user_input):

  input_list = user_input.split()
  if len(input_list) != 3:
    raise FormulaError('Input does not consist of three elements')
  n1, op, n2 = input_list
  try:
    n1 = float(n1)
    n2 = float(n2)
  except ValueError:
    raise FormulaError('The first and third input value must be numbers')
  return n1, op, n2


def calculate(n1, op, n2):

  if op == '+':
    return n1 + n2
  if op == '-':
    return n1 - n2
  if op == '*':
    return n1 * n2
  if op == '/':
    return n1 / n2
  raise FormulaError('{0} is not a valid operator'.format(op))


while True:
  user_input = input('>>> ')
  if user_input == 'quit':
    break
  n1, op, n2 = parse_input(user_input)
  result = calculate(n1, op, n2)
  print(result)
~~~

__Output:__

~~~
>>> 1 + 1
2.0
>>> 3.2 - 1.5
1.7000000000000002
>>> quit
~~~
