##COMMENTS
# This is a one-line Python comment - code blocks are so useful!
"""This type of comment is used to document the purpose of functions and classes."""

##DECLARING/INITIALIZING
# Remember values, not variables, have data types.
# A variable can be reassigned to contain a different data type.
answer = 42
answer = "The answer is 42."

##DATA TYPES
boolean = True
number = 1.1
string = "Strings can be declared with single or double quotes."
list = ["Lists can have", 1, 2, 3, 4, "or more types together!"]
tuple = ("Tuples", "can have", "more than", 2, "elements!")
dictionary = {'one': 1, 'two': 2, 'three': 3}
variable_with_zero_data = None

##SIMPLE LOGGING
#Difference: Python 2 print "Printed!" works
print("Printed!") #Python 3 version with parentheses '()' 
##Take note of this difference and make note which version you are working with
##This environment is Python 3.6 (>3)

##CONDITIONALS
def should_i_eat(cake):
    if cake == "delicious":
        return "Yes please!"
    elif cake == "okay":
        return "I'll have a small piece."
    else:
        return "No, thank you."
print(should_i_eat("bad cake"))

##LOOPS
new_list = [1,2,3] ##In declaration, don't use list(). You can either
##place list = it on the LHS or list() on the RHS. list() is the default
##constructor.
for item in new_list:
    print(item) 

i = 0
total = 0
values = [10,20,30,40,50,60,70,80,90,100]
max_val = 50
while (total < max_val):
    total += values[i]
    i += 2

##FUNCTIONS
def divide(dividend, divisor):
    quotient = dividend / divisor
    remainder = dividend % divisor
    return quotient, remainder

def calculate_stuff(x, y):
    (q, r) = divide(x,y)
    print(q, r)
    
##CLASSES 
class Person(object):
    def __init__(self, name, age): ##the use of self is pretty iconic. (__:double under dash)
        self.name = name
        self.age = age 

    def birthday(self):
        self.age += 1
        
##EFFICIENCY -> time and space complexity

##Time complexity in Big Oh Notation
##O(n) is called linear time and happens often when you use a single loop.
##Always think like: "Some number of computations must be performed for
##EACH letter in the input."
##When we discuss efficiency, we take worst case for upper bound.
##O(29n+3) = O(16n+3) = O(n) APPROXIMATIONS
##When you approximate, always talk about in which case you are approximating.
##You will want to generally approximate for the worst case.

##Space complexity ALSO in Big Oh Notation.
##If you have to copy over your input string 3 times in your code,
##the space efficiency will be O(3n).

#TIME COMPLEXITY EXERCISE -> used approximations whenever possible.
"""input manatees: a list of "manatees", where one manatee is represented by a dictionary
a single manatee has properties like "name", "age", et cetera
n = the number of elements in "manatees"
m = the number of properties per "manatee" (i.e. the number of keys in a manatee dictionary)"""

manatees = []
#RUNS IN O(n)
def example1(manatees):
    for manatee in manatees:
        print(manatee['name'])

#RUNS IN O(1)
def example2(manatees):
    print(manatees[0]['name'])
    print(manatees[0]['age'])

def example3(manatees):
    for manatee in manatees:
        for manatee_property in manatee:
            print(manatee_property, ": ", manatee[manatee_property])

def example4(manatees):
    oldest_manatee = "No manatees here!"
    for manatee1 in manatees:
        for manatee2 in manatees:
            if manatee1['age'] < manatee2['age']:
                oldest_manatee = manatee2['name']
            else:
                oldest_manatee = manatee1['name']
    print(oldest_manatee)
    
##Although len() surely does some more background work, Python
##has really great built in functions like that which takes constant
##time meaning O(1). Normally, you would have to iterate over each 
##element which would give you O(n), BUT WITH PYTHON LEN() IS O(1).