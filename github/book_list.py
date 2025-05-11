books =[]

def show_menu():
    print("\n 1 adding books")
    print("2 book list")
    print("3 search book")
    print("4 buying book")
    print("5 exiting")

def adding_books():
    title = input("please input the title")
    author = input("please input the author name")
    price = int(input("how much is teh book"))
    stock = int(input("how many stock left"))

    book ={"title":title ,"author": author , "price":price , "stock":stock }
    books.append(book)
    print("success adding books")

def book_list():
    for i ,  b in enumerate(books , start=1):
        print(f"{i} ,title: {b['title']},author: {b['author']},price= {b['price']},stock: {b['stock']}")

def search_book():
    keyword = input("please input the title")
    found = False

    for b in books:
        if keyword == b['title']:
            print(f"title : {b['title']} , author  : {b['author']} , price = {b['price']}  , stock :{b['stock']}")
            found = True

def buying_book():
    book_list()
    if not books:
        return
    try:
        choice = int(input("please input the book number"))
        if 1<= choice <= len(books):
            b = books.pop(choice -1)
            if b['stock'] >0:
                b['stock']-=1
            else:
                print("the book stock is empty ")
            print("you success buying a book ")
            print(f"title : {b['title']} , author  : {b['author']} , price = {b['price']}  , stock :{b['stock']}")
    except ValueError:
        print("Please enter a valid number.")

while True:
    show_menu()
    choice = input ("please input the number")

    if choice=="1":
        adding_books()
    elif choice =="2":
        book_list()
    elif choice=="3":
        search_book()
    elif choice=="4":
        buying_book()
    elif choice=="5":
        print("exitting....")
        break
    else:
        print("please enter the right number")




