def validateIntegers(num):
    while not num.isdigit():
        num = input("Please enter a valid integer: ")
    return int(num)


def validateOperations(operation):
    operations = '+-*/'
    while operation not in operations:
        operation = input("please eneter a valid operation: ")
    return operation


def calculate(num_1,num_2,operation):
    result = 0
    if operation == '+':
        result = num_1 + num_2
    elif operation == '-':
        result = num_1 - num_2
    elif operation == '*':
        result = num_1 * num_2
    elif operation == '/':
        if num_2==0:
            print("Error: division by zero")
            return
        else:
            result = num_1 / num_2

    print(f"{num_1} {operation} {num_2} = {result}")


choice='1'
while choice=='1':
    num_1 = input('Enter the first number: ')
    num_1 = validateIntegers(num_1)
    operation = input('Enter the operation: ')
    operation = validateOperations(operation)
    num_2 = input('Enter the second number: ')
    num_2 = validateIntegers(num_2)
    calculate(num_1,num_2,operation)
    
    choice = input("1. Continue \n2. Exit the program ")
    
    while choice !='1' and choice!='2' :
        choice = input("Enter a valid choice (1,2)")
    if choice=='2':
        print("Exiting the program")
        






