title: NumPy
next_title: DataMatrix
next_url: %url:datamatrix%


[TOC]


## What is NumPy?

[NumPy](https://numpy.org/) is a Python library built around the concept of arrays, which are collections of elements. The elements of a NumPy array are usually (but not necessarily) numbers, and NumPy allows you to perform calculations with those numbers.

Everything that you can do with NumPy, you can also do with built-in Python objects (notably `list`s, see [iterables](%url:iterables%)). But NumPy is *much* faster and, in many cases, more elegant.

NumPy is not part of the Python standard library. However, it is such a widely used library that it is pre-installed in most Python environments.


## Arrays


### Dimensions

NumPy arrays are called `ndarray` objects. The `nd` stands for "N-dimensional", which is indicates that an array can have any numbers of dimensions. A 1D array is like a `list`, because you need only a single coordinate (or index) to indicate an element. A 2D array is like a spreadsheet, because you need two coordinates (a row and a column, or an X and a Y coordinate) to indicate an element. Higher-dimensional arrays are also possible, although arrays of more than three dimensions are difficult to mentally picture. (But this is a limitation of your brain, not of NumPy!)

A real-life example of a 5D array might be an fMRI dataset (a brain scan) of multiple participants. Here, the first three dimensions would be space (X, Y, Z), because a brain is a 3D object. The fourth dimension would time, because an fMRI scan measures brain activity over time. And the fifth dimension would be the participant, because there are multiple participants. Therefore, you need five numbers to identify an element in this dataset (X, Y, Z, time, participant number).


### Data types

A NumPy array has a single data type (its `dtype`), and all elements in the array are of that type. This is different from a `list` object, which can contain elements of different types. The most common data types for NumPy arrays are `bool`, `int`, `float`, and `str`.


## Creating an array

First, we're going to import `numpy` with the alias `np` (see [modules](%url:modules%)). The `np` alias is by convention, and has the advantage that it requires less typing than `numpy`.

```python
import numpy as np
```

You can create an array directly from a `list`. If you pass a `list` of `list`s, as in the example below, the array will become 2D; you can tell this from the shape property, which returns the size of each dimension. The length of an array is the size of the first dimension. The `dtype` of the array will also be automatically determined, unless you explicitly specify this with the `dtype` keyword. In this case, it's an `int` array (or `int64`, ).

```python
a = np.array([[1, 2, 3], [4, 5, 6]])
print(a)
print('dtype: {}'.format(a.dtype))
print('shape: {}'.format(a.shape))
print('length: {}'.format(len(a)))
```

If you want an array of only zeros, you can use `np.zeros()`. If you want an array of only ones, you can use `np.ones()`. The only required argument is the desired shape.

```python
print('zeros:')
print(np.zeros((2, 3)))
print('ones:')
print(np.ones((2, 3)))
```

The NumPy equivalent of `range()` is `np.arange()`. `np.linspace()` is similar to `np.arange()` but differs in its arguments.

```python
print(np.arange(start=0, stop=2, step=0.5))
print(np.linspace(start=0, stop=1.5, num=4))
```

And finally, the `np.random` module has functions for generating random numbers. For example, `np.random.random()` generates random `float`s between 0 and 1:

```python
print(np.random.random((2, 3)))
```


## Indexing and slicing

Let's start with a 2D array of numbers. First create a 1D array with `np.arange()` and then simply change its shape (this is allowed as long as the shape is compatible with the number of elements in the array).

```python
a = np.arange(9)
a.shape = 3, 3
print(a)
```

To get a single number, specify the row (1) and column (2), as always starting from 0:

```python
print(a[1, 2])
```

To get a single row, specify the index of that row:

```python
print(a[1])
```

To get multiple rows, specify a slice:

```python
print(a[1:3])
```

To get a column, get the full slice of rows (`:`), and then specify the column index: (The column now looks like a row, because the result is 1D!)


```python
print(a[:, 1])
```

Or to get multiple columns:

```python
print(a[:, 1:3])
```

## Selecting elements

Consider the expression (`a > 2`):

```python
print(a)
print('Larger than 2?')
print(a > 2)
```

For each element of the array, NumPy checks whether the value is larger than 2. The result is an array of `bool` values. This `bool` array is in itself not that useful, but you can use it to index the original array, like so:

```python
print(a[a > 2])
```

You now get an array of elements that are larger than 2. This array is only 1D, even though the original array was 2D. This is because you have 'shot holes' in the array, and NumPy deals with this by flattening the resulting selection to a 1D array.

You can also select based on multiple criteria. The normal Python operators `and` and `or` don't work in this context! Instead, you have to use `&` (and) and `|` (or). And you have to put parentheses around the criteria. Like so:

```python
print(a[(a > 2) & (a < 7)])
```


## Mathematical operations

If you apply the standard mathematical operators (`*`, `/`, `+`, `-`, `%`, `**`, `//`) to an array, then this operator is applied to each element separately, resulting in a new array. You can even apply multiple operators in a single expression:

```python
print(a)
print('a * 2 - 2:')
print(a * 2 - 2)
```

NumPy has many built-in functions for applying mathematical operations to arrays, such as `np.sqrt()`, `np.exp()`, `np.log()`, etc.

```python
print(a)
print('sqrt(a):')
print(np.sqrt(a))
```


## Mean, median, and standard deviation

You can easily get the mean, median, and standard deviation of an array:

```python
print(a)
print('mean = {}\nmedian = {}\nstd = {}'.format(
    np.mean(a),
    np.median(a),
    np.std(a)
))
```

If you have a multidimensional array, then you can specify the axis across which the mean should be calculated. You can even specify multiple axes; this sounds a bit abstract, but you can think of it as specifying which dimensions should be averaged out. Therefore, specifying all axes is the same as taking the mean across the entire array.

```python
a = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
print(a)
print('mean(across first axis) = {}'.format(a.mean(axis=0)))
print('mean(across second axis) = {}'.format(a.mean(axis=1)))
print('mean(across all axes) = {}'.format(a.mean(axis=(0, 1))))
```

If an array contains `nan` values (see [syntax](%url:syntax%)), then each of the above functions will also return `nan`. This is because of the mathematical convention that every operation that involves a `nan` evaluates to `nan`. However, this behavior is often not what you want, and therefore NumPy contains functions that explicitly ignore `nan` values:

```
a = np.linspace(0, 10, 5)
a[0] = np.nan
print(a)
print('mean = {}\nmedian = {}\nstd = {}'.format(
    np.mean(a),
    np.median(a),
    np.std(a)
))
print('nanmean = {}\nnanmedian = {}\nnanstd = {}'.format(
    np.nanmean(a),
    np.nanmedian(a),
    np.nanstd(a)
))
```


## Exercises

<div class='info-box' markdown=1>

### Removing extreme values

%-- include: exercises/numerical/numpy-1.md --%

[View solution](%url:numpy%-solution-1)

</div>

<div class='info-box' markdown=1>

### Activity in the left vs right brain

%-- include: exercises/numerical/numpy-2.md --%

[View solution](%url:numpy%-solution-2)

</div>
