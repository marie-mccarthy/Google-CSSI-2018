print "running..."
def factorial(number):
    anwser = 1
    for i in range(1, number+1):
        anwser = anwser * i
    return anwser
print (factorial(5))
print (factorial(3))
print (factorial(8))

"""
while factorial2(x):
    anwser = 1
    i = 0
    while x > 1:
        i = i + 1
        anwser = anwser * i
    return answer

print (factorial2(5))
"""
ceri = {
    "species": "dog",
    "name": "ceri",
    "sound": "yips",
    "food": ["tuna", "vanilla ice cream"],
    "age": 8
}

petey = {
    "species": "dog",
    "name": "petey",
    "sound": "woof",
    "food": ["peanut butter","steak", "tuna"],
    "age": 9
}
for i in range(len(petey["food"])):
    print("My dog's favorite food is " + petey["food"][i])
 
