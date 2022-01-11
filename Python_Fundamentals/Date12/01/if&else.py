# 1. Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).

#a = []
#for x in range(1500,2701):
#    if (x % 7== 0) and (x % 5 == 0):
#        a.append(x)
#print(a)
    

# 1-1. Write a Python program to find those numbers which are divisible by 11 and multiple of 6, between 250 and 4333 (both included).

#b = []
#for x in range(250, 4334):
#    if (x % 11 == 0) and (x % 6 == 0):
#        b.append(x)
#print(b)

#2. Write a Python program to guess a number between 1 to 9.
#Note : User is prompted to enter a guess. If the user guesses wrong then the prompt appears again until the guess is correct, on successful guess, user will get a "Well guessed!" message, and the program will exit.


#guess_num = int(input('Guess any number: '))

#for x in range(1, 10):
#    if (guess_num != x):
#        continue
#    else: 
#        print('Well guessed')  #but still not work properly


#3.  Write a Python program to count the number of even and odd numbers from a series of numbers.

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10) # Declaring the tuple
count_odd = 0
count_even = 0
for x in numbers:
        if not x % 2:
            count_even+=1
        else:
            count_odd+=1
print("Number of even numbers :",count_even)
print("Number of odd numbers :",count_odd)



    
        

    
    
        
    
        
        


