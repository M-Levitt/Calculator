print("Hello and welcome.\nThis is a tool for investors.") 
print("It's used to see to see how they should set up their investment portfolio. \nPlease proceed by following the instructions.")
""" above line introduces the user to what this program does """
def portfolio(): #functions that starts the portfolio
    money = float(input("How much money would you like to invest?")) #asks the user how much money they'd like to save, and then holds that value
    if money > 0:
        def calc(money):
            print("You would invest in stocks, bonds, and cash")
            x2 = input("Would you like a small, medium, or large risk portfolio?")
            if x2 == "small" or x2 == "s":
                inv1 = {"Stocks": "$" + str(money * 0.3), "Bonds": "$" + str(money * 0.6), "Cash": "$" + str(money * 0.1)}
                print(inv1)
            elif x2 == "medium" or x2 =="m":
                inv2 = {"Stocks": "$" + str(money * 0.5), "Bonds": "$" + str(money * 0.4), "Cash": "$" + str(money * 0.1)}
                print(inv2)
            elif x2 == "large" or x2 == "l":
                inv3 = {"Stocks": "$" + str(money * 0.6), "Bonds": "$" + str(money * 0.3), "Cash": "$" + str(money * 0.1)}
                print(inv3)
            """ above code is messer, would recommend to clean it up more fluid code """    
        calc(money) # calls function + argument            
    else:
        print("Please input a number greater than 0") # user must input a real number that isn't less than 0
        portfolio()    
    question = input("Would you like to use this again?") # asks user if they'd like to use the tool again
    while question == "y" or question == "yes":
        portfolio()
        break
""" above code, user must answer one of those two arguments or else the code won't work, basically repeats the program """
portfolio() # calls the function
