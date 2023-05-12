# Course-Udemy-100DaysofCode-TheCompletePythonProBootcamp-2023
some exercises and 100 python projects in 100 Days of Code: The Complete Python Pro Bootcamp for 2023

# note
# **syntax**

# variables and string

```python
# 输出
print()
# string
print("Hello" + "Agela")
# 换行符 \n
print("Hello\nWorld~")
'''Hello
World~'''
# error
IndentationError
SyntaxError
NameError
......
# 输入
name = input("What is your name? ")
# variable
# exercise : switch the values of 2 variables
# name rule: real meaning \ _connection \ not use number begin
# data type \ operation
string \ integer \ float \ boolean
subscript
calculation ： + - * / ** // () Pemdaslr......
# 保留小数
round(a，2) # 保留几位小数,会将小数末尾的0舍去
'{:.2f}'.format(a) # 保留2位小数
'%.2f' % a # 保留2位小数
# type conversion
str()
int() # operation// always gets this type
float() # operation/ always gets the type
a=4
a/=2
a/=2 
print(a) # 1.0
print(type(a)) # <class 'float'>
# f-strings : do not need to converse the type
score = 5
height = 1.63
isWinning = True
print(f"your score is {score},your height is {height}, you are wining is {isWinning}")

# conditinal statements
# multiple if statement in succession

# logical operators
and
or
not

# code blocks and scope
# change local variable into global variable
def foo():
    global x
    x = 10
foo()
print(x)
# Note that it is generally not recommended to use global variables unless necessary, as they can make the code more difficult to understand and maintain. 
# Instead, it is usually better to pass variables as arguments to functions or return them as results.
```

## Count the number of occurrences of a character in a string

```python
# Count the number of occurrences of a character in a string
sentence = 'Mary had a little lamb'
sentence.count('a')
# 4

list=("Angela, Ben, Jenny, Michael, Chloe")
list = list.split()
len = len(list)
print(list)
print(len)
# ['Angela,', 'Ben,', 'Jenny,', 'Michael,', 'Chloe']
# 5
```

## lowercase a string

```python
# lowercase a string in Python
"Kilometer".lower()

# capitalize()将字符串的第一个字母变成大写,其他字母变小写
```

## docstrings

```python
def days_in_month(year,month):
    '''what we use this function to do?......sothing like that''' # docstrings
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
    year = is_leap(year)
    if month > 12 or month < 1:
    	return "Invalid month entered."
    if year=="Leap year." and month==2:
         return 29
    return month_days[month-1]
```

 random and list

## random

```python
# random()
# https://www.askpython.com/python-modules/python-random-module-generate-random-numbers-sequences

# random Module Methods
random.seed() # This seed value determines the output of a random number generator, so if it remains the same, the output also remains the same.
getstate() # returns an object containing the current state of the generator
setstate(state_obj) # restores the state of the generator at the point when getstate() was called, by passing the state object
getrandbits(k) # returns a Python integer with k random bits
>>> random.getrandbits(100) # Get a random integer having 100 bits
802952130840845478288641107953

# Generate Random Integers
random.randrange(start, stop, step) 
random.randint(a, b) # include a and b 

# Generating Random floating point numbers
random.random() # Returns the next random floating point number between [0.0 to 1.0)
random.uniform(a, b) # Returns a random floating point N such that a <= N <= b if a <= b and b <= N <= a if b < a.
random.expovariate(lambda) # Returns a number corresponding to an exponential distribution.
random.gauss(mu, sigma) # Returns a number corresponding to a gaussian distribution.

# Random Sequences
random.shuffle(x) # shuffle the sequence in place. A sequence can be any list/tuple containing elements.
random.choice(seq) # you would want to randomly pick up an item from a List/sequence.
random.sample(population, k) # Returns a random sample from a sequence of length k.
```

```python
import random
 
random.seed(1)
 
# Get the state of the generator
state = random.getstate()
 
print('Generating a random sequence of 3 integers...')
for i in range(3):
    print(random.randint(1, 1000))
 
# Restore the state to a point before the sequence was generated
random.setstate(state)
print('Generating the same identical sequence of 3 integers...')
for i in range(3):
    print(random.randint(1, 1000))
```

> Possible Output: 
>
> Generating a random sequence of 3 integers...
> 138
> 583
> 868
> Generating the same identical sequence of 3 integers...
> 138
> 583
> 868

```python
import random
 
i = 100
j = 20e7
 
# Generates a random number between i and j
a = random.randrange(i, j)
try:
    b = random.randrange(j, i)
except ValueError:
    print('ValueError on randrange() since start > stop')
 
c = random.randint(100, 200)
try:
    d = random.randint(200, 100)
except ValueError:
    print('ValueError on randint() since 200 > 100')
 
print('i =', i, ' and j =', j)
print('randrange() generated number:', a)
print('randint() generated number:', c)
```

>**Possible Output :**
>
>ValueError on randrange() since start > stop
>ValueError on randint() since 200 > 100
>i = 100  and j = 200000000.0
>randrange() generated number: 143577043
>randint() generated number: 170

```python
import random
print('Random number from 0 to 1 :', random.random())
print('Uniform Distribution between [1,5] :', random.uniform(1, 5))
print('Gaussian Distribution with mean = 0 and standard deviation = 1 :', random.gauss(0, 1))
print('Exponential Distribution with lambda = 0.1 :', random.expovariate(0.1))
print('Normal Distribution with mean = 1 and standard deviation = 2:', random.normalvariate(1, 5))
```

>**Possible Output** :
>Random number from 0 to 1 : 0.44663645835100585
>Uniform Distribution between [1,5] : 3.65657099941547
>Gaussian Distribution with mean = 0 and standard deviation = 1 : -2.271813609629832
>Exponential Distribution with lambda = 0.1 : 12.64275539117617
>Normal Distribution with mean = 1 and standard deviation = 2 : 4.2590371195111757

```python
import random
sequence = [random.randint(0, i) for i in range(10)]
print('Before shuffling', sequence)
random.shuffle(sequence)
print('After shuffling', sequence)

# pay attention to this: To print the shuffled list, you should directly print the sequence list after calling the shuffle() method
sequence = ["abc","def","ghi","jkl","mln","opq","rst","uvw"]
random.shuffle(sequence)
print(sequence)

d = ['one', 'eleven', 'twelve', 'five', 'six', 'ten']
print(d)
for i in range(5):
    print(random.choice(d))
    
a = ['one', 'eleven', 'twelve', 'five', 'six', 'ten']
print(a)
for i in range(3):
    b = random.sample(a, 2)
    print('random sample:', b)
```

>**output :** 
>
>Before shuffling [0, 0, 2, 0, 4, 5, 5, 0, 1, 9]
>After shuffling [5, 0, 9, 1, 5, 0, 4, 2, 0, 0]
>
>['one', 'eleven', 'twelve', 'five', 'six', 'ten']
>ten
>eleven
>six
>twelve
>twelve
>
>['one', 'eleven', 'twelve', 'five', 'six', 'ten']
>random sample: ['five', 'twelve']
>random sample: ['ten', 'six']
>random sample: ['eleven', 'one']

## change the line when print

```python
print("Hello", end="")
print("World")
# HelloWorld

print("Hello\nWorld")
# Hello
# World

print("abc\n")

a = 123456
print(str(a) + "\n")
# \n 必须在“”内部，而且文字必须是string类型
```

## data structure

 a way of organizing and storing data 

> list [ ] (order / [-1] from the end of the variable / )
>
> iterable (Examples of iterables include lists, tuples, strings, dictionaries, sets, and ranges. )

### stake

In computer science, a stack is a data structure that stores a collection of elements, and provides two primary operations: `push`, which adds an element to the top of the stack, and `pop`, which removes the top element from the stack.

A stack can be thought of as a container that holds a set of items, arranged in a specific order. The order is determined by the rules of the stack, which dictate that items can only be added to or removed from the top of the stack.

Stacks follow the "Last-In, First-Out" (LIFO) principle, which means that the last item added to the stack is the first item to be removed. This makes stacks useful for tasks that require processing items in reverse order, such as undoing actions in a software application, evaluating expressions in a programming language, or tracking the call stack of a running program.

In addition to the `push` and `pop` operations, stacks often provide other useful methods, such as `peek`, which returns the value of the top element without removing it, and `isEmpty`, which checks whether the stack is currently empty.

Stacks can be implemented using a variety of underlying data structures, such as arrays, linked lists, or dynamic arrays, and are widely used in computer science and software engineering for a variety of applications.

### Queues

In computer science, a queue is a data structure that stores a collection of elements and provides two primary operations: `enqueue`, which adds an element to the back of the queue, and `dequeue`, which removes the front element from the queue.

A queue can be thought of as a container that holds a set of items, arranged in a specific order. The order is determined by the rules of the queue, which dictate that items can only be added to the back of the queue and removed from the front of the queue.

Queues follow the "First-In, First-Out" (FIFO) principle, which means that the first item added to the queue is the first item to be removed. This makes queues useful for tasks that require processing items in the order they were added, such as handling requests in a web server or managing tasks in a background job queue.

In addition to the `enqueue` and `dequeue` operations, queues often provide other useful methods, such as `peek`, which returns the value of the front element without removing it, and `isEmpty`, which checks whether the queue is currently empty.

Queues can be implemented using a variety of underlying data structures, such as arrays, linked lists, or dynamic arrays, and are widely used in computer science and software engineering for a variety of applications.















## functions about list

```python
list[1:-1] # 列出 Slice
list.append(x) # Add an item to the end of the list.
list.extend(iterable) # Extend the list by appending all the items from the iterable. Equivalent to a[len(a):] = iterable.
list.insert(i, x) # Insert an item at a given position. The first argument is the index of the element before which to insert
list.remove(x) # Remove the first item from the list whose value is equal to x. It raises a ValueError if there is no such item.
list.pop([i]) # Remove the item at the given position in the list, and return it. If no index is specified, a.pop() removes and returns the last item in the list.
list.clear() # Remove all items from the list.
list.index(x[, start[, end]]) # Return zero-based index in the list of the first item whose value is equal to x. Raises a ValueError if there is no such item.The optional arguments start and end are interpreted as in the slice notation and are used to limit the search to a particular subsequence of the list. The returned index is computed relative to the beginning of the full sequence rather than the start argument.
list.count(x) # Return the number of times x appears in the list.
list.sort(*, key=None, reverse=False) # Sort the items of the list in place (the arguments can be used for sort customization, see sorted() for their explanation).
list.reverse() # Reverse the elements of the list in place.
list.copy() # Return a shallow copy of the list.

# You might have noticed that methods like insert, remove or sort that only modify the list have no return value printed – they return the default None. 1 This is a design principle for all mutable data structures in Python

# Another thing you might notice is that not all data can be sorted or compared. For instance, [None, 'hello', 10] doesn’t sort because integers can’t be compared to strings and None can’t be compared to other types. Also, there are some types that don’t have a defined ordering relation. For example, 3+4j < 5+7j isn’t a valid comparison.

# using Lists as Stacks
stack = [3, 4, 5]
stack.append(6)
stack.pop()

# Using Lists as Queues : While appends and pops from the end of list are fast, doing inserts or pops from the beginning of a list is slow (because all of the other elements have to be shifted by one).
from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")   # Terry arrives
queue.append("Graham")  # Graham arrives
queue.popleft()  # The first to arrive now leaves
# 'Eric'
queue.popleft()  # The second to arrive now leaves
# 'John'
queue   # Remaining queue in order of arrival
# deque(['Michael', 'Terry', 'Graham'])
```

```python
# list.extend(iterable)
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
print(list1)
# [1, 2, 3, 4, 5, 6]
list1 = ['a', 'b', 'c']
string1 = 'def'
list1.extend(string1)
print(list1)
# ['a', 'b', 'c', 'd', 'e', 'f']
```

##  splits the string into a list

```python
names_string = input("Give me everybody's names, separated by a comma. ")
# Angela, Ben, Jenny, Michael, Chloe
names = names_string.split(", ")

# another way
my_string = "Hello, world!"
my_list = list(my_string)
print(my_list)
```

## IndexError

`IndexError` is a built-in exception in Python that is raised when an index is out of range of a sequence (such as a list, tuple, or string). 

In this case, `my_list` contains three elements, with indices 0, 1, and 2. The expression `my_list[3]` attempts to access the element at index 3, which is outside the range of the list. This will raise an `IndexError`, since there is no element at that index.

`IndexError` can also be raised in other situations where an index is used incorrectly, such as when slicing a sequence with indices that are out of range, or when attempting to remove an element from an empty list.

When an `IndexError` is raised, the Python interpreter will print a traceback that shows the line of code that caused the error, along with the type of the error and a description of the problem. This can be useful for debugging your code and identifying where the error occurred.

## nested list



# loop and function

## 四舍五入/舍去/求和/最大/最小

```python
int()
round()
sum()
max()
min()
```

## for in lists/range

```python
list = [1,2,3,4,5,6]
for i in list:
	print(i)
    
range(a,b,gap)
```

## string切片/string去掉特定字符/list合并/list变string

```python
def func(con):
    con=str(con)
    con=con[1:len(con)-1] # 切片
    char="',]["           # 去掉特定字符
    for c in char:
    	con = con.replace(c, "")
        
# list合并：直接相加
final = letter+symbol+number

# list变string
final_str="".join(final)
```

## build-in functions

https://docs.python.org/3/library/functions.html

## use for loop in the list

```python
# the first way
chosen_word = "hello"
guess = "l"
if guess in chosen_word:
    print("Yes, the letter is in the chosen word")
else:
    print("No, the letter is not in the chosen word")

# the second way
import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
guess = input("Guess a letter: ").lower()
for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")
        
# *for* 结构 for var in list 可让您轻松查看列表（或其他集合）中的每个元素。
# 在迭代期间，不要在列表中添加或移除。

# 使用 *in* 构造可轻松测试元素是否显示在列表（或其他集合）中 (value in collection)，用于测试该值是否在集合中，并返回 True/False。
list = ['larry', 'curly', 'moe']
if 'curly' in list:
    print('yay')
```

## clear the screen

```python
from replit import clear
clear()
```

## arguments / parameters / inputs / outputs

```python
# 在调用函数之前，必须先传入参数值
def BMI(height, weight):
    print("Hello, I will calculate your BMI.")
    BMI = float(weight) / float(height) ** 2
    BMI = round(BMI, 1)
    print("Your BMI is: " + str(BMI))
height = input("What is your height? ")
weight = input("What is your weight? ")
BMI(height, weight)

def BMI(height,weight):
    print("Hello, I will calculate your BMI.")
    bmi=weight/ height**2
    bmi='%.1f' % bmi
    print("Your BMI is:" + str(bmi))
BMI(1.61,70.0)
```

 An **argument** is referred to the **value**s that are **pass**ed within a function when the function **is called**.  The type of the values passed in the function is the same as that of the variables defined in the function definition. These are also called **Actual arguments** or **Actual Parameters**. 

 The **parameter** is referred to as the **variable**s that are **define**d during a function **declaration or definition**.  These variables are used to receive the arguments that are passed during a function call.  These are also called **Formal arguments** or **Formal Parameters**. 

```python
# function with output
def concatenate(f_name,l_name):
    name = f_name.title()+" "+l_name.title()
    return name
	#another way: return f"{name}" 
print(concatenate("CHICHI","ZHANG"))

# multiple return values
# return tells the computer this is the end of the function
def format_name(f_name, l_name):
	if f_name == "" or l_name == "":
		return "You didn't provide valid inputs."
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"Result: {formated_f_name} {formated_l_name}"
formatted_name = format_name(input("Your first name: "), input("Your last name: "))
print(formatted_name)
```

> **why we use return ,not print() ?**
>
> return can pass easily; print() ask us to create variable to save and then pass

## positional & keyword argument

## change a decimal number into a whole number

```python
import math
number_of_cans = math.ceil(area/cover)
```

## find the index of a item in a list

```python
fruits = ['apple', 'banana', 'cherry']
x = fruits.index("cherry")
```

##  end the function directly 

```python
# use the return statement to end a function directly.
def my_function(x):
    if x < 0:
        return "Error: x should be non-negative"
    else:
        return x ** 2
```







# dictionaries & nesting

```python
# dictionaries : each key has one value
dictionary = {key:value,"key":"value",key:value}
dictionary["key"] # "value"
dictionary["loop"] = "definition of loop" # add an item
dictionary["key"] = "definition of key" # edit an item
# loop through a dictionary
for key in dictionary:
    print(key)
    print(dictionary[key])
```

```python
# nesting
capitals = {
    "France" : "Paris",
    "Germany" : "Berlin"
}
# nesting a list in a dictionary
travel_log = {
    "France" : ["Paris","Lille","Dijon"]
    "Germany" : ["Berlin","Hamburg","Stuttgart"]
}
# nesting a list in a list
["A","B","C",["D","E"]]
# nesting a dictionary in a dictionary
travel_log = {
    "France" :{"city_visited":["Paris","Lille","Dijon"],"total_visits":12 }
    "Germany" : {"city_visited":["Berlin","Hamburg","Stuttgart"],"total_visits":5}
}
# nesting a dictionary in a list
travel_log =[
    {
        "country":"France" ,
        "city_visited":["Paris","Lille","Dijon"],
        "total_visits":12 
    }
    {
        "country":"Germany" , 
        "city_visited":["Berlin","Hamburg","Stuttgart"],
        "total_visits":5
    }
]
```



# scope

## local VS global 

```python
enemies = 1

def increase_enemies():
    enemies = "Zombies"
    print(f"enemies inside function: {enemies}")
    
def increase_enemies1():
    global enemies
    enemies += "Zombies"
    print(f"enemies inside function: {enemies}")
    
increase_enemies()
increase_enemies1()
print(f"enemies outside function: {enemies}")
```

## constants and global scope

we always use global especially when we define a constant

constant name : upper case

# debug : find and fix the error

## find

1.describe the problem : run the code block by block

2.reproduce the bug : 遍历所有情况

3.evaluate the code line by line : check if we miss something or the logic is right

## fix

1.check the result and watch for red underlines

2.print() can help to debug : if the result can be print correctly

3.using a debugger

4.**take a break** and then find + fix it

5.let a friend to look over your code

6.run often : write and run the code at any time

7.ask StackOverflow : https://stackoverflow.com/questions/tagged/python





