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

A list comprehension consists of brackets containing an expression followed 
by a for clause, then zero or more for or if clauses. The result will be a
new list resulting from evaluating the expression in the context of the
for and if clauses which follow it. For example, this listcomp combines 
the elements of two lists if they are not equal:
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
    it's the same def fib(n) thing, written in e.g. fibo.py
    then import fibo in another file, then use fibo.fib(100)

- modules have their own private symbol table
 when a module is imported, Python sets globals()['__name__'] in this module to the module's name
    this lets you use "global variables" without fucking up
the rest of the future program
you can touch them at modname.itemname
    
    -run as script: python fibo.py <arguments>
add:
if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))
    #if run as a script, it'll be run as main.
    #if not a script, it wont run. Why?

importlib.reload(modulename) lets you reload the module again,
e.g. after it has been modified but without restarting the interpreter

import searches for built in module, then a .py in directories
given by variable sys.path (dir containing input script, PYTHONPATH...)

*precompiled modules (.pyc) load, but dont run faster

dir() lists the names a module defines - if no arg, then whats currently defined
"name" = variables, modules, functions etc. but not builtins (which are mostly errors, also list, hex, object, open...
access those with dir(builtins)

    Package
a package is a series of modules, instead of having to know each module namedyo
you use the same package.function to use them!
__init__.py #marks the directory as a package (can be empty)
however you can still e.g. sound.effects.echo and use a specific module

---
    input and output
f'blabla{year} {event}' will insert the variables year and EnvironmentError 
    called "formatted string literal", starts with f or F before quotes or triple quotation marks
str.format() also uses {} but you must give it the variables too:
    '{:-9} YES votes {:2.2%}'.format(yes_votes, percentage)
    #:-9 pads the input so it uses at least 9 characters
    #% tells python to use a decimal as a percentage, so .5 becomes 50%
    # the - minus sign means to only use it for negatives (which is the default?)
    # https://stackoverflow.com/questions/63806417/what-is-the-function-of-9-in-python
#underscores in an interget are ignored by the interpreter so
#123_456 is 123456 but easier to read!
    an integer after : makes the field a minimum number of characters wide
    !a applies ascii(), !s applies str() !r repr())
    the {} can be empty. Can use an int to refer to which of the variables
at the end they apply to:
    print('{1} and {0}'.format('spam', 'eggs')) #prints eggs and ham
    or you could do print("this {food}".format(food="corn"))

%d will truncate to integer, %s will maintain formatting, 
%f will print as float and %g is used for generic number
name ='giacomo'
number = 4.3
print('%s %s %d %f %g' % (name, number, number, number, number))
outputs giacomo 4.3 4 4.300000 4.3

print ('%s is %d years old' % ('Joe', 42))

    %s tells the formatter to call the str() function on the 
argument and since we are coercing to a string by definition,
 %s is essentially just performing str(arg).
    %d on the other hand, is calling int() on the
 argument before calling str(), like str(int(arg)), 
 This will cause int coercion as well as str coercion. 
>>> '%d' % 0x15 #hex to decimal
'21'

https://docs.python.org/3.7/library/string.html
:d makes a decimal, :x hex, :, seperates thousands with comma
:.2% gives percentage with 2 numbers past the decimal
e.g. print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))

file1.write("...{}...".format(blabla)) #for writing to a file

% modulo formats strings:
"string" % values - called string interpolation
print('The value of pi is approximately %5.3f.' % math.pi)
    prints 3.142
    cf "old string formating"

open("filename", "w")
    r only reads, w only writes (erases old file), a appends to end
r+ read and writes. r is assumed if unspecified.
b opens in binary mode, reading in byte objects - use for non-text filters
    in text mode, \n and \r\n (windows) are converted to just \name
and when writing back, they go back to platform specific versions.
This would corrupt a .exe or .jpg...
use filename.close() so the interpreter actually writes the stuff to the file

filename.seek(offset, whence) adds the offset to the reference point,
to get a new "cursor" position when reading a file (or readlines())
    in text files, only seeks relative to the beginning are allowed


JSON - json in std lib "serializes" (converts python data
 hyrachies like dictionaries into string representations),
 turning them back is "deserializing"
 json.dumps([1, "simple", list"])
json.dump(x, f) will read from f assuming f was = open("filename.txt")
x = json.load(f) 
    ***check docs, this is UnicodeTranslateError




------ errors and exceptions
e.g. in a while loop 
    try: #blabla, ends if an error occurs
    use except ValueError: # or (ValueError, RuntimeError):
        print("oops, that's not a valid number")
    #it will print if a ValueError comes up
    #if another exception, its "unhandled" and execution stops
    #last except clause may omit exception names as a wildcard
you can print:
    print("Unexpected error:", sys.exc_info()[0]) which would print
the exception to file or whatever...
After all excepts, you can use else:
    it executes if the try: doesnt raise exceptions!

raise NameError("hi") #forces an exception to occur

user defined exceptions !
    create a new exception classes

Class Error(Exception):
    """Base class"""
    passed
    
class InputError(Error):
    """exception raised for errors in the input.

    Attributes:
        expression -- input expression the error occured in
        message - explain error
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message= = message

clean up actions
    try statements' finally: clause executes no matter the circumstances
(executes right before a break, continue or return)

--- Classes! --- 

bundle data and functionality together. A class makes a new type of object,
so new instances of that type can be made. It has attributes to maintainits state.
And has methods to modify its state.
    class inheritence has base classes, derived classes can override
the base class(es) and can use its base class' methods

Objects are individuals, but multiple names can bind to one object. (aliasing)
    when dealing with mutable objects (lists, dicts...) names act like
pointers. Passing it only needs to pass the pointer!

scope rules, namespaces

namespace - maps names to objects. Mostly implemented as dictionaries.
    builtins, built in exceptions, global names in module, local names in a function invocation
    - names in different namespaces have no relation. each can have its own "max"

n.b. attribute = a name following a dot. in z.real, real is attribute

scope - textual region of program where namespace is accessible
accessible = referncing a name tries to find it in the namespace
    3-4 scopes:
    innermost (searched first) local names 
    scopes of enclosing functions - non local, but non global
    global names of current module
    outermost, built in names
if a name's declared global, it goes to the middle scope. nonlocal
can rebind names

module objects have a read only attribute __dict__ returning the
dict used to implement its namespace

assignments dont copy data, just bind names to objects.
del also only removes the binding (as reference by the local scope)
all operations introducing new names use the local, import binds to local

example:

def scope_test():
    def do_local():
        spam = "local spam"
    
    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("after local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("in global scope:", spam)

result:
after local assignment: test spam
After nonlocal assignment: nonlocal spam
After global assignment: nonlocal spam #it is in the function, so doesnt use globals...
In global scope: global spam

    Classes
entering class definition, creates new namespace, used as localswhenn
when class ef ends, a class object's created (wrapping the namespace contents)
the original local scope (from before class definition) returns
with the class object bound to the classname

class objects have 2 operations: attribute reference, instantiation
    attribute references are obj.name (classname.variableorfunctionname)
    instantiation uses function notation x = classname()

def __init__(self, data): #makes the class do something when instantiated
    self.r = data

x = classname(5)
print(x.r)
    gives 5

functions in a class are called method
variables in a class are called attributes/instance variables

instance objects - only accept attribute references.
    2 kinds of attribute names - data attributes and Methods
    data attributes = instance variables

the key difference between a function and a class method.
 A function is floating free, unencumbered. A class (instance) 
 method has to be aware of it's parent (and parent properties) 
 so you need to pass the method a reference to the parent class 
 (as self). It's just one less implicit rule that you have to 
 internalize before understanding OOP. Other languages choose 
 syntactic sugar over semantic simplicity, python isn't other languages. 

self in a class refers to this instance. So you need the functions etc. to 
refer to their instance.
    The instance a method belongs to is passed automatically, but not received.
     So the first parameter of a method is the instance the method is called
      on. This makes methods and functions the same - but you use them differently.
Self comes from smalltalk and modula-3 conventions, but "this" could be clearer

### if ClassA has methodA, defined as:
def methodA(self, arg1, arg2):
    if ObjectA is an instance of this class and you call methodA on ObjectA:
    ObjectA.methodA(arg1, arg2) # python will automatically convert it to:
    ClassA.methodA(ObjectA, arg1, arg2) #<- see? self is the... instance!

a method can call another method using self:
class Bag:
    def __init__(self):
        self.data = []
    
    def add(self, x):
        self.data.append(x)
    
    def addtwice(self, x):
        self.add(x)
        self.add(x)


method objects


p.g. 82 - method objects, function objects etc... are these differences important?
    return later ???






converting a list of ints into a string is difficult!
    output = "".join([str(num) for num in output])
            use map()
    final_str = delimiter.join(map(str, mix_list))
    therefore: output ="".join(map(str, output))
    

---    inheritence ---
class DerivedClassName(BaseClassName): #but other expressions are allowed 
    e.g. modname.BaseClassName

class DerivedClassName(BaseClass1, BaseClass2, BaseClass3): #multiple inheritance!
    #if e.g. method names are shared in all, the first one mentioned has precedence

Varuables starting with an underscore aren't part of APIs, they're subject to
change without notice



Vocab:

    namespace - maps names to object, it's a dictionary
    nested scope / scope ? 
    
    object
    class variable
    class object - 2 ops, attribute ref, instantiation
    class methods
    
    module object - have a __dict__ attribute returning the dict implementing its namespace

    method - function defined in a class body





------------
------------
----------

    tour of standard library
os.get.cwd() - gets current working directory
os.chdir("/server/accesslogs") - changes current directory
os.system("mkdir today") - runs mkdir in the system shell

shutil.copyfile("data.txt", /file/data.txt")
shutil.move("/build/executables", "installdir") # I guess copyfile cant go backwards?

glob.glob("*.py") - lets you do wildcard searchers

re.findall(r"\bf[a-z]*", "which foot or hand fell fastest") #gives list of words in f-
re.sub(r" (\b[a-z]+) \1", r"\1", "cat in the the hat") #gives 1 string without 2nd the
"tea for too".replace("too", "two")
    math gives access to C functions for floating point path
math.cos(math.pi/4) #gives cos...
math.log(1024, 2) #gives 10.0

random.choice(["apple", "pear", "bannana"])
random.sample(range(100), 10) #gives 10 random numbers in range(100)
random.random() #random float e.g. .173423432
random.randrange(6) #random int in range (6)

statistics.mean(data) #gives the mean of some list
.median()
.variance()

urllib.request.urlopen("http:.... .com") as response:
    for line in response:
        line = line.decode("utf-8") #decodes binary to text
        if "EST" in line or "EDT" in line: #look for Eastern Time
            print(line)

server = smtplib.SMTP("localhost")
server.sendmail("blabla@gmail.com", "caeser@gmail.com", "Hey man, what's up?") #sends from to
    #needs mailserver running on localhost

date.today()
now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")
    date can do calender math!
birthday = date(1964, 7, 31)
age = date.today() - birthday
age.days #gives the number of days...

zlib, gzip, bz2,lzma, zipfile and tarfile
s = b"witch which has..."
t = zlib.compress(s)
zlib.decompress(t)

Timer('a,b = b,a', 'a=1; b=2').timeit() #times a function, for speed testing!
    profile and pstats have similar tools

doctest #scans a module, validates tests in its docstrings

def average(values):
    """Computes the arithmetic mean of a list of ints

    >>> print(average([20, 30, 70]))
    40.0
    """
    return sum(values) / len(values)

doctest.testmod() #validates the embedded tests
unittest lets you maintain tests ina  separate file

xmlrpc.client and xmlrpc.server

email builds and decodes messages w/ attachments, header protocols etc.
    smtplib and poplib actually send and receive the messages

json
sqlite3 wraps SQLite database library

    multithreading: #can run tasks while others wait for user input...
threading 

logging.debug("Deubbing info") #sends log messages to a file or sys.stderr
.info #defaults as standard error
.warning #
.error
.critical

array.array() #makes an array which can only hold 1 data type, but
    at 2 bytes per entry, a python list uses 16 bytes per entry!
collections.deque() #makes a list with faster appends and pops on both sides
    but slower to look up the middle
