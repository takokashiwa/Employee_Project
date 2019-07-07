import employee
import employee_list


employee_list = employee_list.EmployeeList()

while True:
    print('*=====================*')
    print('1. show employee list *')
    print('2. add employee       *')
    print('3. update employee    *')
    print('4. delete employee    *')
    print('5. quit app           *')
    print('*=====================*')
    user_input = input('Plese select number:')

    if user_input == '1':
        employee_list.show_employee_list()

    elif user_input == '2':
        employee_list.add_employee_list()

    elif user_input == '3':
        employee_list.update_employee_list()

    elif user_input == '4':
        employee_list.delete_employee_list()

    elif user_input == '5':
        print('See you again!')
        break
    else:
        print("you input wrong number, please try again!")
