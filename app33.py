from math import*
x=int(input("donner une annee :"))
if ((x%4==0)and(x%100!=0)):
    print("Leap year")
else:
    print("non-leap year")


