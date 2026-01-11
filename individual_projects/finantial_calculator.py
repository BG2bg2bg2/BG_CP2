#BG 1st finantial calculator

#Budget Allocator (use set percentages to divide an income into spending categories like savings, entertainment, and food)

#enter what your job is and how much you are getting payed per month/weekly

#starting menu (menu)
def menu():
# enter a number to select an optoin
    while True:
        print("1 = Savings Goal")
        print("2 = Compound Interest")
        print("3 = Budget Allocator")
        print("4 = Sale Price")
        print("5 = Tip")
        print("6 = Exit")# 1 saving time calculif = if:ator ()
        to_calc = input("Enter a number 1-6 to do calculations on that option")
        if to_calc == "":
            savings_goal()
        elif to_calc == "":
            comp_int()
        elif to_calc == "":# 1 saving time calculator = if: you want to save up to a surtain amount of money ()
            bud_allo
        elif to_calc == "":
            sale()
        elif to_calc == "":
            tip()
        elif to_calc == "":
            print("Thankyou for your time.\nGoodbye...")# 1 saving time calculator = if: you want to save up to a surtain amount of money ()
            break
        else:
            print("Invalid")
            print("Try again!!!")
            continue
# 1 saving time calculator = if: you want to save up to a surtain amount of money ()
def save_goal():
    # enter a savings goal how much are you trying to save (save)
    save_to = float(input("Enter your savings goal amount: $"))# 1 saving time calculator = if: you want to save up to a surtain amount of money ()
    deposit = float(input("Enter deposit amount: $"))
    # how often are you saving?
    frequency = input("Do you deposit Weekly or Monthly? (w/m): ").lower
    # w weekly
    if frequency == "w":
        breaks = save_to / deposit# 1 saving time calculator = if: you want to save up to a surtain amount of money ()
        print(f"It will take you about{breaks:.1f} weeks to reach your goal.")
    # m monthly
    elif frequency == "m":
        print(f"It will take you about {breaks:.1f} mounths to reach your goal")
    else:# enter a savings goal how much are you trying to save (save)
        print("Invalid enter a savings goal") # 1 weekly
        # 2 monthly
        # enter how much are you contributing? # 1 saving time calculator = if: you how much are you trying to save (save)lid answer\ntry again")
    # 1 saving time calculator = if: you want to save up to a surtain amount of money()
# 2 compound interest # 1 saving time calculator = if: you want to save up to a surtain amount of money ()calculator ()
def comp_int():
    principal = float(input("Enter initial amount"))
    rate = float(input("Enter annual interest rate (%): ")) /100
    years = int(input ("Enter the number of years: "))
    comp_per_year = int(input("Times compund per year: "))

    def calc_amount():
        return principal * (1 + rate/comp_per_year) ** (comp_per_year * years)
    final_amount = calc_amount()
    print(f"Final amount after {years} years: ${final_amount:.2f}")
# 3 budget allocator (# 1 saving time calculator = if: you want to save up to a surtain amount of money ())
def budget():
    income = float(input("Enter mounthly income: $"))
    saving = int(input("enter what percent are you saving: $"))
    food = int(input("enter what percent are you spending for your food: $"))
    entertainment = int(input("enter what percent are you spending for entertainment: $"))
    other = int(input("enter what percent are other things you might spend on: $"))
    print(f"Savings: ${income * savings:.2f}")
    print(f"Food: ${income * food:.2f}")
    print(f"Entertainment: ${income * entertainment:.2f}")
    print(f"Other: ${income * other:.2f}")
# 4 sale price calculator (if an item is on sale divide it by the percent)
def sale():
    cost = int(input("How much does the item cost: "))
    percent = int(input("What percent is the discount: "))
    print(f"The item now costs {cost / percent}")
# 5 tip clculator (adds how much = if: you have earn from tips/day)
# how often are you saving?

    items = []
    costs = []
    origonal_costs = []
    while True:
        item = input("Enter what is on sale: ")
        items.    items = []
    costs = []
    origonal_costs = []
    while True:
        item = input("Enter what is on sale: ")
        items.append(item)
        origonal_cost = int(input(f"Enter the origonal cost of the {item}: "))
        cost = int(input(f"Enter the percent of the {item} is on sale for: "))
        costs.append(cost).append(item)
        origonal_cost = int(input(f"Enter the origonal cost of the {item}: "))
        cost = int(input(f"Enter the percent of the {item} is on sale for: "))
        costs.append(cost)
    
        
menu()
