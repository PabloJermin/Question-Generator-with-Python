menu = {
    "fufu": {"price": 20,
             "ingredients": {"Cassava": 1,
                             "Plantain": 0.5,
                             "Water": 500}
             },
    "banku": {"price": 15,
              "ingredients": {"Cassava Dough": 2,
                              "Corn Dough": 1.5,
                              "Water": 200}
              },
    "tuo": {"price": 10,
            "ingredients": {"Cassava": 10,
                            "Water": 700}
            },
}

stock = {"Water": 1500,
         "Corn Dough": 300,
         "Plantain": 4,
         "Cassava": 20,
         "Cassava Dough": 50,}


def compare(food_ingredients):
    """A function to compare the stock of ingredients"""
    for i in food_ingredients:
        if food_ingredients[i] >= stock[i]:
            print(f"Sorry there is no enough {i}")
            return False
        else:
            return True


def stock_remain(food_ingredients):
    """Subtracts from the current stock"""
    for i in food_ingredients:
        stock_bal = stock[i] - food_ingredients[i]
        if food_ingredients[i] >= stock[i]:
            print(f"Sorry there is no enough {i}")
            return False
        else:
            return True


def currency(amount):
    """A function to calculate to change of a customer"""
    if amount >= menu_price:
        global balance
        balance = amount - menu_price
        return balance
    else:
        print("Sorry, your money is not enough for this food")
        global is_order
        is_order = False
        return False

balance = 0
food = [""]
choice = input("What do you want?")

if choice == "off":
    is_order = False
elif choice == "report" :
    print(f"The amount of water left is {stock['Water']}")
    print(f"The amount of Corn Dough left is {stock['Corn Dough']}")
    print(f"The amount of plantain left is {stock['Plantain']}")
    print(f"The amount of cassava left is {stock['Cassava']}")
    print(f"The amount of Cassava dough left is {stock['Cassava Dough']}")
    print(f"The amount of money left {balance}")
else:
    food = menu[choice]
    food_ingredients = food["ingredients"]
    compared = compare(food_ingredients)

    if not compared:
        print(f"Sorry, there is no enough {food_ingredients}")
    else:
        menu_list = menu[choice]
        menu_price = menu_list["price"]
        amount = int(input("how much money do you have?"))
        balance += currency(amount)

    initial_bal = currency(amount)

    print(f"Your change is {initial_bal}")

    order_option = input("would you want another order? Y or N")

    is_order = True
    while is_order:
        if order_option == "y":
            food = input("what else do you want?")
            stock_check = stock_remain(food_ingredients)
            bal_left = currency(balance)
            if stock_check and bal_left:
                print("Your food has been ordered")
            elif not stock_check:
                is_order = False
            elif not bal_left:
                print("you need to top up your money")
                top_up = int(input("How much do you want to top up with?"))
                balance += top_up
            else:
                print("YOur food will be here right away")
            print(f"your money left is {balance}")
            print(f"your food is {food}")
        else:
            is_order = False


