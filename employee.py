"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, salary = 0, hours = 0, hourlyPay = 0, commissionPay = 0, number_of_contracts = 0, bonus = 0, totalSalary = 0):
        self.name = name
        self.salary = salary
        self.hours = hours
        self.hourlyPay = hourlyPay
        self.commissionPay = commissionPay
        self.number_of_contracts = number_of_contracts
        self.bonus = bonus
        self.totalSalary = totalSalary

    def get_pay(self):
        if self.salary:
            self.totalSalary += self.salary
        if self.hours:
            self.totalSalary += (self.hours * self.hourlyPay)
        if self.number_of_contracts:
            self.totalSalary += (self.number_of_contracts * self.commissionPay)
        if self.bonus:
            self.totalSalary += self.bonus
        return self.totalSalary

    def __str__(self):
        salaryMessage = self.name

        if self.salary:
            salaryMessage += f" works on a monthly salary of {self.salary}"
        else:
            salaryMessage += f" works on a contract of {self.hours} hours at {self.hourlyPay}/hour"

        if self.number_of_contracts:
            salaryMessage += f" and receives a commission for {self.number_of_contracts} contract(s) at {self.commissionPay}/contract."

        if self.bonus:
            salaryMessage += f" and receives a bonus commission of {self.bonus}."

        if not self.number_of_contracts and not self.bonus:
            salaryMessage += (".")

        salaryMessage += f" Their total pay is {self.totalSalary}."
        return salaryMessage


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', salary = 4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', hours = 100, hourlyPay = 25)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', salary = 3000, commissionPay = 200, number_of_contracts = 4)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', hours = 150, hourlyPay = 25, commissionPay = 220, number_of_contracts = 3)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', salary = 2000, bonus = 1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', hours = 120, hourlyPay = 30, bonus = 600)
