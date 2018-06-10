title: Basic Syntax

[TOC]


## Input and Output

Let's start at the very beginning: by printing a message to the output using the `print()` function. You can do this by executing the following:

```python
print('Hello world!')
```

One way (of many) to get text input from the user is with the `input()` function. This will return a `str` variable, which we will discuss below.

~~~ .python
user_input = input()
print('The user said: {0}'.format(user_input))
~~~


## Comments

A line that starts with a `#` is a *comment*. Comments do nothing, but serve to document your code. It is good practice to comment code that is not self-explanatory.


```python
# This is a comment!
```


## Variable assignment

Python is *dynamically typed*, which means that you not need to explicitly indicate whether a variable will contain a number, a string, or something else. The variable's type is determined implicitly by the value that you assign to it. (We will meet different variable types below.)


```python
the_most_random_number = 7
print(the_most_random_number)
```

You can also assign a single value to multiple variables in a single statement:


```python
# Equivalent to:
# a = 1
# b = 1
a = b = 1
```

And even assign multiple values to multiple variables in a single statement:


```python
# Equivalent to:
# a = 1
# b = 2
a, b = 1, 2
```


## Constants

A *constant* is a computer-science term for a variable that has a fixed value. In Python, real constants don't exist, because you can always change a variable. However, to indicate that a variable should be treated *as if* it were a constant, you can `CAPITALIZE_ITS_NAME`. Naming conventions such as this are described in the [PEP8] style guideline.


```python
# PI should be treated as a constant
PI = 3.14
```


## Common variable types


### `bool`: True or False

A `bool` (from *boolean*) is a variable type with only two values: `True` or `False`. It is used for logical operations including, as you will see below, `if` statements. Many operations, such as `>`, `==`, and `!=`, result in a `bool`. There is also a special set of boolean operations: `and`, `or`, and `not`


```python
print(4 > 3)
print(3 > 4)
print(3 == 4)
print(4 > 3 or 3 > 4)
print(4 > 3 and not 3 > 4)
```

<div class='info-box' markdown=1>
__Exercise!__

Verify that `PI` is neither smaller than 3 nor larger than 4, and print out the resulting `bool`.
</div>


### `None`: a special kind of nothing

`None` is a special kind of value that is a type of its own (`NoneType`). Its main function is to indicate that a value is missing. To check whether a value is `None`, the special `is` operator is often used (and considered more elegant), instead of the regular `==` comparison.

```python
age_of_johnny_depp = None
print('Is Johnny Depp ageless? {0}'.format(age_of_johnny_depp is None))
```


### `str`: text strings

Text strings (`str`) are indicated by putting text between single (`'`) or double (`"`) quotes. You can specify strings spanning multiple lines with triplets of single (`'''`) or double (`"""`) quotes:


```python
my_first_str = 'some text'
my_second_str = "some text"
my_first_multiline_str = '''Line 1
Line 2'''
my_second_multiline_str = """Line 1
Line 2"""
```

You often want to print out a string of text with some values inserted into it. You can do this by concatening (`+`) strings. Another and more elegant way is to use `str.format()`, which treats the string as a template, and inserts values into it.


```python
name = 'Sebastiaan'
print('My name is ' + name)
print('My name is {0}'.format(name))
```

In addition to `str.format()`, `str` objects support many more functions. For example, the `str.startswith()` function checks whether the first part of a `str` is equal to another `str`.

```python
print(my_first_str.startswith('some'))
```

For a complete list of `str` functions, see:

- <https://docs.python.org/3/library/stdtypes.html#string-methods>

<div class='info-box' markdown=1>
__Exercise__

Use string formatting to print out: *Side c of the right triangle is of length 4.47213595499958*
</div>


### `int` and `float`: numbers

The two main numeric types are:

- `int` for integer numbers (without decimals)
- `float` for floating-point numbers (with decimals)

Python automatically determines whether something is an `int` or a `float`.

```python
my_int = 7
my_first_float = 3.14
my_second_float = 7. # The decimal point indicates that this should be a float

# Print out some information about the numbers
print('my_int is {0} and has type {1}'.format(my_int, type(my_int)))
print('my_first_float is {0} and has type {1}'.format(my_first_float, type(my_first_float)))
print('my_second_float is {0} and has type {1}'.format(my_second_float, type(my_second_float)))
```

You can perform [all standard mathematical operations](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex), such as `+` and `*`. You can determine the order in which operations should be evaluated with parentheses.

```python
first_multiply_then_add = 2 * 3 + 4
first_add_then_multiply = 2 * (3 + 4)

# Print out some information about the numbers
print('first_multiply_then_add is {0}'.format(first_multiply_then_add))
print('first_add_then_multiply is {0}'.format(first_add_then_multiply))
```

The `float` type also supports two special values:

- `nan` is *not a number* and is generally used to indicate missing data in numeric computation. It is conceptually similar to `None`, with one important difference: `nan` is the only value that is unequal to itself!
-  `inf` is used to express infinite numbers. You will rarely encounter `inf`, unless you're doing specific kinds of mathematical computations.

<div class='info-box' markdown=1>
__Exercise__

![](https://upload.wikimedia.org/wikipedia/commons/thumb/d/d2/Pythagorean.svg/390px-Pythagorean.svg.png)

Imagine the above right triangle and:


- Assign the number `2` to the variable `a`
- Assign the number `4` to the variable `b`
- Use Pythagoras to assign the correct value to `c`
- Print out `c`
</div>


## Conditional (`if`) statements

An `if` statement is the most basic form of flow control: it allows you to check whether some condition is met, and if so do something.

```python
if 2 * 2 == 4:
    print('Two times to equals four')
```

If the condition is not met, either nothing is done, or something `else` is done:

```python
if 1 * 1 == 2:
    print('This is not printed')
else:
    print('One times one does not equal two')
```

Here we also see an important aspect of Python syntax: colons and indentation. The `if` and `else` statements are followed
by a colon (`:`). This indicates that a block of code will follow that is indented, typically by four spaces (as prescribed by [PEP8]) or a single tab. (But never mix different indentation styles in the same code!) This block ends when the indentation ends. Unlike many other programming languages, Python does not use curly braces or other ways of explicitly indicating the start and end of a block: this is done through indentation.

<div class='info-box' markdown=1>
__Exercise__

Check if side `c` of the right triangle is larger or smaller than `4`, and print a message out to indicate the result (eg. 'c is larger than 4' or 'c is smaller than 4').
</div>


[PEP8]: PEP8)[https://www.python.org/dev/peps/pep-0008/
