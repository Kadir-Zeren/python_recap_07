
city_list = [['New York', 'London' , 'Istanbul' , 'Seoul' , 'Sydney' ]]
print(city_list[0]) # access to first and only element

city_list = [[ 'New York' , 'London', 'Istanbul', 'Seoul', 'Sydney' ]]
print(city_list[0][2])

city_list = [[ 'New York' , 'London', 'Istanbul' , 'Seoul' , 'Sydney' ]]
print(city_list[0][2][3])

even_numbers = [2, 4, 6, 8, 10, 12, 14]
print(even_numbers[2:5])

list(range(10))
list(range(1, 11))
list(range(0, 30, 5))

a = tuple([1,2,3]) + (3,4,5)
print(a)
print(type(a))

range(1,11)

a = range(1,11)
type(a)

print(a)

list(a)

list(range(2,15,2))


a = range(2,15,2)
print(a)
print(*a)

odd_numbers = tuple(range(11))
print(odd_numbers)
print(odd_numbers[1:11:2])


odd_numbers = list(range(11))
print(odd_numbers)
print(odd_numbers[1:11:2])

animals = ['elephant' , 'bear', 'fox' , 'wolf' , 'rabbit', 'deer', 'giraffe' ]
print(animals[ : ]) # all elements of the list

animals = ['elephant', 'bear' , 'fox' , 'wolf', 'rabbit' , 'deer', 'giraffe' ]
print(animals[3:])

animals = ['elephant' , 'bear' , 'fox' , 'wolf', 'rabbit' , 'deer' , 'giraffe' ]
print(animals[ :5])

animals = ['elephant' , 'bear' , 'fox', 'wolf' , 'rabbit' , 'deer' , 'giraffe']
print(animals[ :: 2])

mix_list = [1, [1, "one", 2, "two", 3, "three"], 4]
mix_list[1]

mix_list[1][1 :: 2]

mix_list = [1, [1, "one", 2, "two", 3, "three"], 4]
print(mix_list[1][1:6:2])

mylist = [0,1,2,3,4,5]
mylist[2:20]

city = ['New York', 'London' , 'Istanbul', 'Seoul', 'Sydney' ]
print(city[-4])

reef = ['swordfish', 'shark' , 'whale' , 'jellyfish', 'lobster', 'squid' , 'octopus' ]
print(reef[-3:])

reef = ['swordfish', 'shark', 'whale', 'jellyfish', 'lobster', 'squid' , 'octopus' ]
print(reef[ :- 3])

reef = ['swordfish' , 'shark' , 'whale' , 'jellyfish' , 'lobster' , 'squid' , 'octopus' ]
print(reef[ ::- 1]) # we have produced the reverse of the list

mylist[2:20]
harf = 'abcdefg'
mylist = list(harf)
mylist

mylist[ ::-1]

reef = ['swordfish', 'shark' , 'whale' , 'jellyfish' , 'lobster' , 'squid' , 'octopus' ]
print(reef[ ::- 2])

len(mylist)

harf
harf[ ::- 1]

letters = ["a", "b", "c", "d", "f", "g", "h", "i", "j"]
print(letters[7:3 :- 1])
print(letters[2:6 :- 1])

mylist[2:2 :- 1]
mylist[:4 :- 1]
mylist[0:4 :- 1]
harf
harf[0:4 :- 1]
harf[:4 :- 1]

mylist
mylist[3]

mylist[3] = 'kelime'
mylist

mylist[1] = [1,2,3]
mylist 

mylist[-3:] = [7,8,9]
mylist

mylist[-4:] = [20,30] 
mylist

mylist[2] = [90,89,78] 
mylist
mylist[0:1] = ['a', 'b', 'c']
mylist

a = range(5,20)
type(a)
a
list(a)
range(2,21,3)
list(range(2,21,3))
list(range(2,21,-3))
list(range(21,2,-3))
range(10)

str(range(10))

harf
harf += 'a'
harf
harf = harf + 'a'

tuple_1 = ('h', 'a', 'p', 'p', 'y' )
word = 'happy'
tuple_2 = tuple(word)
print(tuple_1)
print(tuple_2)

mytuple = (1,2,3,4,5,6) 
mytuple
tuple('itop')

mytuple2 = 9,8,7,6,5
mytuple2
print(type(mytuple), type(mytuple2))

empty_tuple = ()
print(type(empty_tuple))

a = [1,2,3]
b = (1,2,3)

print(type(a), type(b))

bos_tuple = ()
type(bos_tuple)
bos_tuple

bos_tuple2 = tuple()
type(bos_tuple2)
bos_tuple2

my_tuple = ("Solar")
print(my_tuple, type(my_tuple), sep="\n")

mytuple = ("Solar")
mytuple
type(mytuple)

mytuple = ("Solar",)
type(mytuple)
mytuple = (5)
type(mytuple)
mytuple = (5,)
type(mytuple)

solar = "Earth", "Venus", "Uranus"
print(solar, type(solar), sep="\n")

my_tuple=(1, 4, 3, 4, 5, 6, 7, 4)
my_list = list(my_tuple)
print(type(my_list), my_list)

my_list = [1, 4, 3, 4, 5, 6, 7, 4]
my_tuple = tuple(my_list)
print(type(my_tuple), my_tuple)

mountain = tuple('Alps')
print(mountain)

tuple_1 = 'h', 'a', 'p', 'p', 'y'
tuple_2 = 1, 3, 5
print(tuple_1)
print(type(tuple_1))
print(tuple_2)

range(1,11)
tuple(range(1,11))

number = tuple(range(1,11))
print(number, type(number), sep="\n")

mytuple = tuple(range(1,11))
print(mytuple, type(mytuple))

even_no = (0, 2, 4)
print(even_no[0])
print(even_no[1])
print(even_no[2])

mytuple

city_list = ['Tokyo' , 'Istanbul' , 'Moskow' , 'Dublin' ]
city_tuple = tuple(city_list) 
# city_tuple[0] = 'New York' # you can't assign a value

mytuple

mytuple[3]

mylist = list(mytuple)
mylist

mylist[3] = 35
mylist

mytuple = tuple(mylist)
mytuple

mix_tuple = ("11", 11, [2, "two", ("six", 6) ], (5, "fair"))

tuple((1,2,3))

mix_tuple = ("11", 11, [2, "two", ("six", 6)], (5, "fair"))
str_six = mix_tuple[2][2][0]
print(str_six)

mix_tuple[2]
mix_tuple[2][2]
mix_tuple[2] [2][0]

mix_tuple = ("11", 11, [2, "two", ("six", 6)], (5, "fair"))
str_six = mix_tuple[2] [1:3]
print(str_six, type(str_six), sep="\n")

mix_tuple[2]
type(mix_tuple[2])
mix_tuple[2] [1:3]

mix_tuple[2]
mix_tuple[2][2]
type(mix_tuple[2][2])

a = tuple(range(10))
a
a[3:7]

mix_tuple = ("11", 11, [2, "two", ("six", 6)], (5, "fair"))
last = mix_tuple[-1]
print(last, type(last), sep="\n")

mix_tuple = ("11", 11, [2, "two", ("six", 6)], (5, "fair"))
option_1 = mix_tuple[3][1]
option_2 = mix_tuple[-1] [1]
print(option_1, option_2, sep = "\n")

a = [1,2,3]
b = (1,2,3)

import sys

sys.getsizeof(a)
sys.getsizeof(b)

print('15.000$' .endswith('$'))

phrase = 'What is Soul?'
print(phrase.upper().swapcase())

phrase = 'What is Soul?'
print(phrase. title())

phrase = 'What is Soul?'
new_phrase = phrase. replace('Soul', 'feeliNGS' )
print(new_phrase. title())

s = 'Hello World  '

s.strip()

s = 'Eggs, spam and eggs'
print(s.count('eggs'))

s = 'Spam, eggs, spam and eggs.'
print(s.find('egs'))

s = 'Eggs, spam and eggs.'
print (s.strip('Es.'))