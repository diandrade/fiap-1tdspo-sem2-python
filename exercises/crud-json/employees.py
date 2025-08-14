separator = "-" * 50
display_wrong_option = "Prompt a valid option."
display_menu = menu_options = f'''{separator}
1 - Register a new employee.
2 - Read employee's info.
3 - Update employee's info.
4 - Delete employee's info.
5 - Read all employee's.
6 - Read employees with age superior then 25 years.
7 - Read employees with age between 22 and 35 years with a salary higher then 3700.
8 - 
{separator}'''
display_continue = f'''{separator}
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
employees = []

def create_employee(code, name, age, salary):
def search_employee(code):




def main():
    print(display_menu)
    choice_option = int(input("Select your option: "))
    print(separator)
    while True:
        match choice_option:
            case 1:
                while True:
                    try:
                        code = int(input("Prompt the employee's code: "))
                        if any(employee['Code'] == code for employee in employees):
                            print("You should prompt a unique value.")
                            continue
                        break
                    except ValueError:
                        print("Invalid input. Please, enter a valid integer for the employee code.")

                while True:
                    try:
                        name = input("Prompt the employee's name: ")
                        age = int(input("Prompt the employee's age: "))
                        salary = float(input("Prompt the employee's salary: "))
                        if age <= 0 or salary <= 0:
                            print("Age and salary should be positive values.")
                            continue
                        break
                    except ValueError:
                        print("Invalid input. Please, enter a valid integer for the employee code.")
                        
                create_employee(code, name, age, salary)

            case 5:
                print("Read all employees")
            case 6:
                print("Read employees with age superior then 25 years")
            case 7:
                print("Read employees with age between 22 and 35 years with a salary higher then 3700")
            case 8:
                print("Export employees to a .txt file.")
            case 9:
                print("Export employees with age superior then 25 years to a .txt file.")
            case 10:
                print("Export employees with age between 22 and 35 years with a salary higher then 3700 to a .txt file.")
            case 11:
                print("Export employees to a JSON file.")
            case 12:
                print("Import JSON file to a table.")

if __name__ == '__main__':
    main()
