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

questions = [
    {
        'question': "1) What is the primary function of a CPU (Central Processing Unit)?\n"
                    "a) Graphics rendering\n"
                    "b) Memory storage\n"
                    "c) Data input/output\n"
                    "d) Processing instructions\n",
        'answer': "d"
    },
    {
        'question': "2) What does the GPU stand for in the context of computers?\n"
                    "a) General Processing Unit\n"
                    "b) Graphics Processing Unit\n"
                    "c) Global Power Utilization\n"
                    "d) General Productivity Upgrade\n",
        'answer': "b"
    },
    {
        'question': 'Which planet in our solar system is known as the "Red Planet"?\n'
                    "a) Venus\n"
                    "b) Saturn\n"
                    "c) Jupiter\n"
                    "d) Mars\n",
        'answer': "d"
    },
    {
        'question': '4) Which of the following is a renewable source of energy?\n'
                    "a) Coal\n"
                    "b) Natural Gas\n"
                    "c) Solar Power\n"
                    "d) Petroleum\n",
        'answer': "c"
    },
    {
        'question': "What is the largest continent on Earth?\n"
                    "a) Europe\n"
                    "b) Africa\n"
                    "c) Asia\n"
                    "d) South America\n",
        'answer': "c"
    }
]

for q in questions:
    print(q['question'])
    answerPicked = input("Answer = ").strip().lower()
    if answerPicked == q['answer']:
        print("Correct answer.\n")
        score += 1
    else:
        print(f"{q['answer']} is the correct answer.\n")

print(f"Your score is {score}")
