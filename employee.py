"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, salary, hours, type_of_contract, type_of_commission, commission_salary, number_of_contracts):
        self.name = name
        self.salary = salary
        self.hours = hours
        self.type_of_contract = type_of_contract
        self.type_of_commission = type_of_commission
        self.commission_salary = commission_salary
        self.number_of_contracts = number_of_contracts

    def get_pay(self):
        pay = calculateSalary(self.type_of_contract, self.hours) + calculateCommission(self.commission_salary,self.number_of_contracts)
        return pay

    def __str__(self):
        return self.name

    def calculateSalary(type_of_contract, hours):
        if type_of_contract == "monthly":
            salary_pay = self.salary
        else:
            salary_pay = self.salary * self.hours
        return salary_pay

    def calculateCommission(commission_salary,number_of_contracts):
        if type_of_commission == "fixed":
            commissionPay = commission_salary
        else:
            commissionPay = commission_salary * number_of_contracts
        return commissionPay


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', '4000', 'none', 'monthly', 'none', 'none', 'none')

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', '25', '100', 'hourly','none', 'none', 'none')

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', '3000', 'none', 'monthly', 'contracted', '200', '4')

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', '25', '150', 'hourly', 'contracted', '220', '3')

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', '2000', 'none', 'monthly', 'fixed', '1500', 'none')

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', '30', '120', 'hourly', 'fixed', '600', 'none')

print (get_pay(billie))
