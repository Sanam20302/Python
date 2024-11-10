itemlist = []

class shop:
    def __init__(self,name,price):
        self.name = name
        self.price = price
        itemlist.append(self)
    def getname(self):
        print("Name of item is : {}".format(self.name))
    def getprice(self):
        print("Price of item is : ${}".format(self.price))

class cart:
    def __init__(self):
        self.cart = []
    def additem(self,item):
        for elem in itemlist:
            if elem.name == item:
                self.cart.append(elem)
                print("\n{} is added to the cart.\n".format(elem.name))
                break
        else:
            print("Item not found")
    def removeitem(self,item):
        for elem in self.cart:
            if elem.name == item:
                self.cart.remove(elem)
                print("\n{} is removed from the cart.\n".format(elem.name))
        else:
            print("Item not found\n")
    def showcart(self):
        if not self.cart:
            print("\nCart is empty\n")
            return
        else:
            print("\nThese are the items in the cart :")
            for items in self.cart:
                print("{} - ${:.2f}".format(items.name,items.price))
            print()
    def showtotal(self):
        total = sum(item.price for item in self.cart)
        print("\nTotal amount: ${:.2f}\n".format(total))
    def clearcart(self):
        self.cart.clear()
        print("\nCart is now empty.\n")

def staff():
    print("\nServer update in progress.\nPease do staff operations manually.\nThank you.\n")
    boot()

item1 = shop("Pen",10)
item2 = shop("Pencil",10)
item3 = shop("Book",40)
item4 = shop("Bottle",100)
item5 = shop("Umbrella",200)

def shopping():
    
    done= True
    c = cart()
    while(done):
        print("1.Add item\n2.Remove item\n3.Show cart\n4.Show total\n5.Clear cart\n6.Exit\n")
        ans = input("Enter your choice : ")
        try:
            choice = int(ans)
        except ValueError:
            print("Invalid entry. Please enter a number between 1 and 6.\n")
            continue

        if(choice == 6):
                print("Thank you for coming.")
                boot()

        elif(choice==1):
            for index,elem in enumerate(itemlist,start=1):
                print("{}. {} - ${:.2f}".format(index,elem.name,elem.price))
            claim = input("Enter the item name you want : ").title()
            c.additem(claim)

        elif(choice==2):
            claim = input("What do you want to remove : ").title()
            c.removeitem(claim)

        elif(choice==3):
            c.showcart()

        elif(choice==4):
            c.showtotal()

        elif(choice==5):
            c.clearcart()

        else:
            print("Invalid entry. Please enter a number between 1 and 6.")

def boot():
    print("User or Staff\nType\n\'U\' for User\n\'S\' for Staff\n\'T\' for Turn Off\n")
    ans = input().lower()
    if ans == "u":
        shopping()
    elif ans == "s":
        password = input("Enter the password : ")
        if password == "12345":
            staff()
        else:
            print("Invalid password.\n")
            boot()
    elif ans == "t":
        quit()
    else:
        print("\nInvalid entry.\n")
        boot()

boot()
