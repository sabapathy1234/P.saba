num1=int(input())
temp=num1
revnum1=0
while(num1>0):
  digit=num1%10
  revnum1=revnum1*10+digit
  num1=num1//10
if(temp==revnum1):
  print("yes")
else:
  print("no")
