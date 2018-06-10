title: Iterables: list, dict, tuple, and set


[TOC]


## Iterables, order, and mutability

In Python, an *iterable* object is a collection of elements that you can loop (or *iterate*) through one element at a time. There are many kinds of iterable objects, and they differ in many ways, including in order and mutability:

- An iterable object is *ordered* if you can retrieve its elements in a *predictable order*
- An iterable object is *mutable* if you can change which elements it contains

Python has four built-in iterable types: `list`, `dict`, `tuple`, and `set`


## `list`: an ordered, mutable collection of elements

A Python `list` is a variable type that consists of zero or more other elements in a fixed order. The elements of a list can be anything, such a numbers (`int`), strings (`str`), and other types, and different elements can have different types.

A `list` is defined as a comma-separated list of values between square brackets:


```python
prime_numbers = [1, 3, 5, 7, 11]
print(prime_numbers)
```

<div class='info-box' markdown=1>
__Exercise__

Define a `list` that contains your first and last name as separate elements, and print it out.
</div>


### Getting elements from a list

If you want to get a single element from a list, you use the index of the element, where `0` is the first element, `1` is the second element, etc. You can also count from the end of the `list` by using a negative index, where `-1` is the last element, `-2`, is the second-to-last element, etc.


```python
print('Prime at index 0: {0}'.format(prime_numbers[0]))
print('Prime at index 1: {0}'.format(prime_numbers[1]))
print('Prime at index -4: {0}'.format(prime_numbers[-4]))
```

<div class='info-box' markdown=1>
__Exercise__

Define a list of odd numbers between 0 and 10, and print out the second highest odd number.
</div>


### Slicing a range of elements from a list

You can also get multiple elements from a `list` by specifying a slice. This looks like this:


```python
from_index = 0
to_index = 6 # Non-inclusive, so until and including 4 (but not 5)!
in_steps_of = 3
print(prime_numbers[from_index:to_index:in_steps_of])
```

All the parts of a slice are optional, and fall back to the start of the list (for `from_index`), the end of the list (for `to_index`), and steps of 1. So you can get the first two prime numbers by only specifying the `to_index`, like this:


```python
print(prime_numbers[:2])
```

<div class='info-box' markdown=1
__Exercise__

From the `list` of odd numbers, use a slice to get a list with only the values 3 and 9.
</div>


### Counting the number of elements in a list with `len()`

The Python built-in function `len()` counts how many elements there are in a `list`, or more generally in an iterable object (it also gives the number of characters in a `str`).


```python
n = len(prime_numbers)
print('We have defined {0} prime numbers'.format(n))
```

<div class='info-box' markdown=1>
__Exercise__

Use `len()` to count how many odd numbers there are between 0 and 10, and print out the result.
</div>


### Checking whether a `list` contains an element with `in`

Python has a special operator, `in`, to check whether an element is part of a `list` (or another iterable object).


```python
if 3 in prime_numbers:
    print('Three is prime')
```


### Modifying a list

A `list` object has a few common functions for adding or removing elements:

- `list.append(element)` adds an element to the end
- `list.insert(index, element)` inserts an element at position `index`
- `element = list.pop()` removes the last element from the list and returns it

However, a `list` object has many more functions, which are documented here:

- <https://docs.python.org/3.6/tutorial/datastructures.html#more-on-lists>

An alternative (but inconvenient) way to create a list of prime numbers is:


```python
prime_numbers = []
prime_numbers.append(1)
prime_numbers.append(3) # Etc.
print(prime_numbers)
```

<div class='info-box' markdown=1>
__Exercise__

Use `list.pop()` to remove `9` from the `list` of odd numbers, assign it to a new variable, and print it out.
</div>


## `dict`: an unordered, mutable collection of key-value pairs

A `dict` is a variable type that consists of zero or more key-value pairs. That is, each element of a `dict` is a combination of a value that serves as a key, and that is associated with another value. A `dict` is *unordered*, which means that if you loop through the elements of a `dict`, you are not guaranteed to get the elements in a particular order.

A `dict` is defined as a comma-separated list of key : value mappings between curly braces.


```python
people_with_ages = {
    'Jay-Z' : 47,
    'Emanuel Macron' : 40
}

print(people_with_ages)
```

<div class='info-box' markdown=1>
__Exercise__

Define a `dict` that maps your first name (the key) onto your last name (the value).
</div>


### Getting values from a `dict`

If you want to get an elements from a `dict`, you do this by specifying a `key`.


```python
print('Jay-Z is {0} years old'.format(people_with_ages['Jay-Z']))
```


## `tuple`: an ordered, immutable collection of elements

The `tuple` is very similar to a `list`. The main difference between the two types is that a `tuple` is *immutable*, which means that it cannot be changed after it has been defined; in other words, there are no functions such as `tuple.append()`, `tuple.pop()`, etc.

A `tuple` is defined as a comma-separated list of values, optionally surrounded by parentheses.


```python
fibonacci = 1, 1, 2, 3, 5, 8
# Parentheses are optional unless they are required to avoid ambiguity
fibonacci = (1, 1, 2, 3, 5, 8)
```


## `set`: an unordered, immutable collection of unique elements

The `set` is a somewhat unusual type, which you will not often use unless you're doing specific kinds of mathematical computations. The `set` corresponds to a mathematical set, following the rules of [set theory](https://en.wikipedia.org/wiki/Set_theory).


A `set` is defined as a comma-separated list of values surrounded by curly braces.

```python
vowels = {'a', 'e', 'i', 'o', 'u'}
```

A characteristic feature of `set`s is that each element can occur at most once.

```python
print({'a', 'e'} == {'a', 'a', 'e', 'e'})
```

The `set` also supports standard operations, including:

- The union (`|`) of two sets contains all elements that occur in either or both of the sets
- The intersection (`&`) of two sets contains all elements that occur in both sets

```python
vowels_1 = {'a', 'e', 'i'}
vowels_2 = {'i', 'o', 'u'}
print('Union: {0}'.format(vowels_1 | vowels_2))
print('Intersection: {0}'.format(vowels_1 & vowels_2))
```

For more information, see:

- <https://docs.python.org/3.6/library/stdtypes.html?highlight=set#set>
