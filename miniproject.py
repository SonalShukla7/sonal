x=("****************Welcome TO Ducat*******************")
print(x)
a=input("Please enter your  name:")
while(True):
     b=input("Please enter your mail id:")
     if("@" in b and ".com" in b):
          break
     else:
          print("enter mail again")
while(True):
     c=input("please enter your contact details:")
     if(c.isdigit()and len(c)==10):
          break
print("Hello",a)
d=("We deal in this course")
print(d)
f=("'python:1500000,'java':1000000,'Hadoop':50000,'AI':200000")
print(f)
e=input("please select your course")
g=("Thanks for applying",a)
print(g)
print("Name:",a)
print("Email:",b)
print("contact:",c)
h=input("please enter your course")
print("course:",h)
if(h=="python"):
     print("course:",h)
     print("Fees:1500000")
     print("GST(18%):27000.0")
     print("subtotal amount:1777000.0")
     print("duration:1 year")
     fees=1777000

elif(h=="java"):
      print("course:",h)
      print("Fees:1000000")
      print("GST(18%):27000.0")
      print("subtotal amount:1027000.0")
      print("duration:1 year")
      fees=1027000
elif(h=="hadoop"):
      print("course:",h)
      print("Fees:50000")
      print("GST(18%):27000.0")
      print("subtotal amount:57000.0")
      print("duration:1 year")
      fees=57000

elif(h=="AI"):
      print("course:",h)
      print("Fees:200000")
      print("GST(18%):27000.0")
      print("subtotal amount:277000.0")
      print("duration:1 year")
      fess=277000
i=input("How do you want to pay............(one time payment/Installation):")
if(i=="one time"):
        print("one time")
elif(i=="installation"):
        print("installation")
j=input("please select the installation period:3 months/per month/6 months:")
k=("'python:1500000,'java':1000000,'Hadoop':50000,'AI':200000")
if(j=="3 months"):
     print(fees/3)
elif(j=="per month"):
     print(fees)
elif(j=="6 months"):
     print(fees/6)

file=open("data.txt","a")
file.write(a+" "+b+" "+c+" "+h+" "+str(fees)+"\n")
file.close()

    

