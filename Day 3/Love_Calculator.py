# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

new_name=name1+name2
new_name = new_name.lower()
count1=0
count2=0
count1+=new_name.count('t')
count1+=new_name.count('r')
count1+=new_name.count('u')
count1+=new_name.count('e')
count2+=new_name.count('l')
count2+=new_name.count('o')
count2+=new_name.count('v')
count2+=new_name.count('e')

count1*=10
total=count1+count2
if total<10 or total>90:
    print(f"Your score is {total}, you go together like coke and mentos.")
elif total<50 and total>40:
    print(f"Your score is {total}, you are alright together.")
else:
    print(f"Your score is {total}.")