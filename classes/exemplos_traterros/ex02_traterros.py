try:
    num1 = int(input("Digit the first number: "))
    num2 = int(input("Digit the second number: "))

    divisao = num1 / num2
except ValueError:
    print("Please, digit only numbers")
except ZeroDivisionError:
    print("Zero error division, digit a denominator different of zero.")
else:
    print(f"Divisão: {divisao}")

# We can have more than one except by code
# We can use try except in database transitions.