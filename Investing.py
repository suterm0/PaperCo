# Michael Suter
# Assignment 8
# 3/25/20

from StackQ import Stack, Queue

total_qty = 0
total_profit = 0.0
total_sold = 0.0
inventory_qty = Stack()
inventory_price = Stack()
queue_inventory_qty = Queue()
queue_inventory_price = Queue()


def lifo_menu():
    choice = int(input("Enter your choice, between 1-5...>>"))
    while choice >= 1 or choice <= 5:
        if choice == 1:
            qty = int(input("How many shares of this stock have been purchased? >>"))
            price = float(input("What was the cost per share? >>"))
            inventory_price.push(price)
            inventory_qty.push(qty)
            print("Successfully added...")
            total_qty += qty # not sure why this isnt working
            lifo_menu()
        elif choice == 2:
            sell_amount = int(input("How many shares are you planning to sell? >>"))
            if sell_amount > total_qty:
                print("You don't have enough shares...")
            sale = 0.0
            popped = 0
            qty_popped = inventory_qty.pop()  #sends the value popped to the stack
            total_qty -= qty_popped         # subtracts the qty popped from the running total
            price = inventory_price.pop()   # adds price to the stack
            total_sale += (qty_popped * price)  #calculates total sale
            total_popped += qty_popped   # running total of the total amount popped
                                        #not to sure where to go after this point
            return
        elif choice == 3:
            print(f"Your total profit for the shares entered in this cycle is {total_profit}.")
            return
        elif choice == 4:
            print(f"Here is the number of shares you have invested {total_qty}")
            return
        else:
            exit("Goodbye")


def fifo_menu():
    choice = int(input("Enter your choice, between 1-5...>>"))
    while choice >= 1 or choice <= 5:
        if choice == 1:
            qty = int(input("How many shares of this stock have been purchased? >>"))
            price = float(input("What was the cost per share? >>"))
            queue_inventory_price.pushy(price)
            queue_inventory_qty.pushy(qty)
            print("Successfully added...")
            total_qty += qty
        elif choice == 2:
            sell_amount = int(input("How many shares are you planning to sell? >>"))
            if sell_amount > total_qty:
                print("You don't have enough shares...")
            sale = 0.0
            popped = 0
            return
        elif choice == 3:
            print(f"Your total profit for the shares entered in this cycle is {total_profit}.")
            return
        elif choice == 4:
            print(f"Here is the number of shares you have invested {total_qty}")
            return
        else:
            exit("Goodbye")



def choice1():
    print("Hello Investor! Welcome Back, Would you like to record your data using the LIFO(Stack) or FIFO(Queue) today?..")
    answer = input("Please Enter '1' for LIFO(Stack), Enter '2' for FIFO(Queue) or Enter '3' to stop the program.. >>")
    if answer == 1:
        print("""You've selected LIFO
        Enter 1 to record a purchase of shares, 
    Enter 2 to sell a set of shares,
    Enter 3 to see your profit, 
    Enter 4 see the shares you have invested, 
    Enter 5 to Quit""")
        lifo_menu()
    elif answer == 2:
        print("""You've selected FIFO,
        Enter 1 to record a purchase of shares, 
    Enter 2 to sell a set of shares,
    Enter 3 to see your profit, 
    Enter 4 see the quantity of shares you have invested, 
    Enter 5 to Quit""")
        fifo_menu()
    else:
        exit("Got it, Thanks!")


choice1()
