# DICTIONARIES

# Dictionary = map = data structure with key-value pairs.
# An array is a list-based structure whereas a map is a set-based structure.
# In a dictionary/map, a group of keys is a set. A set is unordered.
# The keys in a map has to be unique. Sets do not allow repeated elements!

# Example: get n maximum elements from dictionary
a = {'a':100, 'b':40, 'c':66, 'd':77, 'e':99, 'f':33}
b = sorted(a, key=a.get, reverse=True) ##reverse=True for descending, False for ascending order
max_dict = {}

# Remember that b is ONLY ['a', 'e', 'd', 'c', 'b', 'f'] at this point. (without values)

# For 3 maximum entries.
for key in b[:3]:
    print(key)
    max_dict[key] = a[key]
    
print(max_dict)

# LISTS INDEXING & SLICING

a = ["a", "b", "c", "d", "e"]
start = 0
end = len(a) - 1
step = 1 # by default

a[start:end] # items start through end-1
a[start:] # items start through the rest of the array
a[:end] # items form the beginning through end-1
a[:] # a copy of the whole array

a[start:end:step] # start through not past end, by step

a[-1] # last item in the array
a[-2:] # last two items in the array (-2, -1) +1
a[:-2] # everything except the last two items (-5, -4, -3) +1

a[::-1] # all items in the array, reversed (-1, -2, -3, -4, -5) -1
a[1::-1] # the first two items, reversed (1, 0) -1
a[:-3:-1] # the last two items, reversed (-1, -2) -1
a[-3::-1] # everything except the last two items, reversed (-3, -4, -5) -1

b = ["a"]
b[:-2] # we will get a empty list instead of an error

# SAMPLE DICTIONARY INITIALIZING, ACCESSING, AND UPDATING:

udacity = {}
udacity['u'] = 1
udacity['d'] = 2
udacity['a'] = 3
udacity['c'] = 4
udacity['i'] = 5
udacity['t'] = 6
udacity['y'] = 7
udacity[5] = 555 # can have ints as dictionary keys as well

print(udacity)
# {'u': 1, 'd': 2, 'a': 3, 'c': 4, 'i': 5, 't': 6, 'y': 7}

print(udacity['t'])
# 6

# Dictionaries are very flexible! Multiple object types can be included.

dictionary = {}
dictionary['d'] = 1 #integer
dictionary['i'] = [2] #list
dictionary['c'] = [3]
dictionary['t'] = [4]
dictionary['i'].append(5)
dictionary['o'] = [6]
dictionary['n'] = [7]
dictionary['a'] = [8]
dictionary['r'] = [9]
dictionary['y'] = [10]

print(dictionary)
# {'d': [1], 'i': [2, 5], 'c': [3], 't': [4], 'o': [6], 'n': [7], 'a': [8], 'r': [9], 'y':[10]}

locations = {'North America': {'USA': ['Mountain View']}}
locations['North America']['USA'].append('Atlanta')
locations['Asia'] = {'India': ['Bangalore']}
locations['Asia']['China'] = ['Shanghai']
locations['Africa'] = {'Egypt': ['Cairo']}

print(locations.items()) #In Python 3, iteritems() is gone and now life is much easier!
print(locations.keys())
print(locations.values()) 

usa_sorted = sorted(locations['North America']['USA'])
for city in usa_sorted:
    print(city)

asia_cities = []

# This is the correct way to get two keys!
for countries, cities in locations['Asia'].items(): #multiple ways to achieve the same thing.
    print("this is country: " + countries)
    print("this is city: " + str(cities))
    city_country = cities[0] + " - " + countries 
    asia_cities.append(city_country)
    
asia_sorted = sorted(asia_cities)
for city in asia_sorted:
    print(city)

# HASHING
    
# Hashing is very important, because lookup time is constant O(1)
# Hash functions might get asked, there may be multiple hash functions that
# work as desired for your case. Communicate with the interviewer, ask questions, etc.
# Regarding collisions, 1) you can change the hash value, 2) you can add buckets to each hash
# key so that each unique key basically has a list, 3) or you can add a second, new hash function.

# When talking about hash tables, we have 'load factor':
# Load Factor = Number of Entries / Number of Buckets

# APPLICATION OF LOAD FACTOR
# The purpose of a load factor is to give us a sense of how "full" a hash table is. 
# For example, if we're trying to store 10 values in a hash table with 1000 buckets, 
# the load factor would be 0.01, and the majority of buckets in the table will be empty. 
# We end up wasting memory by having so many empty buckets, so we may want to rehash, 
# or come up with a new hash function with less buckets. 

# We can use our load factor as an indicator for when to rehash—as the load factor 
# approaches 0, the more empty, or sparse, our hash table is. 
# On the flip side, the closer our load factor is to 1 
# (meaning the number of values equals the number of buckets), 
# the better it would be for us to rehash and add more buckets. 
# Any table with a load value greater than 1 is guaranteed to have collisions. (IMPORTANT)

# If you have a hash function that divides a group of values by 100, and uses the remainder
# as a key, and if there are 100 numbers that are all multiples of 5; then the load is:
# For the load factor, you should divide the number of values by the number of buckets. 

# There are 100 values, as stated in the question, and 100 buckets (0 to 99). 
# Thus, 100/100 = 1 (CORRECT ANSWER)

# The answer to the second part is 107 (to speed up the algorithm). 
# The other values all had something wrong with them:
# 1) 125 is also a multiple of 5. Dividing a bunch of multiples of 5 by 
# another multiple of 5 will cause a lot of collisions. 
# Here's an example, where 10 is used as the divisor:
# 5 % 10 = 5
# 10 % 10 = 0
# 15 % 10 = 5
# 20 % 10 = 0

# 2) 87 is better than 125, but because it's less than 100 it'll still have collisions. (guarenteed in fact)

# 3) 1001 is good, but it'll create a ton of leftover buckets and waste a lot of memory.
    
# HASHMAPS
    
# A Python dictionary is a hash map! Constant time lookup!

# STRING KEYS QUIZ : check the screenshot for instructions, descriptions, and details.

# HASHTABLE IMPLEMENTATION

class HashTable(object):
    def __init__(self):
        self.table = [None]*10000

    def store(self, string):
        hv = self.calculate_hash_value(string) # don't forget to use self. (VERY IMPORTANT)
        if hv != -1:
            if self.table[hv] != None:
                self.table[hv].append(string)
            else:
                self.table[hv] = [string] # with brackets because we want a list so we can append if there is a collision

    def lookup(self, string):
        hv = self.calculate_hash_value(string)
        if hv != -1:
            if self.table[hv] != None:
                if string in self.table[hv]: # for lookup we also use a list function (... in ...)
                    return hv
        return -1

    def calculate_hash_value(self, string):
        value = ord(string[0])*100 + ord(string[1])
        return value

# ord(c) in Python Given a string of length one, return an integer representing the Unicode code 
# point of the character when the argument is a unicode object, or the value of the byte when the 
# argument is an 8-bit string.

# chr(i) return a string of one character whose ASCII code is the integer i.

# We can say that ord() and chr() inverse to each other.
        
# Setup
hash_table = HashTable()

# Test calculate_hash_value
# Should be 8568
print(hash_table.calculate_hash_value('UDACITY'))

# Test lookup edge case
# Should be -1
print(hash_table.lookup('UDACITY'))

# Test store
hash_table.store('UDACITY')
# Should be 8568
print(hash_table.lookup('UDACITY'))

# Test store edge case
hash_table.store('UDACIOUS')
# Should be 8568
print(hash_table.lookup('UDACIOUS'))

hash_table.table[hash_table.lookup('UDACIOUS')][1] = 'UDAC'

print(hash_table.table)


print(int(pow(4, 0.5)))

for i in range(0, 10):
    for j in range(0, 10):
        if j > 5:
            break # breaks only out of the 2nd (inner) loop
        print(i,j)
        
print(chr(101)) 

def hi(): # python functions how to be defined before they are used, unlike other languages such as Java
    print("hi")
    
hi()

# Given a smaller string s and a bigger string b, design an algorithm to find all permutations
# of the shorter string within the longer one. Print the location of each permutation.

def compare(array1, array2, length):
    """ Function to compare two arrays (hash tables) to determine if they match (True) or not (False) """
    for i in range(0, length):
        if(array1[i] != array2[i]):
            return False
    return True

def find_matching_indexes(str_pattern, str_text):
    """ Function to print out the beginning indexes of matched patterns in the text """
    num_chars = 256 # 256 ASCII characters available

    pattern = [0] * num_chars # similar to a hash table
    sliding_window = [0] * num_chars # similar to a hash table
    
    pat_len = len(str_pattern)
    text_len = len(str_text)
    
    for i in range(0, pat_len): 
        pattern[ord(str_pattern[i])] += 1
        sliding_window[ord(str_text[i])] += 1 # do this here to reduce O(pat_len + text_len) to O(text_len)
        
    for j in range(pat_len, text_len): # thanks to above line, you can start from pat_len and go to text_len
        if(compare(pattern, sliding_window, num_chars)):
            print("Match found begginning at index: ", j-pat_len)
        
        sliding_window[ord(str_text[j-pat_len])] -= 1
        sliding_window[ord(str_text[j])] += 1
        
    if(compare(pattern, sliding_window, num_chars)): # the last check has to be as checks in the loop happened before incrementation
        print("Match found begginning at index: ", text_len-pat_len)
        

# Tester
pattern = "abc"
text = "abccbabaccba"
find_matching_indexes(pattern, text)
# Prints the below lines as expected:
# Match found begginning at index:  0
# Match found begginning at index:  3
# Match found begginning at index:  6
# Match found begginning at index:  9