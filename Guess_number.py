import random

def main():
    # Generate a random number between 1 and 10
    rand = num_generator()
    
    while True:
        try:
            # Get user's guess as an integer
            user = int(input("Guess a number between 1 and 10: "))

            # Check if guess is within range
            if user < 1 or user > 10:
                print("Please enter a number between 1 and 10!")
                continue
            
            # Check if the guess is correct
            if user == rand:
                print("You have guessed the number correctly!")
                break
            elif user < rand:
                print(f"The number is higher than {user}. Try again.")
            else:
                print(f"The number is lower than {user}. Try again.")
        
        except ValueError:
            print("Invalid input. Please enter a number.")
    

def num_generator():
    # Generates a random number between 1 and 10
    return random.randint(1, 10)

if __name__ == "__main__":
    main()
