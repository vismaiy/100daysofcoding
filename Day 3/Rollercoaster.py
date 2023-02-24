print("Welcome to the rollercoaster!")
height=int(input("Enter the height in cm "))
if height>=120:
    Bill=0
    print("You can ride the rollercoaster")
    age= int(input("Enter your age "))
    if age<12:
        print("Child tickets are $5.")
        Bill=5
    elif age<=18:
        print("Youth tickets are $7.")
        Bill=7
    else:
        print("Adult tickets are $12.")
        Bill=12
    wants_photo=input("Do you want a photo? Reply with Y/N ")
    if wants_photo == 'Y' or wants_photo == 'y':
        print(f"Your final bill is ${Bill+3}")
    if wants_photo == 'N' or wants_photo == 'n':
        print(f"Your final bill is ${Bill}")
else:
    print("You cannot ride!!")