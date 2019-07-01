h11,m11= map(int, input().split())
h21,m21= map(int, input().split())
if(h11>h21):
    z=h11-h21
    y=m11-m21
    print(z,y)
else:
    t=h21-h11
    s=m21-m11
    print(t,s)
