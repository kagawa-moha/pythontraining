#If you are testing multiple conditions, an if/else statement will not work.
#We use an if/elif ....else
# Take in an input from a user. Test for high(>70), medium(>40<70) or low(<440)
mynum = float(input("Enter number to test: "))

if (mynum>=0) and (mynum<=100):
    if mynum > 70:
       print("High")
    elif mynum < 70 and mynum > 40:
       print("Medium")
    else:
      print("Low") 
else:
   print("number invalid")
 

#in addition to what you have above. Ensure ensure the number entered by the user falls
#btwn 0 and 100