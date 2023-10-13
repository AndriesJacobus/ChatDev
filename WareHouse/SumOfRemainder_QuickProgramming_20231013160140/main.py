import tkinter as tk
from calculator import Calculator

def main():
    # Create an instance of the Calculator class
    calculator = Calculator()
    # Get user input for the number
    number = int(input("Enter a number: "))
    # Calculate the sum of divisors using the Calculator class
    sum_of_divisors = calculator.calculate_sum_of_divisors(number)
    # Display the result
    print(f"The sum of divisors of {number} is {sum_of_divisors}.")

if __name__ == "__main__":
    main()