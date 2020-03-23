# Michael Suter
# using stack, apply it to scenario
# 3-10-20

from StackQ import Stack


def menu():
    inventory = Stack()
    choice = int(input("Enter a number between 1-5... >>"))
    while choice >= 1 or choice <= 5:
        if choice == 1:
            qty = int(input("How many cases of paper would you like to add to inventory? >>"))
            price = int(input("What is the individual cost of these cases? >> $"))
            inventory.push(qty)
            cost = price * qty
            print(f"The cost of this order is ${cost}")
            print(f"there are now {qty} more cases of paper in the inventory worth {cost}")
            menu()
        elif choice == 2:
            print("Take a look at the inventory below...")
            print(inventory.the_stack)
            sell_amount = int(input(f"How many cases of paper do you want to sell out of the inventory? >>"))
            sell_price = int(input("How much are you selling each case for?>>"))
            total_sale = sell_amount * sell_price
            revenue = total_sale - cost
            print(f"You just sold {sell_amount} cases for {total_sale}")
            inventory.pop()
            menu()
        elif choice == 3:
            print(f"the total revenue is {revenue}.")
            menu()
        else:
            if choice == 4:
                print("Here is a list of cases left in the inventory", inventory.the_stack)
                menu()


print("""Enter 1 to add, 
    Enter 2 to sell,
    Enter 3 to see profit, 
    Enter 4 see the amount of cases in inventory, 
    Enter 5 to Quit""")

menu()
