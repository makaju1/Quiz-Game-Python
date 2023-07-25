print('''
 $$$$$$\            $$\                  $$$$$$\                                    
$$  __$$\           \__|                $$  __$$\                                   
$$ /  $$ |$$\   $$\ $$\ $$$$$$$$\       $$ /  \__| $$$$$$\  $$$$$$\$$$$\   $$$$$$\  
$$ |  $$ |$$ |  $$ |$$ |\____$$  |      $$ |$$$$\  \____$$\ $$  _$$  _$$\ $$  __$$\ 
$$ |  $$ |$$ |  $$ |$$ |  $$$$ _/       $$ |\_$$ | $$$$$$$ |$$ / $$ / $$ |$$$$$$$$ |
$$ $$\$$ |$$ |  $$ |$$ | $$  _/         $$ |  $$ |$$  __$$ |$$ | $$ | $$ |$$   ____|
\$$$$$$ / \$$$$$$  |$$ |$$$$$$$$\       \$$$$$$  |\$$$$$$$ |$$ | $$ | $$ |\$$$$$$$\ 
 \___$$$\  \______/ \__|\________|       \______/  \_______|\__| \__| \__| \_______|
     \___|                                                                          
''')
print("!!!Welcome to the quiz game!!!\n")
score = 0

# Question 1
question = print("1) What is the primary function of a CPU (Central Processing Unit)? \na) Graphics rendering \nb) Memory storage \nc) Data input/output \nd) Processing instructions\n ")
answerPicked = input("Answer = ".lower())
answer = "d"

if answer == answerPicked:
    print("Correct answer.\n")
    score +=1
else:
    print (answer + (" is the correct answer.\n"))
    
# Question 2
question = print("2) What does the GPU stand for in the context of computers? \na) General Processing Unit \nb) Graphics Processing Unit \nc) Global Power Utilization \nd) General Productivity Upgrade\n ")
answerPicked = input("Answer = ".lower())
answer = "b"

if answer == answerPicked:
    print("Correct answer.\n")
    score +=1
else:
    print (answer + (" is the correct answer.\n"))    

# Question 3
question = print('Which planet in our solar system is known as the "Red Planet"?\na) Venus \nb) Saturn \nc) Jupiter \nd) Mars\n ')
answerPicked = input("Answer = ".lower())
answer = "d"

if answer == answerPicked:
    print("Correct answer.\n")
    score +=1
else:
    print (answer + (" is the correct answer.\n"))    


# Question 4

question = print('4) Which of the following is a renewable source of energy?\na) Coal \nb) Natural Gas \nc) Solar Power \nd) Petroleum \n ')
answerPicked = input("Answer = ".lower())
answer = "c"

if answer == answerPicked:
    print("Correct answer.\n")
    score +=1
else:
    print (answer + (" is the correct answer.\n"))    


# Question 5 

question = print("Who is credited with inventing the telephone? \na) Alexander Graham Bell \nb) Thomas Edison \nc) Nikola Tesla \nd) Isaac Newton\n ")
answerPicked = input("Answer = ".lower())
answer = "a"

if answer == answerPicked:
    print("Correct answer.\n")
    score +=1
else:
    print (answer + (" is the correct answer.\n"))    


print (f"Your scored is {score}")