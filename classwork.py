def main():
    # problem1()
    problem2()


# Create a function that has a loop
# Prompt for numbers until the user enters q to quit
# If the user doesn't enter q, ask them to input another number
# When the user enters q to quit, print the SUM of all numbers entered
def problem1():
    num = "0"
    total = 0
    while num.lower() != "q":
        total+= (int(num))
        num = input("Enter a number, Enter q to quit \n")
    print(total)



# Create a function problem2()
#
# In this function prompt the user for 2 numbers
#
# Create a second function called do_the_math that accepts 2 parameters (the 2 entered numbers)
#
# In the do_the_math calculate the SUM, DIFFERENCE, PRODUCT, and QUOTIENT (division result) and return them as a dictionary to the calling function
#
# Example: Dictionary result returned if the argumants 25 and 10 are passed to the function:
#
# {'diff': 15, 'prod': 250, 'quot': 2.5, 'sum': 35}
#
# In your problem2() function, print the dictionary result returned from your do_the_math function using string literal formatting
#
# Example: Execution and Output
#
# Enter the First Number in the calculation:
# 25
# Enter the Second Number in the calculation:
# 10
# Here are your results for the numbers 25 and 10:
#     The SUM result is 35
# The DIFFERENCE result is 15
# The PRODUCT result is 250
# The DIVISION result is 2.5

# KEY: This version is close but would not run
def problem2():
    num1 = int(input("Enter a number "))
    num2 = int(input("Enter another number "))
    opArr= []
    opArr.append(do_the_math(num1,num2))
    sum = num1 + num2
    diff = num1 - num2
    prod = num1 * num2
    quot = num1 / num2
def do_the_math(num1,num2,):
    for eachEl in opArr:
        print(f"sum = {eachEl[sum]},")
        print(f"diff = {eachEl[diff]}")
        print(f"quot ={eachEl[quot]}")
        print(f"prod = {eachEl[prod]}")
    return{"sum": sum , "difference": diff , "product": prod, "quotient": quot}
#








if __name__ == '__main__':
    main()