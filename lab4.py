import numpy as np
import re
first=np.zeros((3,3))
second=np.zeros((3,3))
def addition(first,second):
   print("you selected addition. the results are")
   return np.add(first,second)
def substraction(first,second):
   print("you selected substraction. the results are")
   return np.sub(first,second)
def multiplication(first,second):
   print("you selected multiplication. the results are")
   return np.matmul(first,second)
def elemultiplication(first,second):
   print("you selected element by multiplication. the results are")
   return np.multiply(first,second)

while 1:
   print("Do you wish to play the Matrix Game?")
   op=input("Enter Y for Yes or N for No:")
   print("Enter your phone number(xxx-xxx-xxxx):")
   while 1:
       ph=input()
       if(re.match("\d{3}[-]\d{3}[-]\d{4}", ph)):
           break
       else:
           print("Your phone number is not in correct format please try again")
   print("Enter your zip code +4 (xxxxx-xxxx):")
   while 1:
       zp=input()
       if(re.match("\d{5}[-]\d{4}", zp)):
           break
       else:
           print("Your zip code is not in correct format please try again")
   print("Enter your first 3x3 matrix")
   for i in range(3):
       for j in range(3):
           first[i][j]=input()
   print("your first 3x3 matrix is")
 #  for i in range(3):
     #  for j in range(3):
           #print(first[i][j],end=' ')
      # print()
   print("Enter your second 3x3 matrix")
   for i in range(3):
       for j in range(3):
           second[i][j]=input()
   print("your second 3x3 matrix is")
   #for i in range(3):
     #  for j in range(3):
       #    print(second[i][j],end=' ')
       #print()
   print("select a Matrix operation from the list below \n a. addition b. substraction\n c. matrix multiplication\n d. element by element multiplication\n")
   op=input()
   res=np.zeros((3,3))
   if(op=='a'):
       res=addition(first,second)
   elif(op=='b'):
       res=substraction(first,second)
   elif(op=='c'):
       res=multiplication(first,second)
   elif(op=='d'):
       res=elemultiplication(first,second)
   else:
       print("invalid option")
   #for i in range(3):
       f#or j in range(3):
           #print(res[i][j],end=' ')
       #print()
   print("The transpose is")
 #  for i in range(3):
   #    for j in range(3):
     #      print(res[j][i],end=' ')
       #print()
   print("The row and column mean values of the matrix are")
   rw=np.zeros(3)
   cl=np.zeros(3)
   for i in range(3):
       for j in range(3):
           rw[i]+=res[i][j]
           cl[j]+=res[i][j]
   print("Row:",rw[0]/3,rw[1]/3,rw[2]/3)
   print("column:",cl[0]/3,cl[1]/3,cl[2]/3)