title: Loops: Exercises and Solutions
next_title: loops
next_url: %url:loops%


## Best-selling artists

### Exercise

%-- include: exercises/basic/loops-2.md --%


### Solution

~~~ .python
sales = {}
while True:
  artist = input('Enter an artist name: ')
  if artist == 'quit':
    break
  if artist in sales:
    print('{0} has sold {1} records'.format(artist, sales[artist]))
    continue
  sold = input('Enter sales: ')
  sales[artist] = sold
~~~

__Output:__

~~~
Enter an artist name: Michael Jackson
Enter sales: 350000000
Enter an artist name: Michael Jackson
Michael Jackson has sold 350000000 records
Enter an artist name: quit
~~~
