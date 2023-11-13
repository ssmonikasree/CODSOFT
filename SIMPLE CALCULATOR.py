print("SIMPLE CALCULATOR")
print("-----------------")
print('''Select Operation:
      1. Add
      2. Subtract
      3. Multiply
      4. Division
      5. Exponent
      6. Exit''')
while True:
    ch = int(input("Enter choice"))
    if ch==6:
        print('Exit')
        break
    num1=int(input("Enter an integer 1"))
    num2=int(input("Enter an integer 2"))
    if ch==1:
        res=num1+num2
        print("The sum of",num1,"and",num2,'is',res)
    elif ch==2:
        if num1>num2:
            res=num1-num2
        else:
            res=num2-num1
        print("The difference of",num1,"and",num2,'is',res)
    elif ch==3:
        res=num1*num2
        print("The product of",num1,"and",num2,'is',res)
    elif ch==4:
          try:
              res=num1/num2
              print("The division of",num1,"and",num2,'is',res)
          except ZeroDivisionError as e:
              print(e)
    elif ch==5:
        res = num1**num2
        print(num1,"power",num2,'is',res)
    else:
        print("Invalid choice")


   
  




    
