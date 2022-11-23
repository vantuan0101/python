character_name = "John"
character_age = 35
is_male = True 
is_female = False
print("He is \n years old")
print("Hello World")
print("Here is a " + character_name + "and he is" +character_age + "years old")

# working with string
phrase = "I'm a student"
print(phrase + " good")
print(phrase.lower()) # i'm a student
print(phrase.upper()) # I'M A STUDENT
print(phrase.isupper()) # False
print(phrase.upper().isupper()) # True
print(len(phrase)) # 13
print(phrase[0]) # I
print(phrase.index("a")) #4
print(phrase.index["stud"]) #5
print(phrase.replace("student", "teacher")) # I'm a teacher

# working with numbers
print(2)
print(2.05424334324)
print(-2.3423424)
print( 3 + 4 * 5 /6) # 6

my_num = 5
print(str(my_num)) # convert number to string
my_num2 = -5 
print(abs(my_num2)) # 5
print(pow(3, 2)) # 9 = 3^2
print(round(3.2)) # 3.0
print(round(3.7)) # 4.0

from math import *
from multiprocessing.sharedctypes import Value
print(floor(3.7)) # 3.0 làm tròn xuống
print(ceil(3.7)) # 4.0 làm tròn lên

# getting input from user
name = input("Enter your name : ")
print("Hello " + name + "!")

num1 = input("Enter number 1: ")
num2 = input("Enter number 2 : ")
print(num1 + num2) # Mặc định thì input sẽ đc nhận là string vd : 1 + 2 = 12
print(int(num1) + int(num2)) # convert string to number vd : 1 + 2 = 3
print(int(num1) + int(num2)) # vd : num1 = 1.2 , num2 = 3.0 => sẽ báo lỗi
print(float(num1) + float(num2)) # vd : num1 = 1.2 , num2 = 3.0 => 4.2

# mad libs game
# lists
friends1 = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends2 = ["kevin", 35, True]
print(friends1)
print(friends1[0]) # Kevin
print(friends1[2]) # Jim
print(friends1[-3]) # Jim
print(friends1[1:]) # ['Karen', 'Jim', 'Oscar', 'Toby']

# list functions
lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
# friends.extend(lucky_numbers) # ['Kevin', 'Karen', 'Jim', 'Oscar', 'Toby', 4, 8, 15, 16, 23, 42]
# friends.append("Creed") # ['Kevin', 'Karen', 'Jim', 'Oscar', 'Toby', 4, 8, 15, 16, 23, 42, 'Creed']
# friends.insert(0,"Beo") # ['Beo', 'Kevin', 'Karen', 'Jim', 'Oscar', 'Toby', 4, 8, 15, 16, 23, 42, 'Creed']
# friends.remove("Beo") # ['Kevin', 'Karen', 'Jim', 'Oscar', 'Toby', 4, 8, 15, 16, 23, 42, 'Creed']
# friends.clear() # []
# friends.pop() # ['Kevin', 'Karen', 'Jim', 'Oscar', 'Toby', 4, 8, 15, 16, 23, 42]
# x = friends.pop(1) # ['Kevin', 'Jim', 'Oscar', 'Toby'] return Karen
# print(x) 
# print(friends.index("Jim")) # 1
# print(friends.count("Jim")) # 1
# friends.sort() # ['Jim', 'Kevin', 'Oscar', 'Toby']
# friends.reverse() # ['Toby', 'Oscar', 'Kevin', 'Jim']
# friends2 =  friends

friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends2 =  friends.copy()
print(friends2)

# tuples is same as list but it can't be changed

coordinates = (4, 5)
print(coordinates[0]) # 4
print(coordinates[1]) # 5

coordinates = [(4, 5), (6, 7), (80, 34)]
print(coordinates[0]) # (4, 5)
print(coordinates[0][0]) # 4

# function

def  say_hi(name):
    print("Hello World")
    a  = 3
    b = 'hello'
    print(str(a) + b)
    print("Hello " + name)

say_hi("Beo")

def cube( num):
    return num * num * num

print(cube(3)) # 27
result = cube(4)
print(result) # 64

# if 
is_male =  True
is_tall = False
if is_male or is_tall: # is_male and is_tall:
    print("You are male but not tall")
elif is_male and not(is_tall) :
    print("You are short male")
else:
    print("You are female and not tall")
# if and comparison

def max_num(num1,num2,num3) :
    if num1>=num2 and num1>=num3 :
        return num1
    elif num2>=num1 and num2>=num3:
        return num2
    else: 
        return num3
result = max_num(1,2,3)
print(result)

# dictionary : building a better calculator

num1 = float(input("Enter first number: "))
op = input("Enter operator:")
num2 = float(input("Enter second number: "))
if op == "+" : 
    print("result : " + num1  + " + " + num2 + " = " + num1 + num2)

monthConversions = {
    1 : "January",
    "Feb" : "February",
    "Mar" : "March",
    "Apr" : "April",
    "May" : "May",
    "Jun" : "June",
    "Jul" : "July",
    "Aug" : "August",
    "Sep" : "September",
    "Oct" : "October",
    "Nov" : "November",
    "Dec" : "December",
}
print(monthConversions["Nov"]) # November
print(monthConversions.get("Dec")) # December
print(monthConversions.get("Lux" , "Not a valid key")) # default not found return none . or return options
print(monthConversions.get(1)) # January

# while loop

i= 1 
while i<=10:
    print(i)
    i+=1

# for loop
for letter in "Van Tuan" :
    print(letter) # V a n   T u a n

friends = ["Jim", "Karen", "Kevin"]
for friend in friends :
    print(friend) # Jim Karen Kevin
for index in range(10):
    print(index) # 0 1 2 3 4 5 6 7 8 9
for index in range(3,10):
    print(index) # 3 4 5 6 7 8 9

for index in range(len(friends)) :
    print(index) # 0 1 2
    print(friends[index]) # Jim Karen Kevin

# exponent function
print(2**3) # 8 <-> 2^3 = 2*2*2 = 8
def raise_to_power(base_num,pow_num):
    return base_num ** pow_num

result = raise_to_power(2,3)
print(result) # 8

# 2D lists and nested loops
def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation
print(translate(input("Enter a phrase: ")))

# comments
# this is a comment
'''
 Day la block comment
 block comment
'''

# try except
'''
if we have a error in our code, the program will stop running and we will get an error message
in exception handling, we can use try and except to handle the error
'''
try:
    Value = 10/0
    number = int(input("Enter a number: "))
    print(number)
# except ZeroDivisionError:
#     print("Divided by zero")
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Invalid input")

# read file

employee_file  = open("employees.txt", "a") # r : read , w : write , a : append , r+ : read and write
#print(employee_file.readable()) # check file can read -> True if open("employees.txt", "r")
print(employee_file.read()) # read all file
print(employee_file.readline()) # read 1 line
print(employee_file.readlines()) # read all line

for employee in employee_file.readlines():
    print(employee)

employee_file.write("\nTuan - Developer")
employee_file.close()

# modules and pip
import useful_tools
print(useful_tools.beat_meter)

# classes and objects

# class Student :
#     def __init__(self , name , major , gpa ,is_on_probation ):
#         self.name = name
#         self.major = major
#         self.gpa = gpa
#         self.is_on_probation = is_on_probation      
from Student import Student
student1 = Student("Jim", "Business", 3.1, False)
print(student1.name) # Jim

# 
from Question import Question
question_prompts = [
    "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What color are bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"

]
questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b"),
]

def run_test(questions):
    score = 0
    for question in questions:
        # answer = input(question.prompt)
        print(question.prompt)
        answer = input("Enter your answer: ")
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")

run_test(questions)

#
from Student import Student
student1 = Student("Oscar", "Accounting", 3.1 , False)
student2 = Student("Phyllis", "Business", 3.8 , False)
print(student2.on_honor_roll())

# inheritance
from Chef import Chef
myChef = Chef()
myChef.make_special_dish()
