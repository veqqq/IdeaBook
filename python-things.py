def fib(n):
    """Print Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n;
        print(a, end=' ")
        result.append(a)
        a, b= b, a+b
    return result

The execution of a function introduces a new symbol table used for the local variables of the function. More precisely, all
variable assignments in a function store the value in the local symbol table; whereas variable references first look in the
local symbol table, then in the local symbol tables of enclosing functions, then in the global symbol table, and finally in
the table of built-in names. Thus, global variables and variables of enclosing functions cannot be directly assigned a value
within a function (unless, for global variables, named in a global statement, or, for variables of enclosing functions,
named in a nonlocal statement), although they may be referenced.


The statement result.append(a) calls a method of the list object result. A method is a function that
‘belongs’ to an object and is named obj.methodname, where obj is some object (this may be an expression),
and methodname is the name of a method that is defined by the object’s type. Different types define different
methods. Methods of different types may have the same name without causing ambiguity. (It is possible to define
your own object types and methods, using classes, see Classes) The method append() shown in the example is
defined for list objects; it adds a new element at the end of the list. In this example it is equivalent to result =
result + [a], but more efficient.



def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
            if ok in ('y', 'ye', 'yes'):
        return True
            if ok in ('n', 'no', 'nop', 'nope'):
        return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

A defined function's default value's only evaluated once. So:
def f(a, L=[]):
L.append(a)
return L
if you call it 3 times, 1, 2, then 3. It will give 1, 1 2. 1 2 3 So to make it truly restart each time:
def f(a, L=None):
if L is None:
L = []
L.append(a)
return L

Functions can be called with (optional!) keyword arguments (kwarg=value)
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")
State, action and type are optional. You can call it in many ways:
parrot(voltage=1000000, action='VOOOOOM')
parrot(1000)
parrot('a million', 'bereft of life', 'jump') # positional arguments

Not possible:   
parrot()    #required argument missing
parrot(voltage=5.0, 'dead') #non-keyword argument after a keyword argument
parrot(110, voltage=220) #duplicate value for the sa
parrot(actor='John Cleese') # unknown keyword argument

In a function call, keyword arguments must follow positional arguments. All the keyword arguments passed must match
one of the arguments accepted by the function (e.g. actor is not a valid argument for the parrot function), and their
order is not important. This also includes non-optional arguments (e.g. parrot(voltage=1000) is valid too). No
argument may receive a value more than once.



When a final formal parameter of the form **name is present, it receives a dictionary (see typesmapping) containing all
keyword arguments except for those corresponding to a formal parameter. This may be combined with a formal parameter
of the form *name (described in the next subsection) which receives a tuple containing the positional arguments beyond
the formal parameter list. (*name must occur before **name.)
def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

#Call:
cheeseshop("Limburger", "It's very runny, sir.",
    "It's really very, VERY runny, sir.",
    shopkeeper="Michael Palin",
    client="John Cleese",
    sketch="Cheese Shop Sketch")

Order of arguments: 
def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
      ----------     ----------    - --------
        |               |               |
        |           position/keyword    |
        |                           keyword only
        positional only
where / and * are optional.
    
def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only

Looking at this in a bit more detail, it is possible to mark certain parameters as positional-only. If positional-only, the
parameters’ order matters, and the parameters cannot be passed by keyword. Positional-only parameters are placed before
a / (forward-slash). The / is used to logically separate the positional-only paramet

def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
As guidance:
    • Use positional-only if you want the name of the parameters to not be available to the user. This is useful when
parameter names have no real meaning, if you want to enforce the order of the arguments when the function is
called or if you need to take some positional parameters and arbitrary keywords.
    • Use keyword-only when names have meaning and the function definition is more understandable by being explicit
with names or you want to prevent users relying on the position of the argument being passed.
    • For an API, use positional-only to prevent breaking API changes if the parameter’s name is modified in the future.

    lambda expressions



----- lists ---
    All methods start with list.
    - .append() add to end of list
    - .extend(iterable) appends all items of iterable
    - .insert(i,x) at index add x (0, x) is at the front
                        .insert(len(a), x) is .append(x)
    - .remove(x) remove first thing matching x's value
                                ValueError if none
    - .pop([i]) remove whats at this index, if not specified, the last one
    - .clear() empties list a la del a[:]
    - .index(x[, start[, end]]) return index of 1st item = to x ([within a specific slice]
    - .count(x) how many times is x present
    - .sort(*, key=None, reverse=False) sorts...
        - integers can't be compared to strings or None
    - .reverse()
    - .copy() - make shallow copy = [:]


Use lists as stacks (last in, first out)

Dont use lists as queues (first in, first out) because its inefficent,
everything has to be shifted for that... Use collections.deque for that.

list comprehensions
squares=[]
for x in range(10):
    squares.append(x**2)

squares = list(map(lambda x: x**2, range(10)))

squares = [x**2 for x in range(10)]

A list comprehension consists of brackets containing an expression followed by a for clause, then zero or more for or
if clauses. The result will be a new list resulting from evaluating the expression in the context of the for and if clauses
which follow it. For example, this listcomp combines the elements of two lists if they are not equal:
>>> [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
    is the same as:
combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs.append((x, y))

vec = [-4, -2, 0, 2, 4]
[x*2 for x in vec] #makes new list with values doubled
[x for x in vec if x >= 0] #filters list, excluding negatives
[abs(x) for x in vec] #applies function to elements
[(x, x**2) for x in range(6)] #makes list of tuple pairs, note the parenthesis
vec = [[1,2,3], [4,5,6], [7,8,9]]
[num for elem in vec for num in elem] #flattens the list using 2 fors
[str(round(pi, i)) for i in range(1, 6)]
['3.1', '3.14', '3.142', '3.1416', '3.14159']


The initial expression in a list comprehension can be any arbitrary expression, including another list comprehension.

Matrix = [
    [1, 2, 3, 4]
    [5, 6, 7, 8]
    [9, 10, 11, 12]
]
[[row[i] for row in matrix] for i in range(4)] #transposes rows and columns

    same as:
transposed=[]
for i in range(4):
    transposed.append([row[i] for row in matrix])

    same as:

for i in range(4):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)

actually list(zip(*matrix)) would do it too!
    in function calls, use * to unpack arguments from list or tupple,
        from dicts with **

lists, strings and tupples are "sequence data types"
    tuples cant be modified, but things in them can be (e.g. a list in it)
    Use tuples for hetereogeneous elements accessed by unpacking or indexing
    -because it's faster

sets - unordered with no duplicates (use for memberships or authentication?)

dictionary - (in other languages = associative arrays), use keys  not sequences for indexing - tuples, strings and numbers can be keys (immutable)
    list(d) returns a list of the keys in a dictionary, by insertio order (or use sorted(d) for a sorted list)

{x: x**2 for x in (2, 4, 6)}
dict(sape=4139, guido=4127, jack=4098) <- dict is a function like str() easier to type as no " "


items() returns key and corresponding value at same time
for k, v in knights.items():
    print(k, v) #prints them next to each other

zip() lets you loop over multiple sequences at once
for q, a in zip(questions, answers):
    print('What is your {0}? It is {1}.'.format(q, a))

for f in sorted(set(nameofvariable)):
    is a good way to list elements alphabetically withot copies


comparisons < > have lower priority than +* etc., and or not have even lower priority

and & or will stop if true, a and b and c will stop at b, if a and b is already true.

:= is uses within expressions (walrus operator) to assign variables (c uses == )

module = scripts in another file you want to call
you import them into "main" (the script you are calling them from)

pg. 51 of python tutorial in downloaded docs



















