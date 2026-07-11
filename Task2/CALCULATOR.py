print("=" * 50)
print("          SIMPLE CALCULATOR")
print("=" * 50)

while True:

    print("\nChoose an Operation")
    print("-" * 25)
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")
    print("-" * 25)

    choice = input("Enter your choice (1-5): ")

    if choice == "5":
        print("\nThank you for using the Simple Calculator.")
        print("Program Closed Successfully!")
        break

    elif choice in ["1", "2", "3", "4"]:

        num1 = float(input("\nEnter First Number : "))
        num2 = float(input("Enter Second Number: "))

        print("\n" + "=" * 40)

        if choice == "1":
            result = num1 + num2
            print("Operation : Addition")
            print(f"{num1} + {num2} = {result}")

        elif choice == "2":
            result = num1 - num2
            print("Operation : Subtraction")
            print(f"{num1} - {num2} = {result}")

        elif choice == "3":
            result = num1 * num2
            print("Operation : Multiplication")
            print(f"{num1} * {num2} = {result}")

        elif choice == "4":
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
            else:
                result = num1 / num2
                print("Operation : Division")
                print(f"{num1} / {num2} = {result}")

        print("=" * 40)

    else:
        print("\nInvalid Choice!")
        print("Please enter a number between 1 and 5.")