def checkyear(Year):   #function definition
  try:
      if((Year % 400 == 0) or  
      (Year % 100 != 0) and  
      (Year % 4 == 0)):   
        print("Given Year is a leap Year");  
   
      else:  
         print ("Given Year is not a leap Year"); 
  except:
    print("Input value is wrong");       
#derived class
Year = int(input("Enter the number: "));  
checkyear(Year);  #calling function
