# the class had us do a basic excption handling. I reazlied that excption handling was also needed on the input to handle basic input errors to make sure the user inputs an integer before calling the division function. 

def safe_divide(numerator,denominator):
    """ divides two input numbers and handles ZeroDivisionErrors """
    try:
        answer = numerator/denominator
        return answer
    except ZeroDivisionError:
        print("The number you provided cant divide 1 because it is 0")
        return None
    except ValueError:
        print("You did not provide a number")
        return None
    except:
        print("Something went wrong")
        return None
    finally:
        print("Processing Complete")

try:
    numerator = int(input("Please enter a number to divide"))
except ValueError:
    print("please enter an integer")
    numerator = int(input("Please enter a number to divide"))

try:
    denominator = int(input("Please enter a number to divide by"))
except ValueError: 
    print("please enter an integer")
    denominator = int(input("Please enter a number to divide by"))
    
print(safe_divide(numerator,denominator))

import math

def square_root(number1):
    """ square_root finds the square root of a number while handeling ValueErrors """
    try:
        result = math.sqrt(number1)
        return(result)
    except ValueError:
        print("Error: Invalid input! Please enter a positive integer or a float value.")
        return None

try:
    number1 = int(input("Please enter a number to calculate the square root"))
except ValueError:
    print("please enter an integer")
    number1 = int(input("Please enter a number to calculate the square root"))
    
print(square_root(number1))
