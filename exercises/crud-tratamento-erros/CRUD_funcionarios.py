employees = []

def main():
    while True:
        print('''
        1 - Add an Employee.
        2 - Read the Employee information's.
        3 - Update the Employee information's.
        4 - Delete an Employee.
        5 - Read all the Employees information's
        6 - Create a report of the Employees with age superior to twenty-five years.
        7 - Create a report of the Employees with age between twenty-two
        and thirty-five years with salary above R$3700,00.\n         
        ''')

        try:
            user_option = int(input("Select one option between one and seven. Input the number zero to finish the program.\n"))
        except ValueError:
            print("Only integer values are accepted.")
        else:
            match user_option:
                case 1:
                    add_employee()
                case 2:
                    read_specific_employee_info()
                case 3:
                    update_employee_info()
                case 4:
                    print("4")
                case 5:
                    read_all_employees()
                case 6:
                    print("6")
                case 7:
                    print("7")
                case _:
                    print("Another one")

def add_employee():
    try:
        employee_code = int(input("Write the employee unique code:\n"))
        employee_name = input("Write the name of the employee:\n")
        employee_age = int(input("Write the age of the employee:\n"))
        employee_salary = float(input("Write the salary of the employee:\n"))

    except ValueError:
        print("You might write only numbers to code, age and salary request's.\n")
    else:
        employee = {
            'Code': employee_code,
            'Name': employee_name,
            'Age': employee_age,
            'Salary': employee_salary
        }
        employees.append(employee)
    finally:
        print("Employee created with success.")

def read_all_employees():
    if employees is None:
        print("No person was added to the list.")
    else:
        for employee in employees:
            for key, value in employee.items():
                print(f"{key}: {value}.")
            print("-" * 50)

def read_specific_employee_info():
    index = int(input("Prompt the index of the employee that you want to read: "))
    try:
        selected_employee = employees[index]
    except IndexError:
        print("You should prompt an existent index.")
    else:
        for key, value in selected_employee.items():
            print(f"{key}: {value}")
        print("-" * 50)

def update_employee_info():
    index = int(input("Prompt the index of the employee that you want to read: "))
    try:
        selected_employee = employees[index]
    except IndexError:
        print("You should prompt an existent index.")
    else:
        print('''
        1 - Code.
        2 - Name.
        3 - Age.
        4 - Salary
        ''')
        user_chosen_key = int(input("Select the key that you may want to change: "))
        try:
            match user_chosen_key:
                case 1:
                    print(f"The current code stored is: {employees[index]['Code']}")
                    employees[index]['Code'] = int(input("Prompt the new employee code."))
                case 2:
                    print(f"The current name stored is: {employees[index]['Name']}")
                    employees[index]['Name'] = int(input("Prompt the new employee name."))
                case 3:
                    print(f"The current age stored is: {employees[index]['Age']}")
                    employees[index]['Age'] = int(input("Prompt the new employee age."))
                case 4:
                    print(f"The current salary stored is: {employees[index]['Salary']}")
                    employees[index]['Salary'] = int(input("Prompt the new employee salary."))
                case _:
                    print("Select a valid key.")
        except ValueError:
            print("You might write only numbers to code, age and salary request's.\n")
if __name__ == '__main__':
    main()