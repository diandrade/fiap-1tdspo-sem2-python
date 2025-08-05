try: # Try to execute the info.
    num1 = int(input("Digit the first number.\n"))
    num2 = int(input("Digit the second number.\n"))
except ValueError: # When some instructions return some error.
    print("Please, digit only numbers")
else:
    soma = num1 + num2
    print(f"Sum: {soma}")
finally:
    print("Operation finished")
