class Employee():

    def __init__(self, emp_id, name, telphone_number, address, email_address):
        self.emp_id = emp_id
        self.name = name
        self.telphone_number = telphone_number
        self.address = address
        self.email_address = email_address

    def get_emp_id(self):
        return self.emp_id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_telphone_number(self):
        return self.telphone_number

    def set_telphone_number(self, telphone_number):
        self.telphone_number = telphone_number

    def get_address(self):
        return self.address

    def set_address(self, address):
        self.address = address

    def get_email_address(self):
        return self.email_address

    def set_email_address(self, email_address):
        self.email_address = email_address
