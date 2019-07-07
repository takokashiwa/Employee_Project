import employee


class EmployeeList():
    def __init__(self):
        self.employees = []

        self.employees.append(employee.Employee(
            '1', 'Takuma', '080-6924-4663', 'Tokyo', 'takuma167@gmail.com'))
        self.employees.append(employee.Employee(
            '2', 'Akira', '080-6888-4433', 'Tokyo', 'akira167@gmail.com'))

    def show_employee_list(self):
        for emp in self.employees:
            print("{}: {}, {}, {}, {}".format(emp.get_emp_id(), emp.get_name(), emp.get_telphone_number(),
                                              emp.get_address(), emp.get_email_address()))

    def add_employee_list(self):
        new_emp = employee.Employee()
        new_emp.emp_id = input('please type id:')
        new_emp.emp_name = input('please type name:')
        new_emp.telphone_number = input('please type telphone_number:')
        new_emp.address = input('please type address:')
        new_emp.email_address = input('please type email address:')
        self.employees.append(new_emp)
        return self.employees

    def update_employee_list(self):
        emp_id = input('Please type id you want to update:')

        for emp in self.employees:
            if emp.get_emp_id() == emp_id:
                emp.set_name(input(
                    'please type name ({}):'.format(emp.get_name())))
                emp.telphone_number = input(
                    'please type telphone_number ({}):'.format(emp.get_telphone_number()))
                emp.address = input(
                    'please type address ({}):'.format(emp.get_address()))
                emp.email_address = input(
                    'please type email address ({}):'.format(emp.get_email_address()))
                return self.employees
            else:
                print("the id doesn't exist in our database.")
                break

    def delete_employee_list(self):
        delete_id = input('Please type id you want to delete:')

        for emp in self.employees:
            if emp.get_emp_id() == delete_id:
                self.employees.remove(emp)
                break
