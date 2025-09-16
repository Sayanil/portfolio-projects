'''
1 for snake
-1 for water
0 for gun
'''
import random#random package
computer=random.choice([-1,1,0]) #choose a random number
you=input("enter your choice ")#take input from user in s,g, w
youdict={"s":1,"w":-1,"g":0}#convert it into number form
younum=youdict[you]#store that number
youreserved={1:"snake",-1:"water",0:"gun"}#assign ke wakt CURLY BRACKET ,define ke wakt SQUARE BRACKET
print(f"you chose {youreserved[younum]} \ncomputer chose {youreserved[computer]}")
if(computer==younum):
    print("its a draw")
else:
    if(computer==1 and younum==-1):
        print("you loose")
    elif(computer==1 and younum==0):
        print("you win")
    elif(computer==-1 and younum==1):
        print("you win")
    elif(computer==-1 and younum==0):
        print("you loose")
    elif(computer==0 and younum==1):
        print("you loose")
    elif(computer==0 and younum==-1):
        print("you win")
    else:
        print("error")                    