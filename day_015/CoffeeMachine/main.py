MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,

        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

report = []
dispense_drink = False
is_machine_on = True

def fetch_flavour(flavour):
    flavour_details = []
    flavour_item = MENU[flavour]
    flavour_ingredients = flavour_item["ingredients"]
    flavour_cost = flavour_item["cost"]
    flavour_details.append(flavour_ingredients["water"])
    flavour_details.append(flavour_ingredients["milk"])
    flavour_details.append(flavour_ingredients["coffee"])
    flavour_details.append(flavour_cost)
    return flavour_details

#TODO 2: Create a report variable that fetches resources from the data

def create_report(resources):
    report.append(resources["water"])
    report.append(resources["milk"])
    report.append(resources["coffee"])
    report.append(0)


def print_report():
    print(f"Water: {report[0]}ml")
    print(f"Milk: {report[1]}ml")
    print(f"Coffee: {report[2]}g")
    print(f"Money: ${report[3]}")


def check_ingredient(choice):
    for i in range(0, 3):
        if choice[i] > report[i]:
            askForCoin = False
            if i == 0:
                print("Sorry, there is not enough water")
            elif i == 1:
                print("Sorry, there is not enough milk")
            elif i == 2:
                print("Sorry, there is not enough coffee")
            return askForCoin
        else:
            askForCoin = True
    return askForCoin

def calculate_coin(quarters, dimes, nickles, pennies):
    quarters_calculated = quarters * 0.25
    dimes_calculated = dimes * 0.1
    nickles_calculated = nickles * 0.05
    pennies_calculated = pennies * 0.01
    unrounded_total_coin = quarters_calculated + dimes_calculated + nickles_calculated + pennies_calculated
    total_coin = round(unrounded_total_coin, 2)
    report.append(total_coin)
    return total_coin


def process_payment(flavour, total_coin):
    if round(total_coin, 1) == flavour[3]:
        dispense_drink = True
    elif total_coin > flavour[3]:
        dispense_drink = True
        change = round(total_coin - flavour[3], 2)
        print(f"Here is ${change} in change.")
    else:
        print("Sorry, that's not enough money. Money refunded")
        dispense_drink = False
    report[3] += flavour[3]
    return dispense_drink

espresso = fetch_flavour("espresso")
latte = fetch_flavour("latte")
cappuccino = fetch_flavour("cappuccino")
create_report(resources)

while is_machine_on:
    choice = input("What would you like? (espresso/latte/cappuccino): " ).lower()
    if choice == "off":
        is_machine_on = False
        askForCoin = False
    elif choice == "report":
        print_report()
        askForCoin = False
    elif choice == "espresso":
        choice_flavour = espresso
        askForCoin = check_ingredient(espresso)
    elif choice == "latte":
        choice_flavour = latte
        askForCoin = check_ingredient(latte)
    elif choice == "cappuccino":
        choice_flavour = cappuccino
        askForCoin = check_ingredient(cappuccino)

    if askForCoin:
        print("Please insert coins.")
        quarters = int(input("how many quarters?: "))
        dimes = int(input("how many dimes?: "))
        nickles = int(input("how many nickles?: "))
        pennies = int(input("how many pennies?: "))
        total_coin = calculate_coin(quarters, dimes, nickles, pennies)
        dispense_drink = process_payment(choice_flavour, total_coin)



        if dispense_drink:
            report[0] -= choice_flavour[0]
            report[1] -= choice_flavour[1]
            report[2] -= choice_flavour[2]
            print(f"Here is your {choice} ☕ Enjoy!")

