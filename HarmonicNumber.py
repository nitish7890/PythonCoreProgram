def calc(Num):
    try:
        for i in range(1,Num+1):
           Harmonic=0;
           Harmonic=Harmonic+1/i;
        print("Harmonic Number=>",Harmonic);  
    except:
        print("Value out of range");         

#derived class
Num=int(input("Enter the value of range"));
calc(Num);    