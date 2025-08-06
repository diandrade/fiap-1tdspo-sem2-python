def main():
    products = []

    while True:
        print("-" * 50)
        print('''
PRODUCTS CRUD

1 - Add a new product.
2 - Read the info of some product.
3 - Update some info of the product.
4 - Delete a product.
5 - View all the products.
6 - Report all the products with the value between R$150,00 and R$500,00.
7 - Report all the products with the quantity above 1 hundred units.
''')
        print("-" * 50)

        try:
            continue_decision = int(input('''
Do you want to continue?
1 - Yes.
0 - No.
'''))
            if continue_decision != 0 and continue_decision != 1:
                raise ValueError
        except ValueError:
            print("Input must be 0 or 1.")
            break
        else:
            if not continue_decision:
                break

if __name__ == '__main__':
    main()