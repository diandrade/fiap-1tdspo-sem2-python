separator = "-" * 50
display_wrong_option = "Prompt a valid option."
menu_options = f'''{separator}
1 - Register a new product.
2 - Read product's info.
3 - Update product's info.
4 - Delete product's info.
5 - Read all product's.
6 - Read product's with price between R$150,00 and R$500,00.
7 - Read products with quantity higher then 100 units.
{separator}'''
display_continue = f'''{separator}
Do you want to continue?
1 - Yes.
0 - No.
{separator}'''
display_key = f'''{separator}
Inform the key that you want to change: 
1 - Code
2 - Description
3 - Stocked Quantity
4 - Price
{separator}'''

products = []


def register_product(code, description, quantity, price):
    product = {
        'Code': code,
        'Description': description,
        'Quantity': quantity,
        'Price': price
    }
    products.append(product)


def read_product_info(code):
    for product in products:
        if product['Code'] == code:
            for key, value in product.items():
                print(f"{key}: {value}")
            return True
    return False


def update_product_info(code, key):
    keys = {
        1 : 'Code',
        2 : 'Description',
        3 : 'Quantity',
        4 : 'Price'
    }

    for product in products:
        if product[keys[key]] == code:
            print(f"The oldest value of {keys[key]} was {product[keys[key]]}.")
            new_value = input(f"Prompt the new value of {keys[key]}: ")
            match key:
                case 1:
                    try:
                        if not new_value.isdigit():
                            raise ValueError("You must enter a positive integer.")
                    except ValueError as e:
                        print(f"Caught an error: {e}")
                    else:
                        product[keys[key]] = int(new_value)
                case 2:
                    product[keys[key]] = int(new_value)
                case 3:
                    try:
                        if not new_value.isdigit():
                            raise ValueError("You must enter a positive integer.")
                    except ValueError as e:
                        print(f"Caught an error: {e}")
                    else:
                        product[keys[key]] = int(new_value)
                case 4:
                    try:
                        new_value_float = float(new_value)
                        if new_value_float < 0:
                            raise ValueError("You must enter a positive floating number.")
                    except ValueError as e:
                        print(f"Caught an error: {e}")
                    else:
                        product[keys[key]] = new_value_float
            return True
    return False


def delete_product(code):
    pass


def read_all_products():
    pass


def get_products_by_price_range():
    pass


def get_products_by_quantity():
    pass


def main():
    while True:
        print(menu_options)
        try:
            menu_selected_option = input("Choose an option (1-7): ")
            if not menu_selected_option.isdigit():
                raise ValueError("You must enter a positive integer.")

            menu_selected_option = int(menu_selected_option)
            if menu_selected_option < 1 or menu_selected_option > 7:
                raise ValueError("You must select an option between 1 and 7.")

        except ValueError as e:
            print(f"Caught an error: {e}")

        else:
            match menu_selected_option:
                case 1:
                    try:
                        print("Please enter the product details:")
                        code = input("Product code (a positive integer): ")
                        description = input("Product description: ")
                        quantity = input("Product quantity (a positive integer): ")
                        price = input("Product price (e.g., 99.99): ")

                        code = int(code)
                        if code <= 0:
                            raise ValueError("Code must be a positive integer.")

                        is_unique = True
                        for product in products:
                            if product['code'] == code:
                                is_unique = False
                                break
                        if not is_unique:
                            raise ValueError("You must enter a unique code.")

                        quantity = int(quantity)
                        if quantity < 0:
                            raise ValueError("Quantity cannot be negative.")

                        price = float(price)
                        if price < 0:
                            raise ValueError("Price cannot be negative.")

                    except ValueError as e:
                        print(f"Caught an error: {e}")

                    else:
                        register_product(code, description, quantity, price)
                        print("Product registered successful.")
                case 2:
                    try:
                        code = input("Prompt the product code: ")
                        if not code.isdigit():
                            raise ValueError("You must enter a positive integer.")
                        code = int(code)

                    except ValueError as e:
                        print(f"Caught an error: {e}")

                    else:
                        if not read_product_info(code):
                            print("You must enter a valid code.")
                case 3:
                    try:
                        code = input("Prompt the product code: ")
                        print(display_key)

                        key = input("Prompt the key code: ")
                        if not code.isdigit() and key.isdigit():
                            raise ValueError("You must enter a positive integer.")

                        code = int(code)
                        key = int(key)
                        if key < 1 or key > 4:
                            raise ValueError("You must select a key option between 1 and 4.")

                    except ValueError as e:
                        print(f"Caught an error: {e}")

                    else:
                        if update_product_info(code, key):
                            print("Product updated successful.")
                        else:
                            print("You must enter a valid code.")
                case 4:
                    try:
                        code = input("Prompt the product code: ")
                        if not code.isdigit():
                            raise ValueError("You must enter a positive integer.")
                        code = int(code)

                    except ValueError as e:
                        print(f"Caught an error: {e}")

                    else:
                        delete_product(code)
                        print("Product deleted successful.")
                case 5:
                    read_all_products()
                case 6:
                    get_products_by_price_range()
                case 7:
                    get_products_by_quantity()
            print(display_continue)
            try:
                continue_option = input("Choose an option: ")
                if not continue_option.isdigit():
                    raise ValueError("You must enter a positive integer number.")

                continue_option = int(continue_option)
                if continue_option != 0 and continue_option != 1:
                    raise ValueError("You must prompt a value between 0 and 1.")

            except ValueError as e:
                print(f"Caught an error: {e}")

            else:
                if not continue_option:
                    print("Closing...")
                    break


if __name__ == '__main__':
    main()
