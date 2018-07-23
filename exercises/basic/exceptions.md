You're going to write an interactive calculator! User input is assumed to be a formula that consist of a number, an operator (at least `+` and `-`), and another number, separated by white space (e.g. `1 + 1`). Split user input using [`str.split()`](https://docs.python.org/3/library/stdtypes.html#str.split), and check whether the resulting `list` is valid:

- If the input does not consist of 3 elements, raise a `FormulaError`, which is a custom `Exception`.
- Try to convert the first and third input to a `float` (like so: `float_value = float(str_value)`). Catch any `ValueError` that occurs, and instead raise a `FormulaError`
- If the second input is not `'+'` or `'-'`, again raise a `FormulaError`

If the input is valid, perform the calculation and print out the result. The user is then prompted to provide new input, and so on, until the user enters `quit`.

An interaction could look like this:

~~~
>>> 1 + 1
2.0
>>> 3.2 - 1.5
1.7000000000000002
>>> quit
~~~
