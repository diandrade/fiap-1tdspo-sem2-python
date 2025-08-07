separator = "-" * 50
display_wrong_option = "Prompt a valid option."
display_continue= f'''{separator}
Do you want to continue?
1 - Yes.
0 - No.
{separator}
'''
display_key = f'''Inform the key that you want to change: 
1 - Code
2 - Name
3 - Age
4 - Salary
'''
employees = []

def main():
    while True:
        display_menu()
        choice_option = int(input("\nSelect your option: "))
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
                        print("Employee register with succeed")
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
                    break
                case 4:
                    print(" Something. ")
                    break
                case 5:
                    print(" Something. ")
                    break
                case 6:
                    print(" Something. ")
                    break
                case 7:
                    print(" Something. ")
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
    employees.append(employee)

def read_employee(code):
    for employee in employees:
        if employee['Code'] == code:
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

'''def update_employee(code, key):
    for employee in employees:
        if employee['Code'] == code:
            print(f"The oldest value of {key} was {employee['Code']}.")
            new_value = int(input())
'''

if __name__ == '__main__':
    main()