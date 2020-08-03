title: DataMatrix
next_title: Plotting
next_url: %url:plotting%


[TOC]


## What is DataMatrix?

[DataMatrix](https://datamatrix.cogsci.nl/) is a Python library for working with tabular data, i.e. spreadsheet-like data that consists of named columns and numbered rows. DataMatrix is a light-weight library that allows you to do many things in an intuitive way. (For more advanced functionality, you can use [pandas](https://pandas.pydata.org/).).

This tutorial is an abbreviated version of the following page:

- <https://datamatrix.cogsci.nl/basic/>


## Basics


### Creating a DataMatrix

Create a new `DataMatrix` object. The `length` keyword specifies the number of rows. A newly created `DataMatrix` doesn't have any columns yet.

```python
from datamatrix import DataMatrix

dm = DataMatrix(length=3)
print(dm)
```


### Working with columns

If you assign a value to a column that doesn't exist, the column will be automatically created. If you assign a single value to a column, this will set all cells to that value:

```python
dm.col = 'This creates a new column'
print(dm)
```

If you assign a sequence to a column, this will set the cells based on that sequence. This sequence must have the same length as the column (3 in this case).

```python
dm.col = 'one', 'two', 'three'
print(dm)
```


### Slicing and assigning to column cells

You can assign to one cell, to multiple cells at the same time, or to a slice of cells.

```python
dm.col[1] = ':-)'  # Assign to one cell
dm.col[0, 2] = ':P'  # Assign to two cells
dm.col[2:] = ':D'  # Assing to a slice of cells
print(dm)
```


### Column properties

Basic numeric properties, such as the mean, can be accessed directly. Only numeric values are taken into account.

```python
dm.col = 1, 2, 'not a number'
# Numeric descriptives
print('mean: %s' % dm.col.mean)
print('median: %s' % dm.col.median)
print('standard deviation: %s' % dm.col.std)
print('sum: %s' % dm.col.sum)
print('min: %s' % dm.col.min)
print('max: %s' % dm.col.max)
# Other properties
print('unique values: %s' % dm.col.unique)
print('number of unique values: %s' % dm.col.count)
print('column name: %s' % dm.col.name)
```


### Iterating over rows, columns, and cells

By iterating directly over a `DataMatrix` object, you get successive `Row` objects. From a `Row` object, you can directly access cells. By iterating over a `Row` object, you get `column name, cell value` tuples.

```python
dm.col = 'a', 'b', 'c'
for row in dm:
    print(row.col)
    for colname, cell in row:
        print('{} = {}'.format(colname, cell))
```

By iterating over `DataMatrix.columns`, you get successive `(column_name, column)` tuples.

```python
for colname, col in dm.columns:
    print('{} = []'.format(colname, col))
```

By iterating over a column, you get successive cells:

```python
for cell in dm.col:
    print(cell)
```

The `column_names` property gives a sorted list of all column names (without the corresponding column objects):

```python
print(dm.column_names)
```


### Element-wise column operations

You can apply basic mathematical operations on all cells in a column simultaneously. Cells with non-numeric values are ignored, except by the `+` operator, which then results in concatenation.

```python
dm = DataMatrix(length=3)
dm.col = 0, 'a', 20
dm.col2 = dm.col * .5
dm.col3 = dm.col + 10
dm.col4 = dm.col - 10
dm.col5 = dm.col / 50
print(dm)
```

You can apply a function (or `lambda` expression) to all cells in a column simultaneously with the `@` operator.

```python
def times_two_plus_one(x):
    return x * 2 + 1

dm = DataMatrix(length=3)
dm.col = 0, 1, 2
dm.col2 = dm.col @ times_two_plus_one
print(dm)
```


### Reading and writing files

You can read and write files with functions from the `datamatrix.io` module. The main supported file types are `csv` and `xlsx`.

```python
from datamatrix import io

dm = DataMatrix(length=3)
dm.col = 1, 2, 3
# Write to disk
io.writetxt(dm, 'my_datamatrix.csv')
io.writexlsx(dm, 'my_datamatrix.xlsx')
# And read it back from disk!
dm = io.readtxt('my_datamatrix.csv')
dm = io.readxlsx('my_datamatrix.xlsx')
```


## Splitting and selecting data

### Selecting

You can select by directly comparing columns to values. This returns a new `DataMatrix` object with only the selected rows.

```python
dm = DataMatrix(length=10)
dm.col = range(10)
dm_subset = dm.col > 5
print(dm_subset)
```

You can select by multiple criteria using the `|` (or), `&` (and), and `^` (xor) operators (but not the actual words 'and' and 'or'). Note the parentheses, which are necessary because `|`, `&`, and `^` have priority over other operators.

```python
dm_subset = (dm.col < 1) | (dm.col > 8)
print(dm_subset)
```


### Splitting

You can also split a DataMatrix into subsets, using the `split()` function from `datamatrix.operations` (usually imported as `ops`). To do this, specify a column with discrete values that indicate the groups into which you want to split. For example, consider [this dataset](/data/heartrate.csv) from Moore, McCabe, & Craig (included as example data with JASP). This contains heart rate values for runners and non-runners (controls).

The first way to use `ops.split()` is by only specifying a column to split the data based on. In this case, the function returns a sequence of `value, subdatamatrix` tuples that you can iterate through with a `for` loop: (Note the alternative way to refer to columns that contain spaces or non-ascii characters: `dm['Heart Rate']`.)


```python
from datamatrix import io
from datamatrix import operations as ops

dm = io.readtxt('data/heartrate.csv')
for group, group_dm in ops.split(dm.Group):
    print('Mean heart rate for {} is {} bpm'.format(
        group,
        group_dm['Heart Rate'].mean)
    )
```

The second way to use `ops.split()` is by also specifying the values that you want to split on. In this case, the function returns a sequence of `subdatamatrix` objects that match the order of the splitting values. Like so:


```python
dm_runner, dm_control = ops.split(dm.Group, 'Runners', 'Control')
print('Mean heart rate for runners is {} bpm'.format(dm_runner['Heart Rate'].mean))
print('Mean heart rate for controls is {} bpm'.format(dm_control['Heart Rate'].mean))
```

## Exercises

<div class='info-box' markdown=1>

### Analyzing movie ratings

%-- include: exercises/numerical/datamatrix-1.md --%

[View solution](%url:datamatrix%-solution-1)

</div>

<div class='info-box' markdown=1>

### Removing poorly performing participants

%-- include: exercises/numerical/datamatrix-2.md --%

[View solution](%url:datamatrix%-solution-2)

</div>
