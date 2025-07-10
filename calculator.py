"""
Python Project 01: Personal Calculator
Author: Ameenah Begum ZainaB
Date: 10-07-2025

Description:
This script builds a command-line calculator that supports:
- Addition, subtraction, multiplication. division
- Input from user
- Clean error handling
- Repeat mode 
"""

def calculator(num1, num2, operator):
    if operator == "+":
        answer = num1 + num2
        return answer
    elif operator == "-":
        answer = num1 - num2
        return answer
    elif operator == "*":
        answer = num1 * num2
        return answer
    elif operator == "/":
        try:
            answer = num1 / num2
            return answer
        except ZeroDivisionError:
            return "Cannot divide by zero."
    else:
        return "Invalid operation"


if __name__ == "__main__":
    interaction = input("""Welcome to my Personal Calculator!
You can perform the following operations:
    • + for addition
    • - for subraction
    • * for multiplication
    • / for division
    
Would you like to perform a calculation?
Type "yes" to continue or "exit" to quit.\n""")

    while interaction.lower().strip() not in ["yes", "exit"]:
        print("Invalid input. Please type \"yes\" to continue or \"exit\" to quit.")
        interaction = input("Would you like to perform a calculation? Type 'yes' or 'exit': ")

    while True:
        try:
            number1 = float(input("Enter the first number: "))
            number2 = float(input("Enter the second number: "))
        except ValueError:
            print("Please enter valid numbers.")
            continue

        operation = input("Choose an operation (+, -, *, /): ")
        result = calculator(number1, number2, operation)
        print(f"Result: {result}")

        again = input("Would you like to perform another calculation? (yes/no): ").strip().lower()
        if again != "yes":
            print("Thank you for using the Personal Calculator. Goodbye!")
            break