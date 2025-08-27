marks1 = int(input("Enter the marks 1 : "))
marks2 = int(input("Enter the marks 2 : "))
marks3 = int(input("Enter the marks 3 : "))

total_percentage = (100*(marks1 + marks2 + marks3))/300
if(total_percentage>=40 and marks1>35 and marks2>35 and marks3>35):
    print("you are pass" , total_percentage)

else:
    print("you are failed" , total_percentage)
