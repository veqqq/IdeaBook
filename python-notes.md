- // interger division rounds down 5.0 // 3.0 = 1.0, -5.0 // 3.0 = -2.0
  - / division gives floats 10.3 / 3 = 3.333...5
- == comparison/equality operator : 2 == True => False
  - is checks if 2 variables refer to same object, == if objects have same values
    - use is to compare None
  - != not equal
  - >, <, <=, >= # comparisons
  - 1<2 and 2<3 # seem if value is in a range  (or 1 < 2 < 3)
- "yay!" if 0 > 1 else "nay!"  # => "nay!"

###### booleans
- True and False  => False
- False or True => True
- not False => True
- True + True => 2 # booleans are actually 1 and 0.
  - 0 == False => True #== comparison operator
  -5 != False => True
- None, 0, empty strings/lists... evaluate to false `bool(0)` or `bool([])` => False
  
###### strings
- "Hello " + "world!"
- "Hello"[0] => "H"
- len() - gives length
- f formats(?) (fills in variables?)
  - `f"{name} is {len(name)} characters long." (if you already said name = bob)
- print() defaults to a newline
  - end="1" will end the string with ! instead of \n
- inputdata = input("Please type:") #gets typed stuff as a string

### Control Flow, Iterables

##### loops
- if variable > 10:
  - elif variable2 > 15:
  - else
  - `for animal in ["dog", "cat", "mouse"]` #for iterates over lists
  - print("{} is a mammal".format(animal))
- for i, value in enumerate(animals):
    print(i, value) => 0 dog, 1 cat, 2 mouse
- while x < 4: #iterates until condition ends
  print(x)
  x+=1
- range (start, end, step)  # generates numbers e.g. range(4,8,2) =4 6 8
- exceptions
  - try: - 
  - pass - just ends the operation
  - else: - if the first thing didn't work
  - finally: - do in all cases
- with - closes stuff when done(?)
  - used for writing files like `with open("thisfile.txt") as file1:`
- iterable - object treated as a sequence (e.g. the object range() returns
  - you can't do e.g. iterable[1] because it has no index, rather it generates itself
  - next(iterator) - returns the next part
  - its what for loops do...  
  - make it into a list: list1 = list(iteratorsname)
 
#### functions

- def add(x, y):
  print("x is {} and y is {}".format(x, y))
  return x + y 
add(y=6, x=5) # to use the function
- * variable number of arguments
- ** gives variable number of keyword arguments
  - using this with tuples list1(\*args) or dict1(\*\*keywords) is equivilent to list1(1, 2, 3)
- def set_x(num):
  x = num #local var, not same as global!
  global x
  x = num # now it sets the global!
    
### data structures - lists, tuples, dicts, strings, sets, frozensets
- Due to CPU cache, a flat array or hashmap is almost always the best, regardless of theoretical ramifications
  - CPU has a memory cache, when accessing memory, the CPU checks its own cache first. If it's not there, it goes to RAM (100x slower). That's called cache miss. Reducing cache miss leads to high performance code. Flat arrays are easy to fit in the cache as its contigious blocks of memory.  It can also check a range of memory, making it easier to check!
  - https://www.bigocheatsheet.com/
  - https://www.interviewcake.com/article/java/big-o-notation-time-and-space-complexity?
-Python doesn't come with alot of the advanced data structures but creating them is a breeze with lists, dictionaries and objects as long as you understand the Abstract Data Type. 

##### list [ ]
- list1 = [4, 5, 6]
- list1.append(1) # adds 1 to the end
- list1.pop() #removes final thing from the list
- list1[0] outputs 4
  - list[5] gives IndexError
- slices [start:end:step] e.g. list1[1:3], list1[2:], [::2] every 2nd entry, [::-1] reversed
- list1 = list2[:] makes a copy, one layer deep(?) (but list1 is list2 => False)
- del list1[2] deletes the 3rd thing
- list1.remove(2) deletes the first occurance of this value
- list1.insert(1, 2) - inserts element "1" at index location 2
- list1.index(2) - returns index of the first occurance
- list1+list2 => 4, 5, 6, 4, 5, 6
- list1.extend(otherlist) # adds the list to the other and actually changes it
- 1 in list1 => False (isn't in the list)
- len(list1)

####### tuples ( ) - faster, less memory - immutable lists, use same list operations...
- tup1 = (1, 2, 3) #n.b. tup2 = (1,) because int1=(1). Use type((1)) and type((1,))
- a, b, c = (1, 2, 3) unpacks a tupple (or list) into variables. a, b = b, a to switch them?

####### dictionaries { : }- key: value pairs - python's version of a map
- dict1 = {"one": 1, "two": 2}
- n.b. keys must be immutable, because they're constant hash values for quick lookup
  - {[1,2,3]: "123"} raises TypeError: unhashable type: 'list'
  - {(1,2,3):[1,2,3]} is fine
- list(dict1.keys()) => ["one", "two"] #n.b. in python<3.7 it's backwards [two, one]
- values()
- "one" in dict1 # looks for keys
- get("one") gives the value from a key
- .setdefault("five", 5) #adds only if the key isn't present
- .update({"four":4}) adds it or - dict1["four"] = 4 also adds it
- del dict1["one"]
- weird unpacking options(?) {'a': 1, **{'b': 2}}  # => {'a': 1, 'b': 2}

###### sets { } - immutable elements, no duplicates
- empty_set = set()
- filled_set = {1, 2, 2, 2, 3, 4} # filled_set = {1, 2, 3, 4}
- set_one & set_two # & gives a set of what they share
- | unifies (combines) 2 sets (remember, no duplicates)
- {1, 2, 3, 4} - {2, 3} = {1, 4}
- {1, 2, 3, 4} ^ {2, 3, 5}  # gives a set of what they don't share {1, 4, 5}
- {1, 2} >= {1, 2, 3} # False, if the left includes the whole right (if it's a superset)

###### misc
- no variable declarations, only assignments. Use lower_case_with_underscores





