"""print("running Lesson2.py")
name1 = "Joe"
name2 = "Mary"
name3 = "Aimee"
name4 = "Will"

print("Hi %s, %s, %s, and %s" %
    (name1, name2, name3, name4))
print("My favorite number is %s" % 7)"""

again = "y"

while again == "y":
    num = int(raw_input("enter a number:"))
    if num > 0:
        print("this is a positive number")
    elif num < 0:
        print("this is a negitive number")
    else:
        print("this is 0")
    if num % 2 == 0:
        print ("this is an even number")
    else:
        print("this is odd")
    again = raw_input("Would you like to try again?""y/n")


"""
word = "Marie"
for xyz in word:
    print(xyz.upper())

for i in range(0, 1, 5):
    print (i)
"""
