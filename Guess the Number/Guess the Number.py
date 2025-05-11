import random

rd  = random.randint(1, 200)

while True:
    user_no = input("your number or Quit(Q): ")
    if(user_no == "Q"):
        break

    user_no = int(user_no)
    if(user_no == rd):
        print("sucessful")
        break
    elif(user_no < rd):
        print("your no. is smaller")

    else:
        print("your number is  bigger")

print("-----GAME-OVER-----")

