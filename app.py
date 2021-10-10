# Create a calculator which handles +,-,*,/ and outputs answer based on the mode/ operator used
# Extend functionality with extra mode so it also does celsius to fahrenheit conversion
# formula is: temp in C*9/5 + 32 = temp in f
def farenheit_to_celsius(temp):
    return (temp * 9/5) + 32


def calculate(num1, num2):
    if operand == '+':
        return num1 + num2
    elif operand == '-':
        return num1 - num2
    elif operand == '*':
        return num1 * num2
    elif operand == '/':
        return num1 / num2
    else:
        return None


operand = input('''Please enter:
    + add,
    - subtract,
    * multiply,
    / divide
    -------------
    f convert to
    celsius. ''')
first_number = float(input('Enter first number: '))
if operand == 'f':
    temperature = farenheit_to_celsius(first_number)
    print(f"{first_number}F is {temperature}C")
    quit()
if operand == None:
    print('Please enter +, -, *, /')
second_number = float(input('Enter second number: '))


total = calculate(first_number, second_number)
print(f"{first_number} {operand} {second_number} = {total}")
