#Calculator

def add(n1,n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1 / n2

#store these functions in a dictionary
#act as the means in which we will call the functions
operations = {
"+": add,
"-": subtract,
"*": multiply,
"/":divide
}

num1 = int(input("What's the first number?: "))
for symbol in operations:
    print (symbol)
    #only prints out keys in a dictionary
operation_symbol = input("Pick an opertaion from the line above: ")
num2 = int(input("What's the second number?: "))

calculation_function = operations[operation_symbol]
first_answer = calculation_function(num1,num2)
print (f"{num1} {operation_symbol} {num2} = {first_answer}")

# storethe previous answer to use in the next calculation
operation_symbol = input("Pick an opertaion from the line above: ")
num3 = int(input("What's the third number?: "))
calculation_function = operations[operation_symbol]
second_answer = calculation_function(first_answer,num3)
print (f"{first_answer} {operation_symbol} {num3} = {second_answer}")
# same way as saying answer = calculation_function((num1, num2),num3)
