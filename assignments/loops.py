def fizzbuzz():
  for i in range(1, 31): # Loop from 1 to 30
    if i % 3 == 0 and i % 5 == 0: # Check if divisible by both 3 and 5
      print("FizzBuzz")
    elif i % 3 == 0: # Check if divisible by 3 only
      print("Fizz")
    elif i % 5 == 0: # Check if divisible by 5 only
      print("Buzz")
    else: # If none of the above, print the number
      print(i)

fizzbuzz()





secret_number = 7  # The secret number to be guessed
guess = None       # Initialize guess to a non-matching value

print("I am thinking of a number. Can you guess what it is?")

while guess != secret_number:
    try:
        guess_input = input("Enter your guess: ")
        guess = int(guess_input)  # Convert input to an integer
        if guess != secret_number:
            print("That's not it. Try again.")
    except ValueError:
        print("Invalid input. Please enter a whole number.")

print("Correct! You win.")



