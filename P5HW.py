#Emanuel Smith
#12/7/2023
#Math quiz, using functions,random numbers,and while loop
#will need to import random library
#will need a while loop for main code
#another loop for
#need three functions menu() add() subtract()

import random

#create menu function, this function
def show_menu():
    print("Welcome to Math Quiz")
    print()
    print("_______________")
    print("1. Adding Random Numbers")
    print("2. Subtracting Random Numbers")
    print("3. Exit")
    print()

#This function adds two random numbers
def add():
    ran1= random.randint(0,10)
    ran2= random.randint(0,10)
    print(f"{ran1} + {ran2}")
    return (ran1+ran2)

#This function subtracts two random numbers
def subtract():
    ran1= random.randint(0,10)
    ran2= random.randint(0,10)
    print(f"{ran1} - {ran2}")
    return (ran1-ran2)

#This function simulates the user guessing.
#While the guess is wrong, allow the user to guess again
def guessing (guess, correct_answer):
    num_guesses = 0
    while guess != correct_answer:
        num_guesses += 1
        if guess > correct_answer:  #If user guesses too high
            print("Your guess is too high")
            guess= int(input("Guess again:  ")) #This represents guess
        else:                        #If user guesses to low
            print("Your guess is to low")
            guess= int(input("Guess Again:  ")) #This represents guess
    #User answer is correct while the loop breaks
            print("Your answer is correct!!!")
           
            print(f"It took you {num_guesses} incorrect guesses to get it right")

#get input from user


#Main Function
def main():
    show_menu()
    user_option = int(input("Please choose one of the menu options:  "))
    while user_option !=3:
        if user_option ==1:
            ran_sum=add()     #Represents the same answer
            my_guess = int(input("What is your guess?  "))  #This represents guess
            guessing (my_guess, ran_sum)
            print()
            show_menu()
            user_option = int(input("Please choose one of the menu options:  "))

        if user_option ==2:
            ran_sum = subtract()    #Represents the same answer
            my_guess = int(input("What is your guess?  "))   #This represents
            guessing (my_guess, ran_sum)
            show_menu()
            user_option = int(input("Please choose one of the menu options:  "))
        if user_choice == 3:the while loop breaks
            print("Thank you for playing goodbye")
    
            

# call the main function
        if __name__=="__main__":
            main()
        




    print



            
        

        





























   


