title: Modules: Exercises and Solutions
next_title: Modules
next_url: %url:modules%


## Files and folders

### Exercise

%-- include: exercises/basic/modules-2.md --%


### Solution

~~~ .python
import os

dirname = '/home/sebastiaan/Downloads'
for basename in os.listdir(dirname):
  path = os.path.join(dirname, basename)
  if os.path.isdir(path):
    print('folder: {0}'.format(path))
  else:
    print('file:   {0}'.format(path))
~~~

__Output:__

~~~
file:   /home/sebastiaan/Downloads/revised_ms.docx
folder: /home/sebastiaan/Downloads/.config
file:   /home/sebastiaan/Downloads/34-278-1-PB.pdf
~~~
