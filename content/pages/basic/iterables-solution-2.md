title: Iterables: Exercises and Solutions
next_title: Iterables
next_url: %url:iterables%


## Best-selling artists

### Exercise

%-- include: exercises/basic/iterables-2.md --%


### Solution

~~~ .python
artists = {
  'The Beatles': 600e6,
  'Elvis Presley': 600e6,
  'Michael Jackson': 350e6,
  'Madonna': 300e6
}
artist = input('Enter an artist name: ')
sold = artists.get(artist, 'unknown')
print('{0} has sold {1} records'.format(artist, sold))
~~~

__Output:__

~~~
Enter an artist name: Rick Ross
Rick Ross has sold unknown records
~~~
