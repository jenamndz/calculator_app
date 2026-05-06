def calculator():

    while True:
        print("\n--- Simple App Calculator ---")

        print("Operations: \n"
              "1. Addition \n"
              "2. Subtraction \n"
              "3. Multiplication \n"
              "4. Division")
        choice = input("Enter choice (1/2/3/4): ")

        if choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if choice == '1':
                    print(f"Result: {num1 + num2}")
                elif choice == '2':
                    print(f"Result: {num1 - num2}")
                elif choice == '3':
                    print(f"Result: {num1 * num2}")
                elif choice == '4':
                    if num2 == 0:
                        raise ZeroDivisionError("Cannot divide by zero.")
                    print(f"Result: {num1 / num2}")
calculator()