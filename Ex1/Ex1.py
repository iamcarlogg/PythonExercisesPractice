#  Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old. Note: for this exercise, the expectation is that you explicitly write out the year (and therefore be out of date the next year). If you want to do this in a generic way, see exercise 39.

#  Extras:

#  Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
#  Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)


#  Solution:
def wait():
     input("press enter to continue")

name = input("enter your name: ")
wait()
age = int(input("enter your age: "))
# year = actual year | you can manually change the year
year = int(2024)
wait()
year_100 = (100-age) + 2024
print("Hi," + name + " You're gonna turn 100 on " + str(year_100) )
wait()
num = int(input(name + "enter a random number please: "))
for x in range(num):
    print("The same message\n")