from calculator import Calculator

def main():
    print("Welcome to the Simple Calculator!")
    print("Select an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    calc = Calculator()

    while True:
        choice = input("Enter your choice (1-5): ")
        
        if choice == '5':
            print("Thank you for using the calculator. Goodbye!")
            break

        if choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
            except ValueError:
                print("Invalid input! Please enter numerical values.")
                continue

            if choice == '1':
                print(f"The result is: {calc.add(num1, num2)}")
            elif choice == '2':
                print(f"The result is: {calc.subtract(num1, num2)}")
            elif choice == '3':
                print(f"The result is: {calc.multiply(num1, num2)}")
            elif choice == '4':
                if num2 != 0:
                    print(f"The result is: {calc.divide(num1, num2)}")
                else:
                    print("Division by zero is not allowed.")
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
