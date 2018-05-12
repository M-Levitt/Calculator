print("This is a calculator") #introduces what the code is
def calculator():
    number1 = float(input("Select a number")) #asks the user for a number to start off with
    number2 = float(input("Now select another number")) #takes the first num and the operation and combines it with this num
    def question():
        operation = input("Add, sub, multi, div, or power these numbers?") #asks the user for a function to do with number1
        if operation == "add" or operation == "sub" or operation == "multi" or operation == "div" or operation == "power" or operation == "+" or operation == "-" or operation == "*" or operation == "/" or operation == "^":
            def calculations():
                if operation == "add" or operation == "+": #generates the add function
                    print(number1,"+", number2, "is" ,number1 + number2)
                elif operation == "sub" or operation == "-": #generates the subtract function
                    print(number1, "-", number2, "is", number1 - number2) 
                elif operation == "multi" or operation == "*": #generates the multiply function
                    print(number1, "*", number2, "is", number1 * number2)
                elif operation == "power" or operation == "^": #generates the power function(two ** = ^)
                    print(number1, "^", number2, "is", number1 ** number2)
                elif operation == "div" or operation == "/": #generates the division function(two // or % is the remainder of)
                    x = input("Would you like the remainder? [Y/N]") #asks the user if they'd like the remainder instead of just dividing
                    if x == "y" or x == "yes": #yes will give the remainder
                        print("The remaninder of", number1,"divided by", number2, "is", number1 % number2)
                    else: #anything else just gives the division result
                        print(number1, "/", number2, "is", number1 / number2)
            calculations()            
        else:
            print("Please select a mode")
            question()
    question()
    x = input("Would you like to use this calculator again? [Y/N]") #asks the user if they'd like the use the calculator again
    while x == "yes" or x == "y": #creates an infinite loop if they say yes or y
        calculator()
        break # if not yes or y then the function breaks

calculator()


"""
elif stands for else if and it creates another 
argument for the if argument aside from just one with else:
"""

        