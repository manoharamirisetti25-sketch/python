
venue = 5000
equipment = 3000
transport = 2000

catering = 150
certificate = 50

sponsorship = 5000
registration_fee = 300

participants = int(input("Enter number of participants: "))

fixed_cost = venue + equipment + transport

variable_cost = participants * (catering + certificate)

total_expenses = fixed_cost + variable_cost

registration_income = participants * registration_fee

total_income = registration_income + sponsorship

print("\n--- CAMPUS EVENT FINANCIAL REPORT ---")

print("Participants:", participants)
print("Fixed Expenses:", fixed_cost)
print("Variable Expenses:", variable_cost)
print("Total Expenses:", total_expenses)
print("Registration Income:", registration_income)
print("Sponsorship:", sponsorship)
print("Total Income:", total_income)

if total_income >= total_expenses:
    surplus = total_income - total_expenses
    print("Surplus: Rs.", surplus)
else:
    shortfall = total_expenses - total_income
    print("Shortfall: Rs.", shortfall)

contribution_per_person = registration_fee - catering - certificate

minimum_registrations = (fixed_cost - sponsorship) / contribution_per_person

print("Minimum Registrations Required:",
      int(minimum_registrations))
