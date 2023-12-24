#answer1

name=input("enter your name :")
print("good afternoon, " + name)

#answer2

letter='''dear <|name|>
greetings : from demon slayer corps you are selected to hunt demons in the world kill uppermoons and muzan too
you are selected
have a great day ahead 
thanks and reguards
demon slayer corps
date:<|date|>
'''

name=input("enter your name\n")
date=input("enter date\n")
letter=letter.replace("<|name|>",name)
letter=letter.replace("<|date|>",date)
print(letter)

#answer 3

raghav="this  is"
doublespaces=raghav.find("  ")
print(doublespaces)

#answer4

raghav="this  is"
doublespaces=raghav.replace(" "," ")
print(doublespaces)
