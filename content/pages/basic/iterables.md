title: Iterables: list, dict, tuple, and set
next_title: Loops
next_url: %url:loops%


[TOC]


## Iterables, order, and mutability

In Python, an *iterable* object (or simply an *iterable*) is a collection of elements that you can loop (or *iterate*) through one element at a time. Simply put, an iterable is a list-like object. There are many kinds of iterables, which differ in many ways, including whether they are ordered and mutable:

- An iterable is *ordered* if you can retrieve its elements in a *predictable order*
- An iterable is *mutable* if you can change which elements it contains

Python has four built-in iterable types: `list`, `dict`, `tuple`, and `set`


## list: an ordered, mutable collection of elements

A `list` consists of zero or more other elements in a fixed order. The elements of a `list` can be anything, such a numbers (`int`), strings (`str`), and even other `list`s. Different elements from the same `list` can have different types.

A `list` is defined as a comma-separated list of values between square brackets:


```python
prime_numbers = [1, 3, 5, 7, 11]
print(prime_numbers)
```


### Getting a single element (indexing)

To get a single element from a `list`, use the *index* (position) of the element, where `0` is the first element, `1` is the second element, etc. That is, Python uses [zero-based indexing](https://en.wikipedia.org/wiki/Zero-based_numbering). You can also count from the end of the `list` by using a negative index, where `-1` is the last element, `-2`, is the second-to-last element, etc.


```python
print('Prime at index 0: {0}'.format(prime_numbers[0]))
print('Prime at index 1: {0}'.format(prime_numbers[1]))
print('Prime at index -4: {0}'.format(prime_numbers[-4]))
```


### Getting a range of elements (slicing)

You can also get multiple elements from a `list` by specifying a *slice*.


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

A common way to create a copy of a list to get the *full slice*. (This is equivalent to `list.copy()` in Python 3.)

```python
my_copy = prime_numbers[:]
```


### len(): counting the number of elements

`len()` counts how many elements there are in a `list`, or more generally in any iterable that has a length. (Some special iterables have no length, for example because they correspond to an infinite series. However, all iterables that we consider here have a length.)


```python
n = len(prime_numbers)
print('We have defined {0} prime numbers'.format(n))
```


### in: checking whether an iterable contains an element

Python has a special operator, `in`, to check whether an element is part of a `list` or another iterable.


```python
if 3 in prime_numbers:
    print('Three is prime')
```


### Modifying a list

A `list` has several common functions for adding or removing elements:

- `list.append(element)` adds an element to the end
- `list.insert(index, element)` inserts an element at position `index`
- `element = list.pop()` removes the last element from the list and returns it


```python
prime_numbers = []
prime_numbers.append(1)
prime_numbers.append(3) # Etc.
print(prime_numbers)
```


For an overview of `list` functions, see:

- <https://docs.python.org/3.6/tutorial/datastructures.html#more-on-lists>



## dict: an unordered, mutable collection of key-value pairs

A `dict` consists of zero or more key-value pairs. That is, each element of a `dict` is a combination of a value that serves as a key and that is associated with another value. A `dict` is *unordered*, which means that if you iterate through the elements of a `dict`, you are not guaranteed to get the elements in a particular order. So never rely on the order of a `dict`!

A `dict` supports `len()` and `in`, as described above for `list`s. However, indexing a `dict` works differently from a `list`, as discussed below, and slicing is not supported.

A `dict` is defined as a comma-separated list of key : value mappings between curly braces.


```python
ages = {
    'Jay-Z': 47,
    'Emanuel Macron': 40
}

print(ages)
```


### Getting a single element (indexing)

If you want to get an elements from a `dict`, you do this by specifying a `key`.


```python
print('Jay-Z is {0} years old'.format(ages['Jay-Z']))
```


Alternatively, you can use `dict.get()`, which allows you to specify a default value in case the key is not in the `dict`.


```python
print(
  'Johnny Depp is {0} years old'.format(
    ages.get('Johnny Depp', 'unknown')
  )
)
```


## tuple: an ordered, immutable collection of elements

The `tuple` is very similar to a `list`. The main difference between the two types is that a `tuple` is *immutable*, which means that a `tuple` cannot be changed after it has been defined; in other words, there are no functions such as `tuple.append()`, `tuple.pop()`, etc.

A `tuple` supports indexing, slicing, `len()` and `in`, as described above for `list`s.

A `tuple` is defined as a comma-separated list of values, optionally surrounded by parentheses.


```python
fibonacci = 1, 1, 2, 3, 5, 8
# Parentheses are optional unless they are required to avoid ambiguity
fibonacci = (1, 1, 2, 3, 5, 8)
```


## set: an unordered, immutable collection of unique elements

The `set` is a somewhat unusual type, which you will rarely use unless you're doing mathematical computations. A `set` corresponds to a mathematical set as specified in [set theory](https://en.wikipedia.org/wiki/Set_theory).

A `set` supports `len()` and `in`, as described above for `list`s. However, a `set` does not support indexing or slicing.

A `set` is defined as a comma-separated list of values surrounded by curly braces.

```python
vowels = {'a', 'e', 'i', 'o', 'u'}
```

A characteristic feature of `set`s is that each element can occur at most once (duplicates are ignored):

```python
print({'a', 'e'} == {'a', 'a', 'e', 'e'})
```

The `set` also supports standard operations from set theory:

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


## Exercises

<div class='info-box' markdown=1>

### Fibonacci

Define a `fibonacci` `list` that corresponds to the [Fibonacci series](https://en.wikipedia.org/wiki/Fibonacci_number) up to 8. Then, use slicing to create two subseries:

- `even_fibonacci`, with all numbers at even indices (0, 2, etc.); and
- `odd_fibonacci`, with all numbers at odd indices (1, 3, etc.).

</div>

<div class='info-box' markdown=1>

### Best-selling artists

Define an `artists` `dict` with the names of the [four best-selling music artists](https://en.wikipedia.org/wiki/List_of_best-selling_music_artists) as keys, and their claimed sales as values:

1. The Beatles with 600 million sales
2. Elvis Presley with 600 million sales
3. Michael Jackson with 350 million sales
4. Madonna with 300 million sales

Then ask the user to enter the name of an artist. Look up the number of sales of this artist, falling back to 'unknown' if the artists is not in the `dict`, and print out the result.

</div>
