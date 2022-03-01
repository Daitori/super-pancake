from unittest import result


print("Multiplication Egyptienne.\n Taper le nombre: ");
num_mult=int(input());
print("Taper le nombre: ");
num_fois=int(input());
Result=0;
var_count=0;
while(num_mult!=0):
    var_count+=1;
    if(num_mult%2==1):
        Result+=num_fois;
    num_mult=num_mult//2;
    num_fois+=num_fois;
print(Result);

