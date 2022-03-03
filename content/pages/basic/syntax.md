title: Basic Syntax
next_title: Iterables
next_url: %url:iterables%


This tutorial contains eight interactive mini exercises and one review exercise. Try to solve them all!


[TOC]


## Input and output

Programming is about communication between the user (or users) and the computer. Therefore, the computer needs to be able to communicate to you, that is, send *output*. And you need to be able to communicate to the computer, that is, provide *input*.


### print()

You can print a message to the *standard output* with the `print()` function. (`print()` accepts all the variable types that we will discuss below.)

```python
print('Hello world!')
print(10)
print(True)
print(None)
```

The *standard output* is the default output channel of your program. If you're using Python from a terminal, then whatever goes to the standard output appears in the terminal; if you're using Python from within Rapunzel or Spyder, then whatever goes to the standard output appears in the IPython console; if you're using Python from within a Jupyter Notebook, then whatever goes to the standard output appears in the notebook; an in the interactive mini exercises, whatever goes to the standard output appears below the exercise.

But you generally don't have to worry about this: Your output will appear where you expect it to appear.


<div class="exercise" id="exercise_print" markdown="1">
#### Mini exercise

Print "Learning Python is fun!" to the standard output. (Type your solution below and click Run to execute. Your solution is checked automatically.)

<textarea class="code"></textarea>
<div hidden class="solution_output">Learning Python is fun!</div>
</div>


### input()

You can read text from the standard input with the `input()` function. (This returns a `str` that you can assign to a variable, as we will discuss below.)

~~~ .python
user_input = input('>>> ')
print(user_input)
~~~

__Output:__

~~~ .bash
>>> Hello world!
Hello world!
~~~

The *standard input* is the default input channel of your program. If you're using Python in an interactive environment, such as this website, Rapunzel, Spyder, or a Jupyter Notebook, then the user is prompted to provide input whenever the program tries to read from the standard input.

Again, you generally don't have to worry about this: User input will be handled as you'd expect it to.

<div class="exercise" id="exercise_input" markdown="1">
#### Mini exercise

Ask the user for input. Print out the result. When running the code, enter 42 as input to solve the exercise.

<textarea class="code"></textarea>
<div hidden class="solution_output">42</div>
</div>


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
b = c = 2 # b = 2; c = 2
d, e = 3, 4 # d = 3; e = 4
```

It is good practice to use variable names that are descriptive but not too long. For example, if a variable contains someone's age, the name `age` is preferable to `a` or (even worse) `x`. Variable names should be lowercase with words optionally separated by underscores, `like_this`. (Naming conventions such as this are described in the [PEP8] style guideline.)

<div class="exercise" id="exercise_assignment" markdown="1">
#### Mini exercise
Assign the value 'python' to a variable with the name `my_favorite_language`.

<textarea class="code"></textarea>
<div hidden class="solution_validate">
try:
    correct = my_favorite_language.lower() == 'python'
except:
    correct = 0
</div>
</div>


## Constants

A *constant* is a computer-science term for a variable that has a fixed value. In Python, real constants don't exist, because you can always change a variable. However, to indicate that a variable should be treated *as if* it were a constant, you can capitalize its name, `LIKE_THIS`.


```python
# PI should be treated as a constant
PI = 3.14
```


## Common variable types


### bool: True or False

A `bool` (from *Boolean*) is a variable type with only two values: `True` or `False`. It is used for logical operations including, as you will see below, `if` statements. Many operations, such as `>`, `==`, and `!=`, result in a `bool`. There is also a special set of Boolean operations: `and`, `or`, and `not`


```python
print(4 > 3)
print(3 > 4)
print(3 == 4) # The equality operator is a double equals sign!
print(4 > 3 or 3 > 4)
print(4 > 3 and not 3 > 4)
```

<div class="exercise" id="exercise_bool" markdown="1">
#### Mini exercise

Read two numbers from the standard input. Check whether the two numbers are the same and print out the resulting `bool` value. When running the code, enter two identical numbers to solve the exercise.

<textarea class="code"></textarea>
<div hidden class="solution_output">True</div>
</div>


### str: text strings

Text strings (`str`) are indicated by putting text between single (`'`) or double (`"`) quotes. You can specify strings spanning multiple lines with triplets of single (`'''`) or double (`"""`) quotes:


```python
a_str = 'some text'
another_str = "some text"
a_multiline_str = '''Line 1
Line 2'''
another_multiline_str = """Line 1
Line 2"""
```

If you want to include quotes as characters in a string, you can 'escape' them using an `\` to indicate that the character is part of the string.

```python
an_escaped_str = 'You can escape \'quotes\' to make them part of the string'
```

You often want to print out a string of text with some values inserted into it, and there are several ways to do this. You can:

- Concatenate (`+`) strings.
- Use the `%` string-formatting operator, which trats the string as a template and inserts values into it.
- Use `str.format()`, which similarly treats the string as a template, and inserts values into it.
- Use *f-strings* (formatted string literals), which are prefixed with an `f`, and which allow you to embed variables directly in the string.


```python
name = 'Audrey Tautou'
print('My name is ' + name)
print('My name is %s' % name)
print('My name is {0}'.format(name))
print(f'My name is {name}')  # This is what we will use
```

In addition to `str.format()`, `str` objects support many more functions. For example, the `str.startswith()` function checks whether the first part of a `str` is equal to another `str`.

```python
print(another_str.startswith('some'))
```

For a complete list of `str` functions, see:

- <https://docs.python.org/3/library/stdtypes.html#string-methods>


<div class="exercise" id="exercise_str" markdown="1">
#### Mini exercise

The `str.lower()` function turns all letters of a string into lowercase. Take a string that contains uppercase letters (e.g. 'some UPPERCASE LETTERS'), turn it into lowercase, and assign the resulting string to a variable called `my_lowercase_str`.

<textarea class="code"></textarea>
<div hidden class="solution_validate">
try:
    correct = my_lowercase_str.islower()
except:
    correct = 0
</div>
</div>

### None: a special kind of nothing

`None` is a special kind of value that is a type of its own (`NoneType`). Its main function is to indicate that a value is missing. To check whether a value is `None`, the special `is` operator is often used (and considered more elegant) instead of the regular `==` comparison.

```python
age_depp = None
if age_depp is None:
    print('Johnny Depp is ageless')
```


### int and float: numbers

The two main numeric types are:

- `int` for integer numbers (without decimals)
- `float` for floating-point numbers (with decimals)

Python automatically determines whether a value is an `int` or a `float`.

```python
my_int = 7
my_first_float = 3.14
my_second_float = 7. # The decimal point indicates that this should be a float
```

You can perform [all standard mathematical operations](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex), such as `+` and `*`. You can determine the order in which operations should be evaluated with parentheses.

```python
mul_add = 2 * 3 + 4
add_mul = 2 * (3 + 4)

# Print out some information about the numbers
print('First multiply then add: {0}'.format(mul_add))
print('First add then multiply: {0}'.format(add_mul))
```

The `float` type has two special values:

- `nan` is *not a number* and is generally used to indicate missing data in numeric computation. It is conceptually similar to `None`, with two important differences: `nan` is the only value that is unequal to itself (whereas `None` is equal to itself), and `nan` can be used in mathematical operations (whereas `None` cannot).
-  `inf` is used to express infinite numbers. You will rarely encounter `inf`, unless you're doing specific kinds of mathematical computations.

<div class="exercise" id="exercise_power" markdown="1">
#### Mini exercise

The `**` operator is used for exponentiation (i.e. 3 raised to the power of 2 equals 9: `3 ** 2 == 9`). To get the square root of a number, you can raise the number to the power .5. Determine the square root of 9 and print it out.

<textarea class="code"></textarea>
<div hidden class="solution_output">3.0</div>
</div>


## Converting to float, int, or str

To convert a variable to a `float`, `int`, or `str`, you can use the corresponding `float()`, `int()`, and `str()` functions. A common use case is when you use `input()` to get a number from the user: `input()` returns a `str`, and you need to use `int()` or `float()` to convert the input to a number.

~~~python
age = input('How old are you? ')
age = int(age)
if age >= 18:
    print('You are 18 years or older')
else:
    print('You are younger than 18')
~~~

__Output:__

~~~bash
How old are you? 35
You are 18 years or older
~~~

Converting values to another type is dangerous! If you try to convert the value 'this is not a number' to an `int`, you will get an error message, a so-called `Exception`. We discuss how to deal with `Exception`s [later](%url:exceptions%)

```python
# should-raise
age = int('this is not a number')
```

If you're unsure what type a variable has, you can check with `type()`:

```python
int_like_str = '10'
var_type = type(int_like_str)
print('int_like_str is a {var_type}')
```

<div class="exercise" id="exercise_convert" markdown="1">
#### Mini exercise

Read two values from the standard input. Convert them to `float`, add them up, and print out the result. To solve the exercise, run the code and enter the numbers 1.5 and 2 so that the sum is 3.5.

<textarea class="code"></textarea>
<div hidden class="solution_output">3.5</div>
</div>

## If statements

An `if` statement is the most basic form of flow control. It allows you to check whether some condition is `True`, and if so do something. If the condition is `False`, either nothing is done (if there is no `else` block), or something `else` is done:

```python
# Without else
if 2 * 2 == 4:
    print('Two times to equals four')
# With else
if 1 * 1 == 2:
    print('This is not printed')
else:
    print('One times one does not equal two')
```

Here we also see an important aspect of Python syntax: colons and indentation. The `if` and `else` statements are followed by a colon (`:`). This indicates that a block of code will follow that is indented, typically by four spaces (as prescribed by [PEP8]) or a single tab. (But never mix different indentation styles in the same code!) The block ends when the indentation ends. Unlike many other programming languages, Python does not use curly braces or other ways to explicitly indicate the start and end of a block: blocks are defined entirely through indentation.


<div class="exercise" id="exercise_if" markdown="1">
#### Mini exercise

Ask the user to guess your age! Read a value from the standard input. Convert it to `int` and check whether it matches your current age. If so, print out 'You guessed correctly!' otherwise print out 'You guessed incorrectly!'. To solve the exercise, run the code and enter your current age.

<textarea class="code"></textarea>
<div hidden class="solution_output">You guessed correctly!</div>
</div>

## Review exercise

<div class='exercise no-progress' id='exercise_pythagoras' markdown=1>

### Pythagoras

%-- include: exercises/basic/syntax.md --%

This exercise is not checked automatically, because there are several possible solutions. Click [here](%url:syntax%-solution) to see one solution!

<textarea class="code height300"></textarea>

</div>

[PEP8]: PEP8)[https://www.python.org/dev/peps/pep-0008/
