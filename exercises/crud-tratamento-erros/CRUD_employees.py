separator = "-" * 50
display_wrong_option = "Prompt a valid option."
display_continue= f'''{separator}
Do you want to continue?
1 - Yes.
0 - No.
'''
display_key = f'''Inform the key that you want to change: 
1 - Code
2 - Name
3 - Age
4 - Salary
{separator}'''
products = []

def main():
    while True:
        display_menu()
        choice_option = int(input("Select your option: "))
        print(separator)
        while True:
            match choice_option:
                case 1:
                    try:
                        code = int(input("Code: "))
                        name = input("Name: ")
                        age = int(input("Age: "))
                        salary = int(input("Salary: "))
                    except ValueError:
                        print("You need to prompt a number to code, age and salary.")
                    else:
                        register_employee(code, name, age, salary)
                        print(separator)
                        print("Employee registered successful.")
                    break
                case 2:
                    try:
                        code = int(input("Prompt the code of the employee that you want to read: "))
                    except ValueError:
                        print("You need to prompt a number to code.")
                    else:
                        read_employee(code)
                    break
                case 3:
                    try:
                        code = int(input("Prompt the code of the employee that you want to update: "))
                        key = int(input(display_key))
                    except ValueError:
                        print("You need to prompt a number to code and key")
                    else:
                        update_employee(code, key)
                        print(separator)
                        print("Employee updated successful.")
                    break
                case 4:
                    try:
                        code = int(input("Prompt the code of the employee that you want to delete: "))
                    except ValueError:
                        print("You need to prompt a number to code.")
                    else:
                        delete_employee(code)
                        print("Employee deleted successful.")
                    break
                case 5:
                    read_all_employees()
                    break
                case 6:
                    age_superior_than_25()
                    break
                case 7:
                    age_between_22_25_and_salary_above_3700()
                    break
                case _:
                    print(display_wrong_option)
        continue_option = int(input(display_continue))
        while True:
            if continue_option != 0 and continue_option != 1:
                print(display_wrong_option)
                print(display_continue)
                continue_option = int(input(display_continue))
            else:
                break
        if continue_option == 0:
            break

def register_employee(code, name, age, salary):
    employee = {
        'Code' : code,
        'Name' : name,
        'Age' : age,
        'Salary' : salary
    }
    products.append(employee)

def read_employee(code):
    for employee in products:
        if employee['Code'] == code:
            for key, value in employee.items():
                print(f"{key}: {value}")
            return
        print(separator)
    print("Prompt an existent code.")

def update_employee(code, key):
    options = {
        1 : 'Code',
        2 : 'Name',
        3 : 'Age',
        4 : 'Salary'
    }
    display_input = f"Prompt the new value of {options[key]}: "

    for employee in products:
        if employee['Code'] == code:
            print(f"The oldest value of {options[key]} was {employee[options[key]]}.")
            if key == 2:
                new_value = input(display_input)
                employee[options[key]] = new_value
                break
            new_value = int(input(display_input))
            employee[options[key]] = new_value
            break

def delete_employee(code):
    i = 0
    for employee in products:
        if employee['Code'] == code:
            products.pop(i)
            break
        i = i + 1

def read_all_employees():
    for employee in products:
        for key, value in employee.items():
            print(f"{key}: {value}")
        print(separator)

def age_superior_than_25():
    for employee in products:
        if employee['Age'] > 25:
            for key, value in employee.items():
                print(f"{key}: {value}")
            print(separator)

def age_between_22_25_and_salary_above_3700():
    for employee in products:
        if 22 < employee['Age'] < 25 and employee['Salary'] > 3700:
            for key, value in employee.items():
                print(f"{key}: {value}")
            print(separator)

def display_menu():
    menu_options = f'''{separator}
1 - Register a new employee.
2 - Read employee's info.
3 - Update employee's info.
4 - Delete employee's info.
5 - Read all employee's.
6 - Read employees with age superior then 25 years.
7 - Read employees with age between 22 and 35 years with a salary higher then 3700.
{separator}'''
    print(menu_options)


if __name__ == '__main__':
    main()