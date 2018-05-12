def conversion():
    x = float(input("Hello there please input a number"))
    question = input("Would you like this number to be converted to miles or kilometers?")
    if question == "miles" or question == "m" or question == "mi":
        print(x * 0.621371)
    if question == "kilometers" or question == "km" or question == "k":
        print(x * 1.60934)
    x2 = input("Would you like to use this conversion calculator again? [Y/N]")
    while x2 == "yes" or x2 == "y":
        conversion()
        break
conversion()


