in1,in2,in3= map(int,input().split())
if(in1<=in2<=in3):
    print(in3)
elif(in1<=in3<=in2):
    print(in2)
else:
    print(in1)
