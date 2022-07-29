#Introduction to Python

#Python Comments
#Any lines with the symbol "#" (pound sign), at the begining will be ignored by Python
#Such as this one
#Go Beach

# 1)Print Statements
print("Hello World")
print('Hello World')
print("GME to the moon")

#Numbers and variables
#Just like in math, you can save values such as number into variables

#Data types that you should know and will be using a lot:
    # 1. Integer
    # 2. Float
    # 3. String
    # 4. Bool (Boolean): Only has 2 values True or False
x = 5       #integer
y = 2.64    #float
z = 3.1412344
bitcoin = 55000

u = True    #bool
v = False   #bool

r = "5"     #String
s = "3.14"  #String
my_word = "shark"


#Printing numbers to the console
print(x)
print("Value of x:", x)

#What would be printed if we try to print "u" and "v"

print("Value of u: ", u)
print("Value of v: ", v)

#What is the difference between the value 5 and the string "5" ? 
##w = x + r
##print("Value of w: ", w)

#Reassigning variables and how it works.
x = 99
print("Value of x:", x)

#Saving Strings to a variable

a = "Hello"
b = "Long"

#Combingning and printing Strings (String Concatenation)
#What would be the value of c ?

c = a + b
print(c)
print("Hello"+ " " + b)
print("hello"+ " " + "Long")

# 2)Python Operators
#Python contains your normal math operators which are straight forward
#and does what you expect them too

m = 5
n = 2
r = "5"
s = "2"

#Operators that are mostly used for math
#Addition

p = m + n
print("Value of p:", p)

#What happened when we add 2 strings?
p = r + s
print("Value of p:", p)

#How would we solve this problem??
#You can change the data type from one to another using "Casting"
p = float(r) + int(s)
print(p)


#Subtraction
p = m - n
print("Value of p (substraction):", p)

#Multiplication
p = m * n
print("Value of p (multiplication):", p)

#Division
p = m / n
print("Value of p (division):", p)

#Exponential
p = m ** n
print("Value of p (exponential):", p)

#Modifying a variable then assign it to itself
z = 1
print("Value of z: ", z)


z = z + 1
#What would be the value of Z after this operation?

print(z)

#Although it looks wrong mathemtically since "z" cannot be equal to "z + 1"
#This statement is saying that take the "z" value previously, add one to it then save it back to "z"


# 3) Comparison operators
#Aside from operators that are used for math and string concatenations,
#there are also operators for comparing value between variables

j = 3
k = 8

#Comparison operators will return a boolean value in order words either True or False
#These values can be saved for later used or simply discarded

#Equal comparisons and not equal
L = (j == k)
print("Value of L:", L)

L = (j != k)
print("Value of L:", L)


#Since the operator "=" or equal sign is used to assign a value to a variable
#The operator "==" is used to compare to see if the two values to see if they are equal or not

#Less than and Less than or equal to

L = (j < k)
print("Less than:", L)
L = (k <= j)
print("Less than or equal:", L)


#More than and more than or equal to

L = (j > k)
L = (j >= k)

# 4)Logial operators such as And, Or, Not
#There are words in Python that are reserved for functions and operators such as these
#What if you want to do more than one comparison on one single line?

x = 4

shark = x < 10 and x > 100
print("Value of shark: ", shark)

shark = x < 10 or x > 100
print("Value of shark with or: ", shark)

shark = not(x < 10)
print("Value with not: ", shark)

# 5)Python If...else statements (also know as Conditional statement)
#What if you want a certain things to happen when a condition is met??

#Print "Go Beach" if i > 5

##i = 100
##if i > 5:
##    print("Go Beach")
##    x = 5 + 9
##    print("Value of x: ", x)
##    if i > 20:
##        print("Hello world")
##print("GME to the moon")        #Outside if statement,execute no matter what value of i is

#You can also do more in the "if block" such as adding another print line
#Just make sure the identation is correct

#3 keyword to remembers for conditional statement
    # 1. if
    # 2. else if (elif)
    # 3. else

#This block will execute from a top down order one line after another
#Which statement to be printed will depends on the value of "i"
#Indentation in Python is very important since it signified what statement will be executed
#depends on which condition is met. You will get an error
    
i = 20
if i > 200:
    print ("Hello World")
elif i > 50:
    print ("Go Beach")
elif i > 10:
    print ("shark")
else:
    print ("GME to the moon")


##i = 300
##if i > 200:
##    print ("Hello World")
##if i > 10:
##    print("Go Beach")
##if i > 5:
##    print ("GME to the moon")


#6)Python loops:
    
#For loops.
#Let say you want to print "Hello World" 5 times, how would you do it without writing 5 "print" statement?
#Also becareful with the value of "i" when you work with with loops and the range() function

print("hello world")
print("hello world")
print("hello world")
print("hello world")
print("hello world")

print("----------------")
for whale in range(8):
    print("Value of whale:", whale)
    print("Hello World")

#The same can be achieve using a while loop:

i = 0
while i < 5:
    print("Go Beach")
    i = i + 1

#Phrase to remember: As long as <condition> keep doing it
                    #Keep running until <condition>

#While loops runs when true and stops when condition is false

#Functions for user input:
#The function will return a String when the user enter a value which means if you are asking for a number
#and you want to do math with it, you will have to cast it to an interger or a float

name = input("Enter your name: ")
print ("Hello, " + name)
    











