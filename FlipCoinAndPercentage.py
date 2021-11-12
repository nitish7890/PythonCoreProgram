import random;
import math;

def flipCoin(num):
   if(num<=0):
        head=0;
        tail=0;
   for i in range(num):
      coin=random.randint(0,1);
      if(coin<=0.5):
           tail=tail+1;
      else:
          head=head+1;

      print("Heads percentage=>");
      headPercentage=(head/num)*100;
      print(headPercentage);  
      print("Tails Percentage=>");
      tailPercentage=tail/num*100;
      print(tailPercentage);      

num = int(input("Enter the the number"));
flipCoin(num);