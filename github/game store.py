from logging import exception
from datetime import datetime

games={"1":("elder ring",50),
       "2" : ('minecraft',60),
       "3":("stardew Valley",50)}

user = input("please input the user")

print("1.elden ring")
print("2. minecraft ")
print("3. Stardew Valley")
genre = input("please input the game you want to buy 1/2/3")

try:

    clock = datetime.now()
    clock_str = clock.strftime("%d %m %Y %H:%M:%S")

    total = int(input("please input how many copy do you want to buy"))
    game_name , price = games[genre]
    real_price = total * price

    diskon =0
    if total > 2:
        diskon = real_price * 0.10
        real_price -= diskon

    with open("game_struk.txt", "a") as file:
        file.write("======GAME STRUK======\n")
        file.write(f"name          :{user}\n")
        file.write(f"genre game    :{genre}\n")
        file.write(f"how many copy :{total}\n")
        file.write(f"diskon        :{diskon}\n")
        file.write(f"the price     :{real_price}\n")
        file.write(f"clock         :{clock_str}\n")
        file.write("======THANK YOU======\n")

        print("success to input to game_struk.txt")

except exception as e:
    print("there is something wrong in,e")












