word = raw_input("What word do you want to make plural?")
number = raw_input("enter how many:")

if word[-2:] == "ay" or word[-2:] == "oy" or word[-2:] == "ey" or word[-2:] == "uy":
    print(number + " " + word + "s")
elif word[-2:] == "ch" or word[-2:] == "sh":
    print(number + " " + word + "es")
elif word[-1:] == "y":
    print(number + " " + word[:-1] + "ies")
elif word[-3:] == "ife":
    print(number + " " + word[:-3] + "ives")
elif word[-2:] == "us":
    print(number + " " + word[:-2] + "i")
else:
    print(number + " " + word + "s")
