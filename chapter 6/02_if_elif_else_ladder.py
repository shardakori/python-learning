a =int(input("Enter your age :"))

# if elif else ladder statement

if(a>=20):
    print("you are above the age of consent")
    print("Good for you")

elif(a<0):
    print("you are entering the invalid negative age")

elif(a==0):
    print("you are entering 0 which is not a valid age")

else:
    print("you are below the age of cosent")

print("End of program")