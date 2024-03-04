EXP6 = ["Studying","Dancing","Sing","ab"]

def add_string(element):
    length = len(element)

    if length > 2 :
        if element[3:]=="ing":
            element += "ly"
        else:
            element += "ing"

    return element


for i in range(len(EXP6)):
    element=EXP6[i]
    EXP6[i]=add_string(element)

print(EXP6)
