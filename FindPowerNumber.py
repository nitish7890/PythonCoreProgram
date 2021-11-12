def power(num):  #function definition
  try:
    result=2**num;
    print("Square of the number=>",result);
  except:
    print("Please enter the correct Number");  

#derived class
num=int(input("Enter the value of Number"));
power(num);   #calling function
