class MenuItem:
    def __init__(self, name, ingredients, cost):
        self.name = name
        self.ingredients = ingredients
        self.cost = cost

class Menu:
    def __init__(self):
        self.items = {}

    def add_item(self, item):
        self.items[item.name] = item

    def get_items(self):
        return list(self.items.keys())

    def find_drink(self, order_name):
        drink = self.items.get(order_name)
        return drink

class CoffeeMachine:
    def __init__(self, resources):
        self.resources = resources
        self.money = 0
        self.turn_on = True

    def turn_off(self):
        print("Turning off. Goodbye")
        self.turn_on = False
        return self.turn_on

    def print_report(self):
        for (item, value) in self.resources.items():
            if item == "coffee":
                print(f"{item.capitalize()}: {value}g")
            else:
                print(f"{item.capitalize()}: {value}ml")
        print(f"Money: ${self.money}")


    def is_resource_sufficient(self, drink):
        for ingredient in drink.ingredients:
            get_resource = self.resources.get(ingredient)
            if drink.ingredients[ingredient] > get_resource:
                print(f"Sorry there is not enough {ingredient}.")
                return False
        return  True

    def make_coffee(self, order):
        if self.is_resource_sufficient(order):
            print(f"Making {order.name}")
            for ingredient in order.ingredients:
                self.resources[ingredient] -= order.ingredients[ingredient]
        else:
            print(f"Sorry, we can't make {order.name}")

    def calculate_change(self, total, cost):
        return float(total - cost)


    def make_payment(self, coins, input_drink):
        quarters = coins["quarters"]
        dimes = coins["dimes"]
        nickles = coins["nickles"]
        pennies = coins["pennies"]
        total = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
        drink_cost = input_drink.cost
        if total < drink_cost:
            print("Sorry that's not enough money. Money refunded.")
            return False
        change = self.calculate_change(total, drink_cost)
        self.money += drink_cost
        if change > 0:
            print(f"Here's {change} in change.")
        return True

f_resources = {
    "water": 3000,
    "milk": 2000,
    "coffee": 1000
}

coffee_machine = CoffeeMachine(f_resources)
espresso = MenuItem("espresso", {"water": 50, "coffee": 18}, 1.5)
latte = MenuItem("latte", {"water": 200, "coffee": 24, "milk": 150}, 2.5)
cappuccino = MenuItem("cappuccino", {"water": 250, "coffee": 24, "milk": 100}, 3.0)

menu = Menu()
menu.add_item(espresso)
menu.add_item(latte)
menu.add_item(cappuccino)

def coffee_program_init():
    while coffee_machine.turn_on:
        try:
            client_input = input(f"What would you like? {'/'.join(menu.get_items())}: ").lower()

            if client_input == "turn off":
                coffee_machine.turn_off()
                break

            if client_input == "report":
                coffee_machine.print_report()
                continue

            input_drink = menu.find_drink(client_input)

            if not coffee_machine.is_resource_sufficient(input_drink):
                continue

            print("Please insert coins.")
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickles = int(input("How many nickles?: "))
            pennies = int(input("How many pennies?: "))

            coins = {
                "quarters": quarters,
                "dimes": dimes,
                "nickles": nickles,
                "pennies": pennies
            }

            if not coffee_machine.make_payment(coins, input_drink):
                continue

            coffee_machine.make_coffee(input_drink)

            continue
        except TypeError:
            print("Command not valid. Try again")
        continue


coffee_program_init()