low = 0
high = 100
ans = int(input("Please think of a number between 0 and 100! ")) # change to straight print stmt to let interpreter guess
is_correct = ''
while is_correct != 'c':
    guess = (high + low)//2
    print("Is your secret number " + str(guess) +"?")
    is_correct = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    if is_correct == 'h':
        high = guess
    elif is_correct == 'l':
        low = guess
    elif is_correct == 'c':
        break
    else:
        print("Sorry, I did not understand your input.")
print("Game over. Your secret number was:", guess)
