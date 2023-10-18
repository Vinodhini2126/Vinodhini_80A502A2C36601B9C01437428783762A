
n=int(input("enter year "));
if n%100==0 and n%400==0 :
  print("Its a Leap Year");
elif (n%4) and (n%100!=0):
  print("Leap Year");
else:
  print('Not leap year');
