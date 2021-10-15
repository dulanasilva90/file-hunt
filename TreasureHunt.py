#treasure hunt.
#find the code.

import os.path
import random

div="\n ---------------------------------- \n"
yay = "\n Yay you found the code!"


save_path = '/home/dulanasilva/Desktop'
file_name = "CODE1.txt" 
completeName = os.path.join(save_path, file_name)

code1 = str(random.randrange(20000,30000))
code2 = str(random.randrange(40000,50000))
code3 = str(random.randrange(50000,60000))

print ("\n FIND THE CODE! \n \n Find your first code \n (a file named 'CODE1.txt') ")

one= open(completeName,"w+") #create
one.write("your code is  : " + code1) #write
one.close() #close



q = str("Enter code to proceed:")

print("\n did you find the txt file? ")
a1 = str(input(q))

if a1 == str(code1):
   print(yay)
   print("\n \n your next text file is 'CODE2' ,duh")
   
   file_name="CODE2.txt"
   save_path = '/home/dulanasilva/Documents'
   completeName = os.path.join(save_path, file_name)
   two= open(completeName,"w+") #create
   two.write("your code is  : " + code2) #write
   two.close() #close
  
   a2 = str(input(q)) #ask for code
  

else:
    print("\n WRONG!, try again.")


if a2 == str(code2):
    print(yay)
    print("\n \n Now it is time your last code... \n Ready ,Set , Go!")
    file_name="CODE3.txt"
    save_path = '/home/dulanasilva/Music'
    completeName = os.path.join(save_path, file_name)
    tri= open(completeName,"w+") #create
    tri.write("your code is  : " + code3) #write
    tri.close() #close
  
    a3 = str(input(q)) #ask for code

else:
    print("\n WRONG!, try again.")


if a3 == str(code3):
    print(div)
    print("\n \n Well done! you have found the last code! ")
    
    file_name="yourPRIZE.txt"
    save_path = '/home/dulanasilva/Desktop'
    completeName = os.path.join(save_path, file_name)
    prize= open(completeName,"w+") #create
    prize.write("The best GIFT you can get is experience you get \n I hope this has been a nice treasure hunt for you... \n Made with python by Dulana Silva \n \n \n "  ) #write
 
   
    prize.close() #close 
    print("\n now for the prize. \n I have placed a txt file in your desktop folder. ")
    print("\n \n \n ---PROGRAM TERMINATED---")



else:
    print("\n WRONG!, try again.")