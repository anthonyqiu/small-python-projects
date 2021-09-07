secret_word = "apple"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    # != means not equal
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True
        # Repeats the loop. Code only progresses if the conditions aren't true anymore.
        
if out_of_guesses:
    print("Out of guesses, you lose!")
else:
    print("You guessed the word!")
