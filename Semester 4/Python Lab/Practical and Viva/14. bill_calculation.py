"""
Write a program to calculate electricity bill according to following criteria
i. first 10 units then no charge
ii. next 100 units - 5 rs per unit
iii. next 200 units - 10 rs per unit
"""

units=int(input("Enter the units consumed: "))


if(units<=10):
    print("No Charge") 
elif(units<=110):
    print("Bill is ",(units-10)," units * 5 i.e.",(units-10)*5)
elif(units<=310):
    print("Bill is (100 units *5) +",(units-110),"units * 10 i.e.", (100*5)+(units-110)*10)
else:
    print("Enter Units that are less than 310")