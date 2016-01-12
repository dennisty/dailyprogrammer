import random

#Designates a name and family info for each person on the secret Santa list
class SecretSanta:

    def __init__(self, name, family, size, giveTo = None, getFrom = None):
        self.name = name
        self.family = family
        self.size = size
        self.giveTo = giveTo
        self.getFrom = getFrom

#Final list of secret santa participants
secretSantaList = []

#Reads through original list and populates final list
familyList = open('secretsanta.txt','r')

for i, line in enumerate(familyList):
    for person in line.split():
        secretSantaList.append(SecretSanta(str(person),int(i),len(line.split())))
        
#Sorts list so largest families get matched first
secretSantaList = sorted(secretSantaList, key = lambda person: person.size, reverse = True)

#Matches people within the secret Santa list
for person in secretSantaList:
    check = 0
    while check == 0:
        receiver = random.choice(secretSantaList)
        if person.family != receiver.family and receiver.getFrom == None and receiver.giveTo != person:
            person.giveTo = receiver
            receiver.getFrom = person
            check += 1

#Outputs secret Santa matches
for person in secretSantaList:
    print person.name, "->", person.giveTo.name
        