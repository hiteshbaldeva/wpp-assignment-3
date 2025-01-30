#You are given a number N, you need to print the number of positions where digits exactly divides N.
#Input format 
#The first line contains T (number of test cases followed by T lines each containing N). 
#Constraints 
#1 <= T <= 15 
#0 <= N <= 1010 

T = int(input("enter the number of test cases"))
numbers = []
for i in range(0,T):
        print(f"enter a number {i+1}:")
        n = int((input()) )                                     
        numbers.append(n)
       
print(numbers)
divisible =[]

for i in numbers:
       count,n = 0,i
       while (i>0):
                
                rem = i%10
                i //= 10
                if rem != 0:
                        if n%rem == 0:
                                count += 1
       divisible.append(count)

print(divisible)
        
         



    