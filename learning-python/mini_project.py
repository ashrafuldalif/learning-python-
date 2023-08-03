print ("what do you wanna do ? \n press + for add\npress - for subtract \n press * for multiply \n press / for devide \n press p for power \n press r for reminder \n  ")
ans=input(":")
first = input ("first number :")
second = input ("second number :")
a=int (first)
b=int (second)

if ans=='+' :
   print(a+b)
   
elif ans =='-' :
    print(a-b)
    
elif ans =='*' :
    print(a*b)

elif ans =='/' :
    print(a/b)

elif ans =='p' or ans == 'P' :
    print(a**b)

elif ans =='r' or ans == 'R' :
    print(a%b)

else :
    print("press the ringht key not "+ans)
    