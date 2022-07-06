
import menu


profit = 0


def is_res_sufficint(order_ingredients):
    '''Returns True when order can be made or False if ingredients are insufficinet '''
    for item in order_ingredients:
        if order_ingredients[item] > menu.resources[item]:
            print(f"Sorry there is no enough {item}.")
            return False
    return True


def process_coins():
    '''Returns total calculated coins inserted'''
    print("Please Insert Coins")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.5
    total += int(input("how many pennies?: ")) * 0.01
    return total


def is_tansaction_success(money_recieved, cost_drink):
    '''Returns True if money is sufficient or False if money is insufficient'''
    if money_recieved >= cost_drink:
        change = round(money_recieved - cost_drink, 2)
        print(f"Here is ${change} is change")
        global profit
        profit += cost_drink
        print("Transaction Successfull")
        return True
    else:
        print("Sorry! That's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    '''Deduct the resources from the ingredients'''
    for item in order_ingredients:
        menu.resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


is_on = True
while is_on:
    choice = input(
        "What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off" or choice == "exit":
        is_on = False
    elif choice == "report":
        print(f"Water: {menu.resources['water']} ml")
        print(f"Milk: {menu.resources['milk']} ml")
        print(f"Coffee: {menu.resources['coffee']} g")
        print(f"Money: ${profit}")
    else:
        drink = menu.MENU[choice]
        if is_res_sufficint(drink["ingredients"]):
            payment = process_coins()
            if is_tansaction_success(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
