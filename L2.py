import random

print("Welcome to the Multiplication Quiz!")

#Initialize score and number of problems
score = 0
number_of_problems = 5

#Start the main game loop to ask 'number_of_problems'
for i in range(number_of_problems):

    #Generate two random numbers between 1 and 10
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    correct_answer = num1 * num2

    #Ask the question
    print(f"\nQuestion #{i + 1}: What is {num1} * {num2}?")

    # Input validation loop: Keep asking until user enters a valid number
    while True:
        user_input_str = input("Your answer: ")

        # Check if the input string consists only of digits
        if user_input_str.isdigit():
            user_answer = int(user_input_str)  # Convert string to integer
            break
        else:
            print("Error: Please enter a valid number.")

    # Check if the user's answer is correct
    if user_answer == correct_answer:
        print("Correct!")
        score += 1  # Increment score
    else:
        print(f"Incorrect! The correct answer was: {correct_answer}")

# After the loop finishes, display the final score
print("\nGame Over!")
print(f"Thank you for playing! The final score was {score} out of {number_of_problems}")