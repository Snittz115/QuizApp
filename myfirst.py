from Question import Question
question_prompts = [
    "what color are Apple ? \n (a)Green \n (b)White \n (c)Orange \n \n",
    "what color are Bananas ? \n (a)Blue \n (b)White \n (c)Yellow \n \n",
    "what color are Roses ? \n (a)Black \n (b)Blue \n (c)Red \n \n",

]


questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "c"),
]


def start_test():
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + " out of " + str(len(questions)) + " correct ")


start_test()
