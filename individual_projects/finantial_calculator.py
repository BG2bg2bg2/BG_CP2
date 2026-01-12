# Financial  Program
# Provides multiple basic financial calculation tools

def main():
    #Main function that runs the user interface
    while True:
        print("\n1. Savings Goal")
        print("2. Compound Interest")
        print("3. Budget Allocator")
        print("4. Sale Price")
        print("5. Tips")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")
        #if choice is 1 do the savings goal
        if choice == "1":
            savings_goal()
        #if choice is 2 do the compound interest
        elif choice == "2":
            compound_interest()
        #if choice is 3 do budgetting
        elif choice == "3":
            budget_allocator()
        #if choice is 4 do on sale price
        elif choice == "4":
                sale_price()
        #if chioce is 5 do the tip calculator
        elif choice == "5":
                tips()
        elif choice == "6":
                print("Goodbye!")
                break
        else:
            print("Invalid choice. Try again.")


def savings_goal():
    #Calculates how long it will take to reach a savings goal
    goal = float(input("Enter savings goal amount: $"))
    deposit = float(input("Enter deposit amount: $"))
    freuency = input("Deposit weekly or monthly? (w/m): ").lower()

    if freuency == "w":
        periods = goal / deposit
        print(f"It will take about {periods:.1f} weeks to reach your goal.")
    elif freuency == "m":
        periods = goal / deposit
        print(f"It will take about {periods:.1f} months to reach your goal.")
    else:
        print("Invalid frequency choice.")


def compound_interest():
    #compound interest
    principal = float(input("Enter initial amount: $"))
    rate = float(input("Enter annual interest rate (%): ")) / 100
    years = int(input("Enter number of years: "))
    compounds_per_year = int(input("Times compounded per year: "))

    def amount():
        return principal * (1 + rate / compounds_per_year) ** (compounds_per_year * years)

    final_amount = amount()
    print(f"Final amount after {years} years: ${final_amount:.2f}")


def budget_allocator():
    #Budgets what is being spent on
    income = float(input("Enter monthly income: $"))
    #savings
    savings = float(input("Enter what percent are savings"))
    #grogories
    food = float(input("Enter what percent are you spending for food"))
    #entertainment
    entertainment = float(input("Enter what percent are you spending for entertainment"))
    #other things might be spent on
    other = float(input("Enter what percent are you spending on other things like car, gas, car insurence excedera"))

    print("\nbuget spent")
    print(f"Savings: ${income * savings:.2f}")
    print(f"Food: ${income * food:.2f}")
    print(f"Entertainment: ${income * entertainment:.2f}")
    print(f"Other: ${income * other:.2f}")


def sale_price():
    #enter the origianl price
    price = float(input("Enter original price: $"))
    #enter the dicount
    discount = float(input("Enter discount percentage: ")) / 100
    #calculates the final after discount
    final_price = price * (1 - discount)
    #display final price
    print(f"Final price after discount: ${final_price:.2f}")

    #Calculates the tips and the total bill
def tips():
    #Enter how much you get paid
    bill = float(input("Enter paid amount: $"))
    #Enter what percent are you getting tips in
    tippers = float(input("Enter what is your tip percentage: ")) / 100
    #Calculates 
    tip = bill * tippers
    total = bill + tip


    print(f"Tip amount: ${tip:.2f}")
    print(f"Total ampount paid: ${total:.2f}")


#run program
main()
#End