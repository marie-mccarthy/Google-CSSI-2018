def greetAgent():
    print("Bond, James Bond.")
for i in range (5):
    greetAgent()

def greeting(first_name, last_name):
    return str("%s, %s, %s" %
    (last_name, first_name, last_name))


print(greeting("Marie", "McCarthy"))
print(greeting("Janet", "Snakehole"))
agent1 = greeting("Bert", "Macklin")

print(agent1)

agents = [greeting("Leslie", "Knope"), greeting("Ron", "Swanson")]
print(agents)
agents[0] = "Shannon"
print(agents)

agents.append("Damon")
agents.append("Katie")

print(agents)
print(len(agents))
for i in range(len(agents)):
    print(agents[i])
agents.reverse()
for a in agents:
    print(a)
if "Damon " in agents:
    print("congrats")
agents.remove("Shannon")
agents.remove(agents[len(agents)-1])

#agents.append[25] = ("Julissa")

states = {
    "NJ":"New Jersey",
    "VI":"Vermont",
    "WA":"Washington",
    "TX":"Texas",

}
print (states["NJ"][1].upper())
print states
print(states)
for abbrv in states:
#    print(abbrv)
#    print(states[abbrv])
    if"Washington" == states[abbrv]:
        print("we found it ")
        print("the key is " + abbrv)
