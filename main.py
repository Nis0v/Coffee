have = {'water': 400,
        'milk': 540,
        'coffee': 120,
        'cups': 9,
        'money': 550,
        }
espresso = {
    'water': 250,
    'coffee': 16,
    'money': 4,
    }
latte = {
    'water': 350,
    'milk': 75,
    'coffee': 20,
    'money': 7,
    }
cappuccino = {
    'water': 200,
    'milk': 100,
    'coffee': 12,
    'money': 6,
    }
Active = True
n_1 = "I have enough resources, making you a coffee!"
def printC():
    print(f"\nThe coffee machine has: ")
    print(f"{have['water']} ml of water")
    print(f"{have['milk']} ml of milk")
    print(f"{have['coffee']} g of coffee beans")
    print(f"{have['cups']} disposable cups")
    print(f"${have['money']} of money")

def act_buy():
    buy_1 = input("\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n")
    if buy_1 == '1':
        if have['water'] // espresso['water'] < 1:
            print("Sorry, not enough water!")
        elif have['coffee'] // espresso['coffee'] < 1:
            print("Sorry, not enough coffee!")
        elif have['cups'] // 1 < 1:
            print("Sorry, not enough cups!")
        else:
            have['water'] -= espresso["water"]
            have['coffee'] -= espresso["coffee"]
            have['cups'] -= 1
            have['money'] += espresso["money"]
            print(n_1)
    elif buy_1 == '2':
        if have['water'] // latte['water'] < 1:
            print("Sorry, not enough water!")
        elif have['milk'] // latte['milk'] < 1:
            print("Sorry, not enough milk!")
        elif have['coffee'] // latte['coffee'] < 1:
            print("Sorry, not enough coffee!")
        elif have['cups'] // 1 < 1:
            print("Sorry, not enough cups!")
        else:
            have['water'] -= latte["water"]
            have['milk'] -= latte["milk"]
            have['coffee'] -= latte["coffee"]
            have['cups'] -= 1
            have['money'] += latte["money"]
            print(n_1)
    elif buy_1 == '3':
        if have['water'] // cappuccino['water'] < 1:
            print("Sorry, not enough water!")
        elif have['milk'] // cappuccino['milk'] < 1:
            print("Sorry, not enough milk!")
        elif have['coffee'] // cappuccino['coffee'] < 1:
            print("Sorry, not enough coffee!")
        elif have['cups'] // 1 < 1:
            print("Sorry, not enough cups!")
        else:
            have['water'] -= cappuccino["water"]
            have['milk'] -= cappuccino["milk"]
            have['coffee'] -= cappuccino["coffee"]
            have['cups'] -= 1
            have['money'] += cappuccino["money"]
            print(n_1)
    elif buy_1 == 'back':
        return
def act_fill():
    have['water'] += int(input("Write how many ml of water you want to add:\n"))
    have['milk'] += int(input("Write how many ml of milk you want to add:\n"))
    have['coffee'] += int(input("Write how many grams of coffee beans you want to add:\n"))
    have['cups'] += int(input("Write how many disposable cups you want to add:\n"))
    return
def act_take():
    print(f"I give you ${have['money']}")
    have['money'] -= have['money']
    return

def act_exit():
    global Active
    Active = False
    return

def action():
    while Active:
        act = input("\nWrite action (buy, fill, take, remaining, exit):\n")
        if act == 'buy':
            act_buy()
        elif act == 'fill':
            act_fill()
        elif act == 'take':
            act_take()
        elif act == 'remaining':
            printC()
        elif act == 'exit':
            break
action()
