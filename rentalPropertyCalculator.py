class RentalPropertyCalc():
    def __init__(self):
        self.total_investment = int
        self.total_income = int
        self.total_expense = int
        self.total_cash_flow = int

    def aboutProperty(self):
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
        print("-        Welcome to Bigger Pockets Rental Property ROI Calculator!        -")
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n")
        cost_of_property = input("Please enter the purchase price for the property: $")
        if cost_of_property.isnumeric() == False:
            print("     Please only enter a numeric value for the purchase price of your property.")
            self.aboutProperty()
        else:
            cost_of_property = int(cost_of_property)
        down_payment = input("Planned downpayment for property: $")
        if down_payment.isnumeric() == False:
            print("     Please only enter a numeric value for the downpayment amount of your property.")
            self.aboutProperty()
        else:
            down_payment = int(down_payment)
        closing_costs_automatic = int(cost_of_property * .06)
        print(f"Closing Costs typically range from 3%-6% of the property's purchase price. Based on the worst case scenario (6%) we expect your closing costs to be ${int(closing_costs_automatic)}.")
        choose_closing_costs = input("If you would like to use this number please type [Y], if not type [N] and and follow the promt to enter your own closing costs: ").lower()
        if choose_closing_costs == "y":
            closing_costs_manual = int(0)
        else:
            closing_costs_automatic = int(0)
            closing_costs_manual = input("What are your expected Closing Costs? $")
            if closing_costs_manual.isnumeric() == False:
                print("     Please only enter a numeric value for the closing costs of your property.")
                self.aboutProperty()
            else:
                closing_costs_manual = int(closing_costs_manual)
        reno = input("If you are planning on doing renovations on the property please type [Y], if not type [N]: ").lower()
        if reno != "n":
            reno_budget = int(input("How much are you planning to spend on your renovation/rehab? $"))
        else:
            reno_budget = int(0)
        misc = int(input("What are your other miscellaneous expenses if there are any? $"))
        self.total_investment = down_payment + closing_costs_automatic + closing_costs_manual + reno_budget + misc
        print(f"\nYour total initial investment for this property will be ${self.total_investment}\n")

    def income(self):
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
        print("-           Lets gather some Income information for the property          - ")
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
        rental_income = input("What is the expected Monthly Rental Income: $")
        if rental_income.isnumeric() == False:
            print("     Please only enter a numeric value for the Monthly Rental Income of your property.")
            self.income()
        else:
            rental_income = int(rental_income)    
        laundry_income = input("Expected Monthly Laundry Income: $")
        if laundry_income.isnumeric() == False:
            print("     Please only enter a numeric value for the Monthly Laundry Income of your property.")
            self.income()
        else:
            laundry_income = int(laundry_income)
        storage_income = input("Expected Monthly Storage Income: $")
        if storage_income.isnumeric() == False:
            print("     Please only enter a numeric value for the Monthly Storage Income of your property.")
            self.income()
        else:
            storage_income = int(storage_income)
        misc_income = input("Expected Montly Miscellaneous Income: $")
        if misc_income.isnumeric() == False:
            print("     Please only enter a numeric value for the Monthly Miscellaneous Income of your property.")
            self.income()
        else:
            misc_income = int(misc_income)
        self.total_income = rental_income + laundry_income + storage_income + misc_income
        print(f"\nYour expected Monthly Income is ${self.total_income} for this property.\n")
#
    def expenses(self):
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
        print("-         Let's gather some Expense information for your property         -")
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n")
        tax_expense = input("Expected Montly Tax Expense: $")
        if tax_expense.isnumeric() == False:
            print("     Please only enter a numeric value for the Monthly Tax Expense of your property.")
            self.expenses()
        else:
            tax_expense = int(tax_expense)
        insurance_expense = input("Expected Montly Insurance Expense: $")
        if insurance_expense.isnumeric() == False:
            print("     Please only enter a numeric value for the Monthly Insurance Expense of your property.")
            self.expenses()
        else:
            insurance_expense = int(insurance_expense)
        utilities_expense = input("Expected Montly Utilities Expense: $")
        if utilities_expense.isnumeric() == False:
            print("     Please only enter a numeric value for the Monthly Utilities Expense of your property.")
            self.expenses()
        else:
            utilities_expense = int(utilities_expense)
        hoa_expense = input("Expected Montly Home Owners Association Expense: $")
        if hoa_expense.isnumeric() == False:
            print("     Please only enter a numeric value for the Monthly Home Owners Association Expense of your property.")
            self.expenses()
        else:
            hoa_expense = int(hoa_expense)
        yard_expense = input("Expected Montly Yard Upkeep Expense: $")
        if yard_expense.isnumeric() == False:
            print("     Please only enter a numeric value for the Monthly Yard Upkeep Expense of your property.")
            self.expenses()
        else:
            yard_expense = int(yard_expense)
        vacancy_expense = input("Expected Montly Vacancy Expense: $")
        if vacancy_expense.isnumeric() == False:
            print("     Please only enter a numeric value for the Monthly Vacancy Expense of your property.")
            self.expenses()
        else:
            vacancy_expense = int(vacancy_expense)
        repairs_expense = input("Expected Montly Repairs Expense: $")
        if repairs_expense.isnumeric() == False:
            print("     Please only enter a numeric value for the Monthly Repairs Expense of your property.")
            self.expenses()
        else:
            repairs_expense = int(repairs_expense)
        capital_expense = input("Expected Montly Capital Expense: $")
        if capital_expense.isnumeric() == False:
            print("     Please only enter a numeric value for the Monthly Capital Expense of your property.")
            self.expenses()
        else:
            capital_expense = int(capital_expense)
        management_expense = input("Expected Montly Property Management Expense: $")
        if management_expense.isnumeric() == False:
            print("     Please only enter a numeric value for the Monthly Property Mangement Expense of your property.")
            self.expenses()
        else:
            management_expense = int(management_expense)
        mortgage_expense = input("Expected Montly Mortgage Expense: $")
        if mortgage_expense.isnumeric() == False:
            print("     Please only enter a numeric value for the Monthly Mortgage Expense of your property.")
            self.expenses()
        else:
            mortgage_expense = int(mortgage_expense)
        self.total_expense = tax_expense + insurance_expense + utilities_expense + hoa_expense + yard_expense + vacancy_expense + repairs_expense + capital_expense + management_expense + mortgage_expense
        print(f"\nYour expected Monthly Expenses are ${self.total_expense} for this property.\n")

    def cashFlow(self):
        self.total_cash_flow = self.total_income - self.total_expense
        print(f"Your projected Monthly Cash Flow is ${self.total_cash_flow}\n")

    def cashOnCashROI(self):
        annual_cash_flow = self.total_cash_flow * 12
        cash_on_cash_roi = (annual_cash_flow / self.total_investment) * 100
        print(f"Your Cash on Cash Return on Invesment is {cash_on_cash_roi}%\n")
        if cash_on_cash_roi > 8:
            print("There is a consensus amongst investors that a cash return between 8 and 12 percent is a worthwhile investment.  Following that criteria, we would rate this property as a good choice for purchase.")
        else:
            print("This property has a Cash on Cash ROI below 8 percent.  Proceed with caution.\n")
        print("\nThank you for using Bigger Pockets Rental Property ROI Calculator. Have a great day and happy investing!\n")

new_house = RentalPropertyCalc()

def runner():
    new_house.aboutProperty()
    new_house.income()
    new_house.expenses()
    new_house.cashFlow()
    new_house.cashOnCashROI()

runner()