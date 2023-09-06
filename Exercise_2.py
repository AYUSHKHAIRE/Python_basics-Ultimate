print('Hello there! I am a programmer bacchan.\n ye aapko roadpati nhi bnne dega.')
print('Rule: You have to answer 3 questions, each with one correct answer.')
questions = [
    'What is the capital of India?',
    'What is the highest mountain in the world?',
    'Does gravity affect light?'
]
options = [
    ['Delhi', 'New Delhi', 'Mumbai', 'New Mumbai'],
    ['Mount Agret', 'Mount Everest', 'Mount Kenta', 'Mount Fenta'],
    ['May be', 'Not sure', 'Yes', 'No']
]
answers = [1, 2, 4]  # Index of the correct options
print('Let\'s get started!\n')
score = 0
for i in range(len(questions)):
    print('Question', i + 1, ":")
    print(questions[i])
    for j in range(4):
        print('Option', j + 1, ":", options[i][j])
    user_answer = int(input('Enter your answer (1/2/3/4): '))
    if user_answer == answers[i]:
        print('Correct!\n')
        score += 1
    else:
        print('Incorrect.\n')
print('Quiz complete!')
print('Your score:', score, '/', len(questions))
print('Your prize:', score*150, '/', len(questions*1000))
print('dedhsau rupaya degha \n')
