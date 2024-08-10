def main():
    # Define a string containing the correct answers.
    CORRECT_ANSWERS = "adbdcacbdac"

# initialize string
user_answers = ""

# Enter Exam answers (error message for incorrect number !=10)
user_answers = str(input("Enter your answer choices, lowercase, no spaces: "))

# valid input 
valid_input = len(user_answers) == 11
if not valid_input:
    print("Incorrect number of answers entered!")

# Compare user's answers to answer key 
correct_count = 0
test_result = ""

for i in range(len(CORRECT_ANSWERS)):
    if i < len(user_answers) and user_answers[i] == CORRECT_ANSWERS[i] :
        test_result += user_answers[i]
        correct_count += 1
    else:
        test_result += "X"
        correct_count += 0
# show correct answers (as a string) and use X for incorrect
print("Correct answer: ", CORRECT_ANSWERS)
print("Your answer: ", str(test_result)) 

# Calculate and display score as a percentage 
score = correct_count * 10
# Feedback for 100% scores
if score == 100:
    print("Very good!")
else:
    print("Number of correct answers: ", correct_count)
    print("Your score: ", score)


if __name__ == "__main__":
    main()