title: Files and folders: Exercise and Solution
next_title: Files and folders
next_url: %url:files-and-folders%


## An interactive file browser

### Excercise

%-- include: exercises/basic/files-and-folders.md --%


### Solution

~~~python
import os
from pathlib import Path

while True:
  # Build a list of files and folders in the working directory.
  entries = []
  current_folder = Path.cwd()
  # If we're not already in the root, the first entry is the parent folder
  if current_folder.parent != current_folder:
    entries.append(Path('..'))
  entries += current_folder.glob('*')
  # Print a numbered list of files and folders
  print(f'Listing contents of {current_folder}')
  for i, path in enumerate(entries):
    print(f'{i}: {path.name}')
  # Get user input. Valid input is the word 'quit' or a number that corresponds
  # to an index in the list of files and folders
  user_input = input('>>> ')
  if user_input == 'quit':
    break
  try:
    selection = int(user_input)
  except ValueError:
    print('Invalid user input (please enter a number)')
    continue
  if selection >= len(entries):
    print('Invalid user input (invalid number)')
    continue
  # If the selected path is a folder, then change the working directory to
  # that folder
  selected_path = Path(entries[selection])
  if selected_path.is_dir():
    os.chdir(selected_path)
    continue
  # Otherwise, try to read the file contents as if they are text. If this fails
  # print a warning message
  try:
    file_contents = selected_path.read_text()
  except UnicodeDecodeError:
    print(f'{selected_path.name} is not a text file')
    continue
  # Otherwise print the file contents
  print(file_contents)
~~~
