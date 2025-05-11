book = []

def rewrite_guest():
    total = int(input("please input how many guest you want to rewrite"))
    with open("guest_book.txt","w") as file:
        for i in range(total):
            name = input(f"guest no {i}")
            file.write(f"guest number {i} : {name}\n")
    print("success to rewrite the guest in guest book")

def adding_guest():
    name = input("please input the name you want to add")
    with open("guest_book.txt","a") as file:
        file.write(f"name : {name}\n")
        print("success to add")

def list_guest():
    try:
        with open("guest_book.txt","r") as file:
            list = file.readlines()
            for i , name in enumerate(list,start=1):
                print("====== GUEST BOOK ======")
                print(f"{i} {name.strip()}\n")

    except FileNotFoundError:
        print("the file is not found ")

def show_menu():
    print("====== GUEST BOOK ======")
    print("1. write the guest menu ")
    print("2. adding guest")
    print("3. list guest ")
    print("4. exit.....")

while True:
    show_menu()
    try:
        enter = int(input("Please input the number 1/2/3/4: "))
        if enter == 1:
            rewrite_guest()
        elif enter == 2:
            adding_guest()
        elif enter == 3:
            list_guest()
        elif enter == 4:
            print("👋 Exit...")
            break
        else:
            print("❌ Please enter a valid number.")
    except ValueError:
        print("⚠️ Input must be a number.")