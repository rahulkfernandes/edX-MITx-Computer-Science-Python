print("Please think of a number between 0 and 100!")

low = 0
high = 100
guess = (low + high) // 2

while True:
    print(f"Is your secret number {guess}?")
    feedback = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    
    if feedback == 'c':
        print(f"Game over. Your secret number was: {guess}")
        break
    elif feedback == 'h':
        high = guess
    elif feedback == 'l':
        low = guess
    else:
        print("Invalid input, please enter 'h', 'l', or 'c'.")
    
    guess = (low + high) // 2
