import math
def Calcute(X,Y):     #function definition
    try:
      result=math.sqrt(X*X+Y*Y);
      return(result);
    except:
        print("Please enter the correct number");


#derived class

X=int(input("Enter the value of x"));
Y=int(input("Enter the value of Y"));

print("Euclidean Distance===>",Calcute(X,Y));    #calling function
