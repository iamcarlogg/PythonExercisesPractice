# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

# Extras:

# If the number is a multiple of 4, print out a different message.
# Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
def odd_even(a):
    if a%4==0:
        print("The number is a multiply of 4 and even")
    elif a%2==0:
        print("The number is even")
    elif a%2!=0:
        print("the number is odd")
def divisible(num, check):
    if num%check == 0:
        print("the number is evenly divisible with " + str(check))
    else:
        print("the number is not evenly divisble")
# a = int(input("Enter a number: "))
# odd_even(a)
# divisible(15,2)

