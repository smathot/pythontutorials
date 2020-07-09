title: DataMatrix
next_title: Plotting
next_url: %url:plotting%


[TOC]


## What is DataMatrix?

[DataMatrix](https://datamatrix.cogsci.nl/) is a Python library for working with tabular data, i.e. spreadsheet-like data that consists of named columns and numbered rows. DataMatrix is a light-weight library that allows you to do many things in an intuitive way. (For more advanced functionality, you can use [pandas](https://pandas.pydata.org/).).

This is an abbreviated version of the following page:

- <https://datamatrix.cogsci.nl/basic/>


## Creating a DataMatrix

Create a new `DataMatrix` object, and add a column (named `col`). By default, the column is of the `MixedColumn` type, which can store numeric and string data.

```python
from datamatrix import DataMatrix

dm = DataMatrix(length=3)
print(dm)
```

You can change the length of the `DataMatrix` later on. If you reduce the length, data will be lost. If you increase the length, empty cells will be added.


## Working with columns

If you assign to a column that doesn't exist, it will be automatically created. If you assign a single value to a column, this will change all cells to that value:

```python
dm.col = 'This creates a new column'
print(dm)
```

If you assign a sequence to a column, this will change the cells based on that sequence. This sequence must have the same length as the column (3 in this case).

```python
dm.col = 1, 2, 3
print(dm)
```


## Slicing and assigning to column cells

You can assign to one cell, to multiple cells at the same time, or to a slice of cells.

```python
dm.col[1] = ':-)'
dm.col[0, 2] = ':P'
dm.col[1:] = ':D'
print(dm)
```


## Column properties

Basic numeric properties, such as the mean, can be accessed directly. Only numeric values are taken into account.

%--
python: |
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
--%


## Iterating over rows, columns, and cells

By iterating directly over a `DataMatrix` object, you get successive `Row` objects. From a `Row` object, you can directly access cells. By iterating over a `Row` object, you get `column name, cell value` tuples.

```python
dm.col = 'a', 'b', 'c'
for row in dm:
    print(row.col)
    for colname, cell in row:
        print('%s = %s' % (colname, cell))
```

By iterating over `DataMatrix.columns`, you get successive `(column_name, column)` tuples.

```python
for colname, col in dm.columns:
    print('%s = %s' % (colname, col))
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


## Selecting data

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


## Element-wise column operations

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


## Reading and writing files

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


## Exercises

<div class='info-box' markdown=1>

### Analyzing movie ratings

%-- include: exercises/numerical/datamatrix-1.md --%

[View solution](%url:datamatrix%-solution-1)

</div>

</div>
