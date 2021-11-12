"""
   @ Author - Nitish kumar Mehta
   @ Date - 07-nov-2021
   @ Time - 10:40
   @ Title - Sum of three Integer adds to ZERO
"""
import math

def GamblerGame(N,stack,goal):
    
    for i in range(N):
        if(stack>0 and stack<goal):
            if(math.random()<0.5):
                win=win+1;
                stack=stack+1;
                count=count+1;
            else:
                lose=lose+1;
                stack=stack-1;
                count=count-1;
        elif(stack>=goal):
            print("Reached the goal",i,"th number of gambler");
            break;
        else:
            print("out of stack after"+i+"th number of gambler");
            break;
        print("Number of wins=>",win);
        print("Percentage of game won=>",100*win/N);
        print("Percentage of game lose=>",100*lose/N);
        print("Average=>",1*count/N);

#derived class#
print("\n");
N=int(input("Enter the number of times"));
stack=int(input("Enter the stack"));
goal=int(input("Enter the goal"));
GamblerGame(N, stack, goal);
