print("Conjecture Syracuse.\n Taper un nombre: ");
num=int(input());
t=0;
while t==0:
    print(num);
    if(num%2)==0:
        num=num/2;
    else:
        if num==1:
            t=1;
        else:
            num=(num*3)+1;