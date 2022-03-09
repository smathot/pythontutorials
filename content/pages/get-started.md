title: Getting started
next_title: Syntax
next_url: %url:syntax%


There are many ways in which you can install and use Python. If you're unsure how to get started, the instructions below are a good way to get coding quickly!


## Python 2 or 3?

There are two main versions of Python: 2 and 3. The recommended version is Python 3, which is newer and actively maintained. Python 2 is still used occasionally, but only because certain Python libraries have not yet been updated to be compatible with Python 3.


## Interactive mini exercises in the browser

Most tutorials on this site contain interactive mini exercises. These consist of a problem to solve, and a small editor in which you can enter your solution in the form of Python code. You can click the Run button to execute your code, and the output appears in a box below. In most cases, your solution will be checked automatically.

<div class="exercise" id="exercise_get_started" markdown="1">
#### Mini exercise

Click on the Run button to execute the code and solve this mini exercise!

<textarea class="code">
print('Welcome to PythonTutorials.eu!')
</textarea>
<div hidden class="solution_output">Welcome to PythonTutorials.eu!</div>
</div>

If you want to start learning Python right away, without installing anything, you can skip the rest of this section. However, if you want to use Python for real-life programming, you will need a code editor with a Python environment, such as Rapunzel or Spyder.

<a role="button" class="btn btn-primary btn-large btn-block" href="%url:syntax%">
Skip the rest and get started with <b>Syntax >></b>
</a>

## Rapunzel

Rapunzel is a free code editor focused on numerical computing with Python. It is included with [OpenSesame](https://osdoc.cogsci.nl/). You can also download it as a standalone application from here:

- <https://rapunzel.cogsci.nl/>

In Rapunzel, create an empty document (`Ctrl+N`) and enter the code `print('Hello world!')` in the editor window. Next, press `F9` to execute (%FigRapunzel). This will execute this line of code in the so-called IPython Console, which by default is on the bottom of the window. You can also type directly into this console.



%--
figure:
 id: FigRapunzel
 source: rapunzel.png
 caption: |
  Printing 'Hello world' to the IPython console in Rapunzel.
--%



## Anaconda

Anaconda is a Python distribution that comes with many useful packages pre-installed. Notably, it comes with [Spyder](https://www.spyder-ide.org/) pre-installed, which is another popular code editor for Python.

1. Visit <http://anaconda.org/>, click on *Download Anaconda*, and download the 64 bit version for Python 3.
2. Once the `.exe` installer has been downloaded, launch it and follow the steps to install Anaconda on your system. The default installation settings are generally fine.
3. Now launch Spyder, which has been installed as part of Anaconda.

In Spyder, enter the code `print('Hello world!')` in the editor window, select it and press `F9` to execute (%FigSpyder). This will execute this line of code in the so-called IPython Console, which by default is on the bottom-right of the window. You can also type directly into this console.

%--
figure:
 id: FigSpyder
 source: spyder.png
 caption: |
  Printing 'Hello world' to the IPython console in Spyder.
--%


All set up? Then let's begin with [Basic Syntax](%url:syntax%)!
