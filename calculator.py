
import math

def calculator():
    print("=" * 40)
    print("       PYTHON SCIENTIFIC CALCULATOR")
    print("=" * 40)

    while True:
        print("\nSelect an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Modulus (%)")
        print("6. Power (**)")
        print("7. Square Root (√)")
        print("8. Percentage (%)")
        print("9. Factorial (!)")
        print("10. Exit")

        choice = input("\nEnter your choice (1-10): ")

        if choice == '10':
            print("\nThank you for using the calculator!")
            break

        try:
            if choice in ['1', '2', '3', '4', '5', '6']:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if choice == '1':
                    result = num1 + num2
                    operator = '+'

                elif choice == '2':
                    result = num1 - num2
                    operator = '-'

                elif choice == '3':
                    result = num1 * num2
                    operator = '*'

                elif choice == '4':
                    if num2 == 0:
                        print("Error: Cannot divide by zero!")
                        continue
                    result = num1 / num2
                    operator = '/'

                elif choice == '5':
                    if num2 == 0:
                        print("Error: Modulus by zero is not allowed!")
                        continue
                    result = num1 % num2
                    operator = '%'

                elif choice == '6':
                    result = num1 ** num2
                    operator = '**'

                print(f"\nResult: {num1} {operator} {num2} = {result}")

            elif choice == '7':
                num = float(input("Enter a number: "))

                if num < 0:
                    print("Error: Cannot calculate square root of a negative number!")
                    continue

                result = math.sqrt(num)
                print(f"\nSquare Root of {num} = {result}")

            elif choice == '8':
                num = float(input("Enter the number: "))
                percentage = float(input("Enter percentage: "))

                result = (num * percentage) / 100
                print(f"\n{percentage}% of {num} = {result}")

            elif choice == '9':
                num = int(input("Enter a non-negative integer: "))

                if num < 0:
                    print("Error: Factorial is not defined for negative numbers!")
                    continue

                result = math.factorial(num)
                print(f"\nFactorial of {num} = {result}")

            else:
                print("Invalid choice! Please select between 1 and 10.")

        except ValueError:
            print("Error: Please enter valid numeric values.")

        except OverflowError:
            print("Error: Result is too large.")

        except Exception as e:
            print(f"Unexpected error: {e}")


# Start the calculator
calculator()
