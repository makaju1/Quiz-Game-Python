Quiz-Game-Python
Welcome to the Quiz Game for Kids! This simple Python program allows you to add more questions easily. Just follow the template below:

question = print("1) *Question ? \na) *Option1 \nb) *Option2 \nc) *Option3 \nd) *Option4 \n")
answerPicked = input("Your Answer: ").lower()
correctAnswer = "*correct answer"

if answerPicked == correctAnswer:
    print("Correct answer!\n")
    score += 1
else:
    print(correctAnswer + " is the correct answer.\n")

Feel free to add new questions by copying and pasting the above code and replacing the placeholders indicated by asterisks (*).
Make sure to customize the question, options, and correct answer accordingly.
Enjoy the game and have fun!

Note: Ensure that you have the score variable initialized somewhere in your code before using it in this quiz script. Happy coding!
