title: Files and folders

This tutorial contains X interactive mini exercises and two review exercises. Try to solve them all!

[TOC]


## What are files, folders, and paths?

Computer data is generally organized in a structure of *files* and *folders*. Folders, which are sometimes also called *directories*. are containers that can contain files and also other (sub)folders.

For example, I could have a folder called `coding` that contains two subfolders called `python` and `r`, which in turn contain a number of Python (`.py`) and R (`.R`) scripts with exercises. In this case, your files-and-folders structure would look like this:

```
/home/sebastiaan/coding/
    python/
        exercices1.py
        exercises2.py
    R/
        exercises1.R
        exercises2.R
```

Let's define a few important terms. You don't have to remember all of these immediately, but you can refer back to this list when you encounter an unknown term later on.

- A *path* is the name of a file or folder.
- The *root* is the top-level folder in the path. In the example above, the root is simply `/`. On Windows systems (see below), the root is the drive letter (e.g. `c:\`).
- The *working directory* is the currently active folder. When executing a Python script from a code editor, the working directory is usally the folder that contains the script.
- The *home folder* is the folder that contains user-specific files. In the example above, the home folder is `/home/sebastiaan/`. The home folder is often abbreviated as `~/`.
- An *absolute path* fully specifies the location of a file or folder. In the example above, the absolute path to `exercises1.py` is `/home/sebastiaan/coding/python/exercises1.py`.
- A *relative path* only specifies the location relative to the current working directory. In the example above, and assuming that I'm currently working in the folder `/home/sebastiaan/coding`, the relative path to `exercises1.py` is `coding/python/exercises1.py`. Note that a relative path doesn't start with a `/` (i.e. doesn't contain the root).
- A *extension*, sometimes also called *suffix*, is the part of the file name that follows (and includes) the final `.`. The extension of `exercises1.py` is `.py`. Extensions usually indicate the file type, such as `.py` for Python scripts. Not all files have an extension.
- A *wildcard* is a special character that acts as a placeholder in a path. The most common wildcard is the `*`, which matches anything. For example, the wildcard string `*.py` matches any path that ends with `.py`.
- A *glob* is a collection of paths that matches a wildcard string. For example, the glob for `coding/python/*.py` consists of `exercise1.py` and `exercise2.py`.


## Differences between operating systems

Except for Windows, all operating systems use the slashforward (`/`). Windows uses the slashback (`\`) as a path separator; absolute paths in windows also include a drive letter, such as `C:\`.

Different operating systems also use different naming conventions for home folders: Windows: `C:\Users\[name]`, Linux: `/home/[name]`, Mac OS: `/user/[name]`.

Luckily, Python avoids you from having to worry about these differences: no matter with operating system you are using, you can use the `\` path separator and `~` (or `Path.home()`) to refer to the home folder. Python will make sure that these paths are correctly interpreted on all operating systems.


## The pathlib module and the Path class

The `Path` class from the [`pathlib` module](https://docs.python.org/3/library/pathlib.html) provides an intuitive way work with files and folders. Let's create a `Path` object that corresponds to the `coding/python/` folder. We use a relative path and assume that my home folder is the current working directory.

```python
from pathlib import Path
py_exercises = Path('coding/python/')
print(py_exercises)
```

You can concatenate Path objects using the `/` operator. For example, we can create a new `Path` object that corresponds to `exercises1.py` like so:

```python
py_exercise1 = py_exercises / Path('exercise1.py')
```


## Listing files and folders

To list files in a folder, use the `glob()` function. You can specify a wildcard string to indicate which files you want. To list all files, specify the `*` wildcard string (which matches any path).

```python
print(f'All files in {py_exercises}:')
for path in py_exercises.glob('*'):
    print(f'- {path}')
```

## Creating, renaming, and removing files and folders

So far, we've worked with `Path` objects that all correspond to existing files and folders. However, you can also create `Path` object for a non-existing path, in which case the `exists()` function will return `False`.

Let's say that we want to create a folder for exercises in the Julia programming language. We first create a Path object for this non-existing folder:

```python
jl_exercises = Path('coding/julia')
print(jl_exercises.exists())
```

And then we use the `mkdir()` function to turn this non-existing path into an actual folder.

```python
jl_exercises.mkdir()
print(jl_exercises.exists())
```

We can create an empty file inside this folder in a very similar way except that we need the `touch()` function for files:

```python
jl_exercise1 = jl_exercises / Path('exercise1.jl')
jl_exercise1.touch()
print(jl_exercise1.exists())
```

Most common operations related to files and folders can be handled by the `Path` class. However, there is one common scenario that the `Path` class *cannot* handle: deleting folders that are not empty. For example, if we would try to delete the `coding/julia` folder that we created above, then we would get an `OSError` because the directory isn't empty (it contains `exercise1.jl`):

```python
# should-raise
jl_exercises.rmdir()
```

To recursively delete the folder, that is, to delete the folder and everything inside it, you need to use `rmtree()` from the [`shutil` module](https://docs.python.org/3/library/shutil.html) instead.

```python
import shutil
shutil.rmtree(jl_exercises)
print(jl_exercises.exists())
```


## Reading and writing files


### Text files

Earlier in this tutorial, we created `py_exercise1`, which is a `Path` object that corresponds to the file `exercise1.py`. Let's see how you can read the contents of this file in the easiest way possible, using the `Path.read_text()` function:

```python
print(f'The contents of {py_exercise1} are:')
contents = py_exercise1.read_text()
print(contents)
```

Writing to text files is almost as easy as reading from them:


```python
contents = 'Define a factorial function using recursion!'
py_exercise2 = Path('coding/python/exercise2.py')
py_exercise2.write_text(contents)
```

Be careful! Calling `Path.write_text()` will create a new file and open it for writing, so the previous contents of the file are lost. If you want to add text to an existing file without erasing its contents, you need to use a slightly more verbose approach, using a `with` context and `Path.open('a')` to indicate that you want to open the file in 'append' mode:

```python
with py_exercise2.open('a') as fd:
    fd.write('\nThis line will be appended to the file')
```

For the purpose of being able to append text to a file, it is not crucial to understand what a `with` context is exactly. However, if you want to fully understand the code above, take a look at [this page of the Python docs](https://docs.python.org/3/reference/compound_stmts.html#with).


### Binary (non-text) files

Python makes a distinction between text (`str` objects) and binary (`bytes` objects) data. Of course, text also consists of bytes, but there is an additional layer on top of it, namely the character encoding that specifies how bytes should be translated into human-readable text, which does not exist for binary data.

Images are binary files. Say that we want to read a photo of De Boef, which you will meet later on in the deep-learning tutorial on [classifying images](%link:image-classification%). We can do this as follows:

```python
img = Path('data/boef.jpg')
contents = img.read_bytes()
print(f'File contents are of type {type(contents)}')
```

To write binary data to a file, simply call `Path.write_bytes()`:

```python
img_copy = Path('copy-of-boef.jpg')
img_copy.write_bytes(contents)
```


## Review exercises
