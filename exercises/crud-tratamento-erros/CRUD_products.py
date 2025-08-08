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
display_continue= f'''{separator}
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
        'Code' : code,
        'Description' : description,
        'Quantity' : quantity,
        'Price' : price
    }
    products.append(product)

def read_product_info(code):
    pass


def update_product_info(code, key):
    pass


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
                        code = input("Prompt the product code: ")
                        description = input("Prompt the product description: ")
                        quantity = input("Prompt the product quantity: ")
                        price = input("Prompt the product price")
                        if not code.isdigit() and quantity.isdigit():
                            raise ValueError("You must enter a positive integer.")
                        if not price.isdecimal():
                            raise ValueError("You must enter a positive decimal.")
                        code = int(code)
                        for product in products:
                            if product['Code'] == code:
                                raise ValueError("You must enter a unique code.")
                        quantity = int(quantity)
                        price = int(price)
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
                        read_product_info(code)
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
                        update_product_info(code, key)
                        print("Product updated successful.")
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