from Calculator import calculator

first_number = int(input("Enter the first number: "))
operator = input("Enter your preferd operator, +, -, /, %, //, **, or *: ")
second_number = int(input("Enter the second number: "))

result = calculator(first_number= first_number, second_number= second_number, operator= operator)
