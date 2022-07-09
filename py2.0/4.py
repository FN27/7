class People:
    def __init__(self, name, work_place, email, phone_number, cash, years_old):
        self.name = name
        self.work_place = work_place
        self.email = email
        self.phone_number = phone_number
        self.cash = cash
        self.years_old = years_old

    def object_information(self):
        print(f"Name: {self.name}, post: {self.work_place}, email: {self.email}, phone number: {self.phone_number}"
              f"salary: {self.cash}, {self.years_old} years old")


Max = People("Max", "Builder", "qwerty@hihi.com", 49876656934, 30000, 56)
Sam = People('Sam', "driver", "zxcvb@hih.com", 65432343456, 25000, 24)
Jake = People('Jake', 'meneger', "dgkk34@hhk.com", 98763452190, 35000, 43)
Kate = People('Kate', 'company owner', 'kate1488@huhu.com', 89265674379, 30000, 41)
Tom = People('Tom', 'assistant', '123ert@hjko.com',97655664321, 12000, 19)
workers=[Max, Sam, Jake, Kate, Tom]
middele_salary = 0
for y in workers:
    middele_salary += y.cash
middele_salary = middele_salary / len(workers)
print(middele_salary)
for y in workers:
    if y.cash >= middele_salary:
        y.object_information()