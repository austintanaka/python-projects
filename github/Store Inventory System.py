inventory = []

def show_menu():
    print("====== INVENTORY SYSTEM ======")
    print("1. add item")
    print("2. show item")
    print("3. search item")
    print("4. update item")
    print("5. delete item")
    print("6. show total value")
    print("7. exit...")
    print("==============================")


def add_item():
    name = input("item name :")
    stock = int(input("how many the stock is"))
    price = int(input("how much is the price"))

    item = {"name":name , "stock":stock , "price": price}
    inventory.append(item)
    print("success to add item ")
    save_data()

    for s in inventory:
        with open("stock.txt", "w") as file:
            file.write("====== INVENTORY SYSTEM ======\n")
            file.write(f"name : {s['name']}\n")
            file.write(f"stock : {s['stock']}\n")
            file.write(f"price : {s['price']}\n")

            print("success to add into txt")


def save_data():
    for s in inventory:
        with open("stock.txt", "a") as file:
            file.write("====== INVENTORY SYSTEM ======\n")
            file.write(f"name : {s['name']}\n")
            file.write(f"stock : {s['stock']}\n")
            file.write(f"price : {s['price']}\n")

            print("success to add into txt")


def show_item():
    for i , s in enumerate(inventory,start=1):
        print(f"{i} ,  name :{s['name']}  stock : {s['stock']}  price : {s['price']}")


def search_item():
    keyword = input("please input the brand name")
    found = False

    for s in inventory:
        if keyword == s['name']:
            print(f"name :{s['name']}  stock : {s['stock']}  price : {s['price']}")
            found = True

def update_item():
    keyword = input("please input the data you want to update")
    found = False

    for s in inventory:
        if keyword == s['name'].lower():
            print(f"name :{s['name']}  stock : {s['stock']}  price : {s['price']}")
            found = True

            new_stock = int(input("please input the new stock"))
            new_price = int(input("please input the new price"))

            if new_price:
                s['price'] = int(new_price)

            if new_stock:
               s['stock']  = int(new_stock)

               print("item success to update")
               found =True
               break

        if not found:
            print("the item is not found")

def delete_item():
    keyword =  input("please input the item you want to delete")
    found = False

    for i , s in enumerate(inventory):
        if keyword == s['name'].lower():
            del inventory[i]
            print(f"{s['name']}success to delete")
            found = True
            break
    if not found:
        print("the item you want to delete is not found")

def count_item():
    total = 0
    for s in inventory:
        total += s['stock'] * s['price']
        print(f"total value = {total}")

while True:
    show_menu()
    enter = int(input('please input the number 1/2/3/4/5/6/7'))

    if enter ==1:
        add_item()
    elif enter ==2:
        show_item()
    elif enter ==3:
        search_item()
    elif enter ==4:
        update_item()
    elif enter ==5:
        delete_item()
    elif enter ==6:
        count_item()
    elif enter==7:
        print("exit.......")
        break
    else:
        print("please input the right number")

















