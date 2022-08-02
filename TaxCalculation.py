#First program
#Calculate tax
#CSULB 2022


#Take user input: User's name, and income

def CalculateTax(): # function header
    Name = input("Please enter your name: ")# take user name input as a string

    Income = float(input("Please enter your income: "))# take user income input as a float

    print(Name," is making $",Income," a year.")# confirmation statement

    IncomeTax = None # make an IncomeTax variable

    if Income <= 10000:
        print("<=10000")
        IncomeTax = 0
        
    elif Income > 10000 and Income <= 19999:
        print(">10000")
        IncomeTax = (Income - 10000) * 0.1

    else:
        print(">20000")
        IncomeTax = 1000 +(Income - 20000)*0.2
        
    print("Your income tax is $",IncomeTax)

CalculateTax() #call the function
