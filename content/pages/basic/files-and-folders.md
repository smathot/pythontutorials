title: Files and folders


<div class="learning-goals" markdown="1">
Files and folders are the building blocks of computer data! Knowing how to programmatically navigate the file system and how to read from and write to files is a crucial skill. So let's learn how to do this!
{.summary}

In this chapter, you will learn
{.header}

- Key terms and concepts related to files and folders
- How to use the `Path` object
- How to write to and read from files

Test yourself
{.header}

- One interactive mini exercise
- One review exercise
</div>


[TOC]


## What are files, folders, and paths?

Computer data is generally organized into *files* and *folders*. Files contain the actual data: images, text files, etc. Folders (or *directories*) are containers that contain files and other (sub)folders.

For example, my home folder (`/home/sebastiaan`) contains a subfolder called `coding`, which in turn contains two subfolders called `python` and `r`, which in turn contain a number of Python (`.py`) and R (`.R`) scripts with exercises. Like this:

```
/home/sebastiaan/coding/
    python/
        exercice1.py
        exercise2.py
    R/
        exercise1.R
        exercise2.R
```


### Important terms

Before we start, let's define the most important terms related to files and folders. You don't have to remember them right now, but you can refer back to this list when you encounter an unknown term later on.

- A __path__ is the location of a file or folder.
- The __root__ is the top-level folder of the path. On Mac OS and Linux, the root is simply `/`. On Windows, the root is the drive letter (e.g. `c:\`). (We will return to differences between operating systems below.)
- The __working directory__ is the currently active folder. When executing a Python script from a code editor, the working directory is usally the folder that contains the script.
- The __home folder__ is the folder that contains user-specific files. My home folder is `/home/sebastiaan/`. The home folder is often abbreviated as `~/`.
- An __absolute path__ specifies the location of a file or folder relative to the root. In the example above, the absolute path to `exercise1.py` is `/home/sebastiaan/coding/python/exercise1.py`.
- A __relative path__ specifies the location of a file or folder relative to the working directory. In the example above, and assuming that I'm working in the folder `/home/sebastiaan/coding`, the relative path to `exercise1.py` is `coding/python/exercise1.py`. Note that a relative path doesn't start with a `/` (i.e. doesn't contain the root).
- An __extension__ (or *suffix*) is the part of the path that follows (and includes) the final `.`. The extension of `exercise1.py` is `.py`. Extensions usually indicate the file type; for example, you can recognize Python scripts by the `.py` extension. Not all files have an extension.
- A __wildcard__ is a special character that acts as a placeholder in a path. The most common wildcard is the `*`, which matches anything. For example, the wildcard string `*.py` matches any path that ends with `.py`.
- A __glob__ is a collection of paths that matches a wildcard string. For example, the glob for `coding/python/*.py` consists of `exercise1.py` and `exercise2.py`.


### Differences between operating systems

Mac OS and Linux use the (forward) slash (`/`) as a path separator; that is, the `/` separates individual folders and files in a path. In contrast, Windows uses the backslash (`\`) as a path separator; absolute paths in windows also include a drive letter, such as `C:\`.

Different operating systems also use different naming conventions for home folders: Windows: `C:\Users\[name]`, Linux: `/home/[name]`, Mac OS: `/user/[name]`. (As you can tell from the name of my home folder, I use Linux.)

Luckily, Python avoids you from having to worry about these differences: no matter with operating system you are using, you can use the `\` path separator and `~` (or `Path.home()`) to refer to the home folder. Python will make sure that these paths are correctly interpreted on all operating systems.

*Pro-tip:* As you've learned in the [Syntax](%url:syntax%) chapter, the backslash also serves as an escape character in Python; that is, the `\` allows you to indicate non-printable characters, such as a tab stop (`\t`) or line break (`\n`). Therefore, it's easiest to avoid the backslash altogether when working with paths, even on Windows.


## The pathlib module and the Path class

The `Path` class from the [`pathlib` module](https://docs.python.org/3/library/pathlib.html) provides an intuitive way work with files and folders. Let's create a `Path` object that corresponds to the `coding/python/` folder. We use a relative path and assume that my home folder is the current working directory.

```python
from pathlib import Path
py_exercises = Path('coding/python/')
print(py_exercises)
```

Path objects can be combined using the `/` operator. Let's use this to create a new `Path` object that corresponds to `exercise1.py`:

```python
py_exercise1 = py_exercises / Path('exercise1.py')
print(py_exercise1)
```

`Path` objects have a number of convenient functions and properties:

- `Path.exists()` returns `True` if the path corresponds to an existing file or folder
- `Path.parent` returns the parent folder of a file or folder, such as `coding/python` for for `coding/python/exercise1.py`
- `Path.is_file()` returns `True` if the path corresponds to an existing file
- `Path.is_dir()` returns `True` if the path corresponds to an existing folder
- `Path.name` returns the name without the parent folder, such as `exercise1.py` for `coding/python/exercise1.py`
- `Path.stem` returns the name without the file extension, such as `exercise1` for `exercise1.py`
- `Path.suffix` returns the file extension, such as `.py` for `exercise1.py`


<div class="exercise" id="exercise_if" markdown="1">
#### Mini exercise

Create a path object that corresponds to the absolute path to `exercise1.py` and print it out. (Except for the most basic functionality, the `Path` class does not work in a browser. That's why this chapter only contains this one interactive mini exercise.)

<textarea class="code"></textarea>
<div hidden class="solution_output">/home/sebastiaan/coding/python/exercise1.py</div>
</div>


### Listing files and folders

The `Path.glob()` function returns a list of files and subfolders inside a folder. You can specify a wildcard string to indicate which files you want. To list all files, specify the `*` wildcard string (which matches any path).

```python
print(f'All files in {py_exercises}:')
for path in py_exercises.glob('*'):
    print(f'- {path}')
```


### Creating and removing files and folders

So far, we've worked with `Path` objects that correspond to files and folders that already exist. However, you can also create `Path` objects for files and folders that do not (yet) exist. The `Path.exists()` function allows you to tell whether or not a path exists.

Let's say that we want to create a folder for exercises in the Julia programming language. We first create a Path object for this non-existing folder:

```python
jl_exercises = Path('coding/julia')
print(jl_exercises.exists())
```

Next, we use the `Path.mkdir()` function to create an empty folder at this location:

```python
jl_exercises.mkdir()
print(jl_exercises.exists())
```

*Pro-tip:* `Path.mkdir()` by default requires that the parent folder (`coding` in the example above) already exists. When this is not the case, you can use `Path.mkdir(parents=True)` to also create all non-existing parent folders.

To create an empty file inside this folder, we use the `Path.touch()`:

```python
jl_exercise1 = jl_exercises / Path('exercise1.jl')
jl_exercise1.touch()
print(jl_exercise1.exists())
```

Most common operations related to files and folders can be handled by the `Path` class. Let's consider the most important functions:

- `Path.mkdir()` creates a folder (see above)
- `Path.rename()` renames a file or folder
- `Path.rmdir()` deletes a folder (which cannot be empty, see below)
- `Path.touch()` creates an empty file
- `Path.unlink()` deletes a file

However, there is one common scenario that the `Path` class *cannot* handle: deleting folders that are not empty. For example, if we would try to use `Path.rmdir()` to delete the `coding/julia` folder that we created above, then we would get an `OSError` because the directory isn't empty (it contains `exercise1.jl`):

```python
# should-raise
jl_exercises.rmdir()
```

To recursively delete the folder, that is, to delete the folder and everything inside it, you can use `rmtree()` from the [`shutil` module](https://docs.python.org/3/library/shutil.html) instead.

```python
import shutil
shutil.rmtree(jl_exercises)
print(jl_exercises.exists())
```

*Pro-tip*: There is a lot of overlap between the functionality of the (newer) `Path` class and the (older) `os`, `os.path`, and `shutil` modules. For most purposes, using the `Path` class is recommended because it results in code that is easier to read and write.


## Reading and writing files


### Text files

`py_exercise1` is a `Path` object that corresponds to the file `exercise1.py` (see above). To read the contents of this file, we can use `Path.read_text()`:

```python
print(f'The contents of {py_exercise1} are:')
contents = py_exercise1.read_text()
print(contents)
```

Writing to text files is almost as easy as reading from them, using `Path.write_text()`:


```python
contents = 'Define a factorial function using recursion!'
py_exercise2 = Path('coding/python/exercise2.py')
py_exercise2.write_text(contents)
```

*Pro-tip:* Calling `Path.write_text()` creates a new file and opens it for writing. This means that the file will be overwritten if it already existed. If you want to add text to an existing file without erasing its contents, you need to use a slightly more verbose approach, using a `with` context and `Path.open('a')` to indicate that you want to open the file in 'append' mode:

```python
with py_exercise2.open('a') as fd:
    fd.write('\nThis line will be appended to the file')
```

For the purpose of being able to append text to a file, it is not crucial to understand what a `with` context is exactly. However, if you want to fully understand the code above, take a look at [this page of the Python docs](https://docs.python.org/3/reference/compound_stmts.html#with).


### Binary (non-text) files

Python makes a distinction between text (`str` objects) and binary (`bytes` objects) data. Of course, text also consists of bytes, but there is an additional layer on top of it, namely the character encoding that specifies how bytes should be translated into human-readable text. Binary data does not have this and often does not correspond to human-readable text.

Images are binary files. Say that we want to read a photo of De Boef, which you may meet later on in the deep-learning course chapter on [classifying images](%link:image-classification%). We can do this as follows:

```python
img = Path('data/boef.jpg')
contents = img.read_bytes()
print(f'File contents are of type {type(contents)}')
```

![](data/boef.jpg)

To write binary data to a file, simply call `Path.write_bytes()`:

```python
img_copy = Path('copy-of-boef.jpg')
img_copy.write_bytes(contents)
```


## Review exercise

### An interactive file browser

%-- include: exercises/basic/files-and-folders.md --%

This exercise is not checked automatically, because there are several possible solutions. Click [here](%url:files-and-folders%-solution) to see one solution!


<hr />


This concludes the Python Basics course. Congratulations—you made it to the finish line!

<div>
<a class='btn btn-success btn-large btn-block' href='/'>Go back to the home page</a></p>
</div>
