"""
Calculator Assignment by Ajadi Ademola
"""


# a = print('yes') if age == 18 else print('no')
# User Input


# def addition(a: int, b: int) -> int:
#     return a + b
#
#
# print(addition(a=2, b=3))

def calculator(first_number, operator, second_number):
    
    if operator == "+":
        result = first_number + second_number
        print(result)
        
    elif operator == "-":
        result = first_number - second_number
        print(result)
          
    elif operator == "*":
        result = first_number * second_number
        print(result)
        
    elif operator == "/":
        result = first_number / second_number
        print(result)
           
    elif operator == "//":
        result = first_number // second_number
        print(result)
        
    elif operator == "**": 
        result = first_number ** second_number
        print(result)
         
    elif operator == "%":
        result = first_number % second_number
        print(result)
         
    if operator != "+" or "-" or "*" or "/" or "//" or "%" or "**":
        print("this input is invalid")

    return result
