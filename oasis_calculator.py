def oasis_calculator():
    print("--- Welcome to The Oasis Accounting Tool ---")
    print("Operations: +, -, *, /, power (pow)")
    
    while True:
        try:
            # Capture inputs
            num1 = float(input("\nEnter first number: "))
            operator = input("Enter operator (+, -, *, /, pow): ")
            num2 = float(input("Enter second number: "))

            # Logic routing
            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                result = num1 / num2 if num2 != 0 else "Error: Division by zero"
            elif operator == 'pow':
                result = num1 ** num2
            else:
                result = "Invalid Operator"

            print(f"Result: {result}")

            # Persistent Loop Check
            cont = input("\nPerform another calculation? (yes/no): ").lower()
            if cont != 'yes':
                print("Exiting The Oasis Accounting Tool. Goodbye!")
                break
                
        except ValueError:
            print("Invalid input. Please enter numeric values.")

# Run the tool
oasis_calculator()
