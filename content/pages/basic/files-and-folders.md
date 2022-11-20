title: Files and folders

This tutorial contains X interactive mini exercises and two review exercises. Try to solve them all!

[TOC]


## What are files, folders, and paths?

Data on the drive of a computer is generally organized in a structure that consists of *files* and *folders* (sometimes also called *directories*). Folders are containers that can contain files and also other (sub)folders.

For example, you may have a folder called `coding` that contains two subfolders called `python` and `r`, which in turn contain a number of Python (`.py`) and R (`.R`) scripts with exercises. In this case, your files-and-folders structure would look like this:

- `/home/sebastiaan/coding/`
  - `python/`
    - `exercices1.py`
    - `exercises2.py`
  - `R/`
    - `exercises1.R`
    - `exercises2.R`


A *path* is the name of a file or folder. An *absolute path* completely specifies the location of a file or folder. In the example above, the absolute path to `exercises1.py` would be `/home/sebastiaan/coding/python/exercises1.py`. A *relative path* only specifies the location relative to the currently active folder, in this context usually called the *working directory*. In the example above, and assuming that I'm currently working in the folder `/home/sebastiaan/coding`, the relative path to `exercises1.py` woul be `python/exercises1.py`. Note that a relative path doesn't start with a `/`.

On Windows, paths are often separated by `\` characters (rather than `/`) and absolute paths also include a drive letter, such as `c:\`. So 

`c:\users\sebastiaan\coding\python\exercises1.py`


## The Path object

```python
from 
```


## Reading and writing files

### Text files


### Binary (non-text) files


## Listing files and folders


## Removing and renaming files and folders


## Review exercises
