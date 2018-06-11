title: Basic Syntax
next_title: Iterables
next_url: %url:iterables%


[TOC]


## Input and output

### The standard input and output

Programming is about communication between the user (or users) and the computer. Therefore, the computer needs to be able to communicate to you, that is, send *output*. And you need to be able to communicate to the computer, that is, provide *input*.

The *standard output* is the default output channel of your program. If you're using Python from terminal, then whatever goes to the standard output will appear in the terminal; if you're using Python from within Spyder, then whatever goes to the standard output will appear in Spyder's IPython console; if you're using Python from within a Jupyter Notebook, then whatever goes to the standard output will appear in the notebook; etc. You generally don't have to worry about this: Your output will appear where you expect it to appear.

Similarly, *the standard input* is the default input channel of your program. If you're using Python in an interactive environment, such as Spyder or a Jupyter Notebook, the user will be prompted to provide input whenever the program tries to read from the standard input. Again, you generally don't have to worry about this: User input will be handled as you'd expect it to.


### print()

You can print a message to the standard output with the `print()` function. (This accepts any variable type.)

```python
print('Hello world!')
```

### input()

You can read text from the standard input with the `input()` function. (This returns a `str` variable, which we will discuss below.)

~~~ .python
user_input = input()
print('The user said: {0}'.format(user_input))
~~~


## Comments

A line that starts with a `#` is a *comment*. Comments only serve to document your code. It is good practice to comment code that is not self-explanatory. However, in many cases, well-written code is self-explanatory, and adding (too many) comments will only make it less clear.


```python
# This is a comment!
```


## Variable assignment

Python is *dynamically typed*, which means that you not need to explicitly indicate whether a variable is a number, a string, or something else. That doesn't mean that there are no variable types: There are, but the type of a variable is determined implicitly by the value that you assign (`=`) to it. (We will meet different variable types below.)


```python
a = 1
print(a)
```

You can also assign a single value to multiple variables in a single statement. And you can even assign multiple values to multiple variables in a single statement:


```python
b = c = 2
d, e = 3, 4
```

It is good practice to use variable names that are descriptive but not too long. For example, if a variable contains someone's age, the name `age` is preferable to `a` or (even worse) `x`. Variable names should be lowercase with words optionally separated by underscores, `like_this`. (Naming conventions such as this are described in the [PEP8] style guideline.)


## Constants

A *constant* is a computer-science term for a variable that has a fixed value. In Python, real constants don't exist, because you can always change a variable. However, to indicate that a variable should be treated *as if* it were a constant, you can capitalize its name, `LIKE_THIS`.


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
print(3 == 4) # The equality operator is a double equals sign!
print(4 > 3 or 3 > 4)
print(4 > 3 and not 3 > 4)
```


### `None`: a special kind of nothing

`None` is a special kind of value that is a type of its own (`NoneType`). Its main function is to indicate that a value is missing. To check whether a value is `None`, the special `is` operator is often used (and considered more elegant) instead of the regular `==` comparison.

```python
age_depp = None
print('Is Johnny Depp ageless? {0}'.format(age_depp is None))
```


### `str`: text strings

Text strings (`str`) are indicated by putting text between single (`'`) or double (`"`) quotes. You can specify strings spanning multiple lines with triplets of single (`'''`) or double (`"""`) quotes:


```python
a_str = 'some text'
another_str = "some text"
a_multiline_str = '''Line 1
Line 2'''
another_multiline_str = """Line 1
Line 2"""
```

You often want to print out a string of text with some values inserted into it. You can do this by concatenating (`+`) strings. Another and more elegant way is to use `str.format()`, which treats the string as a template, and inserts values into it.


```python
name = 'Audrey Tautou'
print('My name is ' + name)
print('My name is {0}'.format(name))
```

In addition to `str.format()`, `str` objects support many more functions. For example, the `str.startswith()` function checks whether the first part of a `str` is equal to another `str`.

```python
print(my_first_str.startswith('some'))
```

For a complete list of `str` functions, see:

- <https://docs.python.org/3/library/stdtypes.html#string-methods>


### `int` and `float`: numbers

The two main numeric types are:

- `int` for integer numbers (without decimals)
- `float` for floating-point numbers (with decimals)

Python automatically determines whether a value is an `int` or a `float`.

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

The `float` type has two special values:

- `nan` is *not a number* and is generally used to indicate missing data in numeric computation. It is conceptually similar to `None`, with one important difference: `nan` is the only value that is unequal to itself!
-  `inf` is used to express infinite numbers. You will rarely encounter `inf`, unless you're doing specific kinds of mathematical computations.


## Conditional (`if`) statements

An `if` statement is the most basic form of flow control. It allows you to check whether some condition is `True`, and if so do something. If the condition is `False`, either nothing is done (if there is no `else` block), or something `else` is done:

```python
if 2 * 2 == 4:
    print('Two times to equals four')

if 1 * 1 == 2:
    print('This is not printed')
else:
    print('One times one does not equal two')
```

Here we also see an important aspect of Python syntax: colons and indentation. The `if` and `else` statements are followed
by a colon (`:`). This indicates that a block of code will follow that is indented, typically by four spaces (as prescribed by [PEP8]) or a single tab. (But never mix different indentation styles in the same code!) The block ends when the indentation ends. Unlike many other programming languages, Python does not use curly braces or other ways to explicitly indicate the start and end of a block: blocks are defined entirely through indentation.


## Exercise: Pythagoras

![](https://upload.wikimedia.org/wikipedia/commons/thumb/d/d2/Pythagorean.svg/390px-Pythagorean.svg.png)

Imagine the above right triangle and:

- Assign the number `2` to the variable `a`
- Assign the number `4` to the variable `b`
- Use Pythagoras theorem to assign the correct value to `c`
- Use string formatting to print out: *The long side (c) has length 4.47213595499958*
- If `c` is larger than `PI` (a constant), also print out: *And this is longer than PI*


[PEP8]: PEP8)[https://www.python.org/dev/peps/pep-0008/
