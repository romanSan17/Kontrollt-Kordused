#1
for n in range(0,10,1):
    n=""" ^---^
( o o )
! = !/)

"""
    print (f"{n:7}", end=" ")
    print()


#2
n=int(input("valige number:"))
aste=int(input("millisel määral:"))
vastus=n ** aste
if vastus<n*100:
    print(vastus)
else:
    print("liiga suur number")


#3
#from random import randint


#4
ameba=2**2
for i in range(0,27,3):
    print(ameba**2, "after", i, "hours")
